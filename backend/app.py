import os
import re
import json
import asyncio
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

# Initialize environment and configuration
load_dotenv()

app = FastAPI()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Ensure the required output directory exists globally
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Configuration and State Management
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the frontend directory
FRONTEND_DIR = Path(__file__).parent.parent / "frontend"
if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/")
async def read_index():
    return FileResponse(FRONTEND_DIR / "index.html")

class GoalRequest(BaseModel):
    goal: str

class OrchestratorState:
    """Maintains the real-time state of the autonomous engineering system."""
    def __init__(self):
        self.status = "IDLE"
        self.plan = []
        self.logs = []
        self.active_task = None

    def add_log(self, msg: str):
        self.logs.append(msg)
        print(f"[SYSTEM LOG] {msg}")

    def reset(self):
        self.status = "RUNNING"
        self.plan = []
        self.logs = []
        self.active_task = None

state = OrchestratorState()

# --- Core Autonomous Logic ---

def validate(result: dict) -> bool:
    """
    Validates the structured output from the LLM.
    Ensures 'files' key exists and contains at least one non-empty file.
    """
    if not isinstance(result, dict) or "files" not in result:
        return False
    files = result.get("files", [])
    if not isinstance(files, list) or len(files) == 0:
        return False
    return all(f.get("path") and f.get("content") for f in files)

def generate_file_list(goal: str, task_desc: str) -> list:
    """Ask LLM for a list of files needed for a specific task."""
    prompt = f"Goal: {goal}\nTask: {task_desc}\nList ONLY the relative file paths needed for this task. No URLs or explanations. Respond ONLY JSON: {{'files': ['src/main.py', ...]}}"
    try:
        completion = client.chat.completions.create(
            model=os.getenv("MODEL_NAME", "llama-3.1-8b-instant"),
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        files = json.loads(completion.choices[0].message.content).get("files", [])
        # Strict sanitization: remove any paths that look like URLs or have invalid chars
        sanitized = []
        for f in files:
            clean = re.sub(r'[:*?"<>|]', '', f).strip("/")
            if clean and not clean.startswith("http"):
                sanitized.append(clean)
        return sanitized
    except: return []

def generate_file_content(goal: str, task_desc: str, file_path: str) -> str:
    """Generate content for a specific file."""
    prompt = f"Goal: {goal}\nTask: {task_desc}\nFile: {file_path}\nWrite the COMPLETE code for this file. No explanations. Code only."
    try:
        completion = client.chat.completions.create(
            model=os.getenv("MODEL_NAME", "llama-3.1-8b-instant"),
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content.strip().strip("`").replace("```python", "").replace("```javascript", "").replace("```html", "").replace("```css", "").replace("```", "")
    except: return ""

def save_single_file(project_id: str, path: str, content: str):
    """Saves a single file to the project directory."""
    full_path = OUTPUT_DIR / project_id / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

def save_project(files: list, target_subdir: str):
    """
    Saves generated file objects to the local filesystem.
    Creates necessary directories and handles file writing.
    """
    project_root = OUTPUT_DIR / target_subdir
    project_root.mkdir(parents=True, exist_ok=True)
    
    for file_data in files:
        file_path = project_root / file_data["path"]
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_data["content"])

async def real_execution_loop(goal: str):
    print(f"DEBUG: Starting real_execution_loop with goal: {goal}")
    state.add_log("Analyzing goal...")
    # Sanitize goal to create a valid directory name
    project_id = re.sub(r'[^a-zA-Z0-9_]', '', goal.replace(" ", "_"))[:30]
    if not project_id:
        project_id = "unnamed_project"
    
    try:
        # Phase 1: Planning
        state.add_log("Generating project structure...")
        plan_prompt = f"Break down this goal into 5 small, specific architectural tasks: {goal}. Respond ONLY JSON: {{'tasks': [{{'id': 1, 'desc': '...'}}]}}"
        
        try:
            res = client.chat.completions.create(
                model=os.getenv("MODEL_NAME", "llama-3.1-8b-instant"),
                messages=[{"role": "user", "content": plan_prompt}],
                response_format={"type": "json_object"}
            )
            state.plan = json.loads(res.choices[0].message.content).get("tasks", [])
        except Exception as e:
            state.status = "ERROR"
            state.add_log(f"System failure during planning: {e}")
            return

        # Phase 2: Granular Real Execution
        for task in state.plan:
            state.active_task = task['desc']
            state.add_log(f"Executing: {task['desc']}")
            
            # 1. Get file list for this specific sub-task
            file_list = generate_file_list(goal, task['desc'])
            if not file_list:
                state.add_log(f"Skipping task (no files defined): {task['desc']}")
                continue
                
            # 2. Generate and save each file individually
            for file_path in file_list:
                state.add_log(f"Writing {file_path}...")
                content = generate_file_content(goal, task['desc'], file_path)
                if content:
                    save_single_file(project_id, file_path, content)
                else:
                    state.add_log(f"Warning: Failed to generate content for {file_path}")

        state.status = "IDLE"
        state.active_task = None
        state.add_log("Mission Accomplished.")
        state.add_log(f"Project saved in /output/{project_id}")
    except Exception as e:
        state.status = "ERROR"
        state.add_log(f"Unhandled execution error: {str(e)}")
    finally:
        if state.status == "RUNNING":
            state.status = "IDLE"

# --- API Endpoints ---

@app.get("/api/status")
async def get_status():
    return {
        "status": state.status,
        "plan": state.plan,
        "logs": state.logs,
        "active_task": state.active_task
    }

@app.post("/api/start")
async def start_mission(req: GoalRequest):
    print(f"DEBUG: Received start_mission request for goal: {req.goal}")
    if state.status == "RUNNING":
        raise HTTPException(status_code=400, detail=f"System engaged: {state.active_task or 'Initializing'}")
    
    state.reset()
    print("DEBUG: state.reset() called")
    asyncio.create_task(real_execution_loop(req.goal))
    print("DEBUG: asyncio.create_task called")
    return {"status": "initiated", "goal": req.goal}

@app.post("/api/reset")
async def reset_system():
    state.status = "IDLE"
    state.active_task = None
    state.add_log("System manually reset to IDLE.")
    return {"status": "reset"}

if __name__ == "__main__":
    import uvicorn
    # Check for API Key presence before launch
    if not os.getenv("GROQ_API_KEY"):
        print("CRITICAL ERROR: GROQ_API_KEY missing from environment.")
    else:
        uvicorn.run(app, host="0.0.0.0", port=8000)
