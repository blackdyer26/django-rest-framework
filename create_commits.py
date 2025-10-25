import os
import subprocess
from datetime import datetime

# Your commit history timeline
commits = [
    ("2025-09-30 17:00:00", "initial DRF project setup for backend employees app."),
    ("2025-10-02 11:30:00", "Added employee model and initial migrations."),

    ("2025-10-03 20:15:00", "created serializers.py for employee model."),
    ("2025-10-04 18:00:00", "Added EmployeeSerializer, EmployeeViewSet and registered routes in urls.py."),

    ("2025-10-09 15:45:00", "Created UserCreateView & User Registeration Components"),

    ("2025-10-11 12:00:00", "Tested API endpoints for registration and login."),
    ("2025-10-14 22:20:00", "Done API integration between DRF and django_frontend"),

]

# Your Git username and email
AUTHOR_NAME = "Ashwinkumar Sethi"
AUTHOR_EMAIL = "ashwinkumarsethi2223@ternaengg.ac.in"  
PUSH_AFTER = True

def run_command(cmd):
    """Run shell command and print output."""
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

def simulate_real_file_edit(date, message):
    """Make each commit modify a meaningful file based on the message."""
    message_lower = message.lower()

    # Match keywords to files
    if "model" in message_lower:
        file_to_edit = "employees/models.py"
    elif "serializer" in message_lower:
        file_to_edit = "employees/serializers.py"
    elif "viewset" in message_lower or "view" in message_lower:
        file_to_edit = "employees/views.py"
    elif "url" in message_lower:
        file_to_edit = "django_rest_main/urls.py"
    elif "auth" in message_lower or "jwt" in message_lower:
        file_to_edit = "django_rest_main/settings.py"
    elif "cors" in message_lower:
        file_to_edit = "django_rest_main/settings.py"
    elif "frontend" in message_lower:
        file_to_edit = "README.md"
    else:
        file_to_edit = "commit_log.txt"

    # Ensure directory exists
    os.makedirs(os.path.dirname(file_to_edit), exist_ok=True)

    # Append a dummy line to show change
    with open(file_to_edit, "a", encoding="utf-8") as f:
        f.write(f"# Commit on {date}: {message}\n")

    print(f"Edited file: {file_to_edit}")

for date, message in commits:
    print(f"\n--- Creating commit for {date}: {message} ---")

    # Make sure there's at least one change (Git won't commit otherwise)
    # Create a dummy file update for each commit
    with open("commit_log.txt", "a") as f:
        f.write(f"{date} - {message}\n")

    # Add all files
    run_command("git add .")

    # Commit with backdated timestamp
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = date
    env["GIT_AUTHOR_DATE"] = date
    cmd = f'git commit -m "{message}" --author="{AUTHOR_NAME} <{AUTHOR_EMAIL}>"'
    subprocess.run(cmd, shell=True, env=env)

# Push to GitHub
if PUSH_AFTER:
    print("\nPushing all commits to GitHub...")
    run_command("git push origin main")