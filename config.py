import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

class Config:
    """
    Centralized configuration for the Autonomous Task AI Agent.
    """
    # Groq settings
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
    
    # Execution constraints
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
    MAX_TASKS = int(os.getenv("MAX_TASKS", "10"))
    
    # Path settings
    OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output")

# Ensure output directory exists globally
if not os.path.exists(Config.OUTPUT_DIR):
    os.makedirs(Config.OUTPUT_DIR)
