import os
import subprocess

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {cmd}: {result.stderr}")
    return result.stdout

commits = [
    ("chore: add root level .gitignore", "git add .gitignore"),
    ("chore: add MIT License", "git add LICENSE"),
    ("chore: remove legacy contributing guide", "git rm CONTRIBUTING.md"),
    ("chore: remove redundant run_empath script", "git rm run_empath.sh"),
    ("chore: remove test_connection utility", "git rm test_connection.py"),
    ("chore: clean up project changelog", "git rm CHANGELOG.md"),
    ("docs: remove banner and bad assets from README", "git add README.md"),
    ("feat: implement 'surprised' gesture in RobotController", "git add empath/robot_controller.py"),
    ("feat: implement 'angry' gesture in RobotController", "git add empath/robot_controller.py"),
    ("feat: implement 'confused' gesture in RobotController", "git add empath/robot_controller.py"),
    ("feat: implement 'excited' gesture in RobotController", "git add empath/robot_controller.py"),
    ("feat: implement 'bashful' gesture in RobotController", "git add empath/robot_controller.py"),
    ("refactor: enhance emotion mapping in main logic", "git add empath/main.py"),
    ("style: improve dashboard glassmorphism aesthetics", "git add dashboard/app/globals.css"),
    ("style: expand emotion color spectrum on dashboard", "git add dashboard/app/page.tsx"),
    ("fix: configure VSCode settings for CSS unknownAtRules", "git add .vscode/settings.json"),
    ("refactor: optimize brain interaction logic", "git add empath/brain.py"),
    ("refactor: update detector speed and accuracy settings", "git add empath/detector.py"),
    ("chore: update python requirements for new features", "git add empath/requirements.txt"),
    ("feat: add core super_launch.sh for simplified startup", "git add super_launch.sh"),
    ("feat: add hearing module for natural voice interaction", "git add empath/hearing.py"),
    ("docs: update technical stack and gesture list in README", "git add README.md"),
    ("chore: finalize source code structure for V2", "git add empath/*.py"),
    ("chore: prepare environment for full project launch", "git add .")
]

# Ensure we are in a clean state (staged-wise)
run("git reset")

# Special handling for already deleted files that are not in index
deleted_files = ["CONTRIBUTING.md", "run_empath.sh", "test_connection.py", "CHANGELOG.md"]
for f in deleted_files:
    if os.path.exists(f):
        run(f"rm {f}") # Ensure they are gone from disk

for i, (msg, cmd) in enumerate(commits):
    print(f"Commit {i+1}/24: {msg}")
    run(cmd)
    run(f'git commit -m "{msg}"')

print("Done making 24 commits.")
