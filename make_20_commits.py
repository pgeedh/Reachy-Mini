import os
import subprocess

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

commits = [
    ("chore: remove dashboard and local web hosting frontend", "git rm -rf dashboard/"),
    ("chore: add high-fidelity T-Rex mesh assets", "git add venv/lib/python3.11/site-packages/reachy_mini/descriptions/reachy_mini/mjcf/assets/trex_toy_1k.blend/"),
    ("feat: integrate OBJ T-Rex mesh into MuJoCo scene", "git add venv/lib/python3.11/site-packages/reachy_mini/descriptions/reachy_mini/mjcf/scenes/minimal.xml"),
    ("feat: remove monitor screen from simulation environment", "git add venv/lib/python3.11/site-packages/reachy_mini/descriptions/reachy_mini/mjcf/scenes/minimal.xml"),
    ("feat: anchor all simulation objects to the table surface", "git add venv/lib/python3.11/site-packages/reachy_mini/descriptions/reachy_mini/mjcf/scenes/minimal.xml"),
    ("feat: implement NVIDIA NIM model as failover for Gemini API", "git add empath/brain.py"),
    ("feat: add persona-aware system instructions for fallback model", "git add empath/brain.py"),
    ("feat: implement wake word activation for Reachy/Jarvis/Tadashi", "git add empath/main.py"),
    ("feat: add 'thoughtful tilt' expression to robot controller", "git add empath/robot_controller.py"),
    ("feat: add 'giggles and shimmy' expression for playful interactions", "git add empath/robot_controller.py"),
    ("feat: add 'agreement nod' expression to robot controller", "git add empath/robot_controller.py"),
    ("feat: add 'embarrassed peek' expression for shy moments", "git add empath/robot_controller.py"),
    ("refactor: enhance interaction loop with expressive responses", "git add empath/main.py"),
    ("fix: optimize MuJoCo backend by removing monitor logic", "git add venv/lib/python3.11/site-packages/reachy_mini/daemon/backend/mujoco/backend.py"),
    ("chore: update super-launch script for dashboard-less operation", "git add super_launch.sh"),
    ("docs: update README with new wake words and features", "git add README.md"),
    ("chore: clean up temporary asset files and unzipped models", "git rm -rf trex_assets/"),
    ("style: expand emotion mapping with sub-gestures", "git add empath/main.py"),
    ("chore: finalize PersonaPlex integration in brain logic", "git add empath/brain.py"),
    ("chore: sync repository state with new feature baseline", "git add .")
]

# Reset index
run("git reset")

for i, (msg, cmd) in enumerate(commits):
    print(f"Commit {i+1}/20: {msg}")
    run(cmd)
    run(f'git commit -m "{msg}"')

# Sync/Push (User asked to sync and push)
print("Syncing with origin...")
run("git push origin main")
print("Done!")
