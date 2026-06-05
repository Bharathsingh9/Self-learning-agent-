import os
from models import groq_client

def plan_project():
    # Create a directory for the project
    project_dir = 'project_structure'
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)

    # Get the updated project structure
    plan = groq_client.plan_project()
    return plan

plan = plan_project()
print(plan)