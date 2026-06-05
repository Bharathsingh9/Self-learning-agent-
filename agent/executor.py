from pydantic import BaseModel, Field
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from agent.memory import Memory
from agent.tools import ToolManager
from agent.file_handler import FileHandler
from agent.planner import TaskItem
from agent.llm import generate_response, extract_json

class Evaluation(BaseModel):
    is_success: bool = Field(description="True if the output correctly fulfills the task requirements")
    feedback: str = Field(description="Constructive feedback if failed, or brief confirmation if successful")

class Executor:
    """
    Executes individual tasks using context, tools, and a feedback loop for improvement.
    """
    def __init__(self, memory: Memory, tool_manager: ToolManager, file_handler: FileHandler):
        self.memory = memory
        self.tool_manager = tool_manager
        self.file_handler = file_handler

    def execute_task(self, task: TaskItem) -> str:
        """Executes a task with an iterative improvement loop."""
        
        # Tool usage phase (Optional simplistic tool routing)
        tool_data = "No external tool data gathered for this task."
        if "research" in task.description.lower() or "search" in task.description.lower():
            query = f"{task.description}"
            tool_data = f"Search Results: {self.tool_manager.execute_tool('search', query)}"

        context = self.memory.get_context()
        feedback = "None - initial attempt."
        final_output = ""
        
        for attempt in range(Config.MAX_RETRIES):
            print(f"  -> Attempt {attempt + 1}/{Config.MAX_RETRIES} for Task {task.id}")
            
            # Execute
            exec_prompt = (
                "You are an autonomous AI agent. Your goal is to execute the given task as perfectly as possible.\n"
                "If you need to generate code, wrap it in standard markdown blocks (e.g. ```html ... ```).\n"
                "If you need to define a filename, use the format 'File: filename.ext' before the code block.\n\n"
                f"You have access to the following current context:\n{context}\n\n"
                f"You also have access to tool outputs:\n{tool_data}\n\n"
                f"If you were given previous feedback to improve, consider it: {feedback}\n\n"
                f"Task ID: {task.id}\n"
                f"Task Description: {task.description}\n"
                f"Expected Output: {task.expected_output}"
            )
            output = generate_response(exec_prompt)
            
            # Evaluate
            eval_prompt = (
                "You are a senior AI quality assurance engineer. Evaluate the following output against its task description and expected output.\n"
                "Ensure it is complete, correct, and contains no obvious placeholders (unless instructed to).\n\n"
                f"Task: {task.description}\n"
                f"Expected: {task.expected_output}\n\n"
                f"Output to evaluate:\n{output}\n\n"
                "Check if the output satisfies the task.\n"
                "Return ONLY valid JSON. No explanation.\n"
                "Expected format:\n"
                "{\n"
                '  "is_success": true/false,\n'
                '  "feedback": "short reason"\n'
                "}"
            )
            
            try:
                eval_response = generate_response(eval_prompt)
                eval_data = extract_json(eval_response)
                evaluation = Evaluation(**eval_data)
            except Exception as e:
                print(f"  -> Evaluation failed: {e}. Moving on with current output.")
                final_output = output
                break

            if evaluation.is_success:
                print(f"  -> Task {task.id} succeeded. QA Feedback: {evaluation.feedback}")
                final_output = output
                break
            else:
                print(f"  -> Task {task.id} needs improvement.\n  -> Feedback: {evaluation.feedback}")
                feedback = evaluation.feedback
                final_output = output # Keep latest in case all retries fail
        
        # Extract files if any
        saved_files = self.file_handler.extract_and_save_files(final_output, task.id)
        if saved_files:
            file_summary = "\nSaved files: " + ", ".join(saved_files)
            final_output += file_summary
            print(f"  -> {file_summary}")

        # Store in memory
        self.memory.add_record(task.id, task.description, final_output)
        
        return final_output
