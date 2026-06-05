import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

# Ensure parent path config is accessible
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agent.planner import Planner
from agent.executor import Executor
from agent.memory import Memory
from agent.tools import ToolManager
from agent.file_handler import FileHandler
from config import Config

console = Console()

def main():
    """
    Main entry point for the Autonomous Task AI Agent CLI interface.
    Connects the planner, executor, tools, memory, and file handler.
    """
    console.print(Panel.fit("[bold green]Autonomous Task AI Agent[/bold green]", subtitle="Goal-Oriented Execution Engine"))
    
    if not Config.GROQ_API_KEY:
        console.print("[bold yellow]Warning:[/bold yellow] GROQ_API_KEY is not set. Please update your .env file or config.py.")
        # Removed sys.exit(1) to try running if environment allows

    # Bootstrapping modules
    try:
        planner = Planner()
        memory = Memory()
        tool_manager = ToolManager()
        file_handler = FileHandler()
        executor = Executor(memory, tool_manager, file_handler)
    except Exception as e:
        console.print(f"[bold red]Initialization Error:[/bold red] {e}")
        sys.exit(1)
    
    while True:
        goal = Prompt.ask("\n[bold cyan]Enter a high-level goal (or 'exit' to quit)[/bold cyan]")
        if goal.lower() in ('exit', 'quit'):
            console.print("[yellow]Shutting down...[/yellow]")
            break
            
        console.print(f"\n[bold yellow]Goal registered:[/bold yellow] {goal}")
        memory.clear() # Fresh context for a new overarching goal
        
        # Phase 1: Planning
        with console.status("[bold blue]Planning tasks using LLM..."):
            plan = planner.create_plan(goal)
            
        if not plan or not plan.tasks:
            console.print("[red]Failed to generate a cohesive plan. Try a different goal.[/red]")
            continue
            
        console.print("\n[bold magenta]Execution Plan:[/bold magenta]")
        for task in plan.tasks:
            console.print(f"  [cyan]{task.id}.[/cyan] {task.description}")
            
        proceed = Prompt.ask("\nProceed with execution?", choices=["y", "n"], default="y")
        if proceed == 'n':
            console.print("[yellow]Execution cancelled.[/yellow]")
            continue
            
        console.print("\n[bold green]--- Starting Execution ---[/bold green]")
        
        # Phase 2: Context-Aware Execution
        for task in plan.tasks:
            console.print(f"\n[bold blue]>> Executing Task {task.id}:[/bold blue] {task.description}")
            
            with console.status(f"[bold cyan]Working on task {task.id} (including QA loop)..."):
                final_output = executor.execute_task(task)
            
            console.print(f"[bold green]Task {task.id} Completed![/bold green]")
            
            # Print a snippet of the output
            preview = final_output[:250] + "\n... [truncated]" if len(final_output) > 250 else final_output
            console.print(Panel(preview, title="Task Output Preview", border_style="dim"))
            
        console.print(f"\n[bold green]Goal Accomplished![/bold green] All tasks completed successfully.")
        console.print(f"Check the [bold yellow]{Config.OUTPUT_DIR}[/bold yellow] directory for generated files.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Force aborted by user.[/red]")
        sys.exit(0)
