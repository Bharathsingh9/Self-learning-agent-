from pydantic import BaseModel, Field
from typing import List
import sys
import os

# Add parent dir to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config
from agent.llm import generate_response, extract_json

class TaskItem(BaseModel):
    id: int = Field(description="Unique incremental ID for the task")
    description: str = Field(description="Actionable description of what needs to be done. E.g. 'Create index.html with basic layout'")
    expected_output: str = Field(description="What the outcome or artifact of this task should be. E.g. 'index.html file with standard boilerplate'")

class Plan(BaseModel):
    tasks: List[TaskItem] = Field(description="List of tasks to achieve the goal in sequential order")

class Planner:
    """
    Goal-Oriented Planner:
    Takes a high-level goal and breaks it down into structured, actionable subtasks.
    """
    def __init__(self):
        pass

    def create_plan(self, goal: str) -> Plan:
        """Generate a sequential plan for a given goal."""
        prompt = (
            "You are an expert AI software architect and project manager.\n"
            "Your job is to break down the user's high-level goal into a logical, sequential list of actionable, technical tasks.\n"
            "Ensure the tasks are explicit, and each focuses on a single tangible, independent output that can be passed to the next step.\n"
            "\n"
            f"Goal: {goal}\n"
            "\n"
            "Return ONLY valid JSON. No explanation.\n"
            "Expected format:\n"
            "{\n"
            '  "tasks": [\n'
            "    {\n"
            '      "id": 1,\n'
            '      "description": "...",\n'
            '      "expected_output": "..."\n'
            "    }\n"
            "  ]\n"
            "}"
        )
        
        try:
            response_text = generate_response(prompt)
            plan_data = extract_json(response_text)
            return Plan(**plan_data)
        except Exception as e:
            print(f"Error during planning: {e}")
            return Plan(tasks=[])
