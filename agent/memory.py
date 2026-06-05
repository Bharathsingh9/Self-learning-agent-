from typing import List, Dict, Any

class Memory:
    """
    Short-Term Memory System:
    Stores the outputs of previously executed tasks to provide context 
    avoiding redundant processing and maintaining consistency.
    """
    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    def add_record(self, task_id: int, description: str, result: str):
        """Add a completed task result to memory."""
        self.history.append({
            "task_id": task_id,
            "description": description,
            "result": result
        })

    def get_context(self) -> str:
        """
        Retrieves all past context formulated as a string for the LLM to read.
        In a more advanced system, this could use semantic search or summarization 
        to avoid exceeding token limits.
        """
        if not self.history:
            return "No previous tasks executed yet."
            
        context_str = "--- PREVIOUS TASK CONTEXT ---\n"
        for record in self.history:
            context_str += f"Task ID {record['task_id']} - {record['description']}:\n"
            context_str += f"Output:\n{record['result']}\n"
            context_str += "-" * 30 + "\n"
        
        return context_str

    def clear(self):
        """Reset memory for a new overarching goal."""
        self.history = []
