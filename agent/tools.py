import time

class SearchTool:
    """
    A Tool for searching the web. We use a mock implementation here 
    that simulates looking up documentation or search results to keep it simple,
    but it can easily be swapped with a real API like SerpAPI.
    """
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        # For a real implementation using SerpAPI:
        # from langchain_community.utilities import SerpAPIWrapper
        # self.search_engine = SerpAPIWrapper(serpapi_api_key=api_key)

    def search(self, query: str) -> str:
        """
        Executes a web search for the given query.
        Returns a string representation of the results.
        """
        print(f"[Tool] Searching web for: '{query}'...")
        time.sleep(1) # Simulate network delay
        
        # Mock responses based on typical queries
        query_lower = query.lower()
        if "html" in query_lower or "css" in query_lower:
            return "MDN Web Docs: Standard HTML5 boilerplate includes <!DOCTYPE html>, <html>, <head> with meta tags, and <body>. CSS can be linked using <link rel='stylesheet' href='style.css'>."
        elif "python" in query_lower:
            return "Python Documentation: Use def to define functions. Standard best practices recommend type hinting and docstrings."
        else:
            return f"Mock Search Results for '{query}': Found 3 relevant articles discussing modern best practices and examples."

class ToolManager:
    """Manager to handle available tools."""
    def __init__(self):
        self.search_tool = SearchTool()
        
    def execute_tool(self, tool_name: str, query: str) -> str:
        if tool_name.lower() == "search":
            return self.search_tool.search(query)
        return f"Error: Tool '{tool_name}' not recognized."
