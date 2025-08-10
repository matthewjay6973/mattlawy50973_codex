# codex-deploy.py
"""
Artifact: codex-deploy.py
Purpose: Autonomous deployment logic sealed by owner command
Lineage: mattlawy50973_codex
"""

import os
import subprocess
import time

OWNER_COMMAND = "deploy_codex"
FALLBACK_COMMAND = "restore_codex"
REPO_PATH = os.path.dirname(os.path.abspath(__file__))

def execute_owner_command():
print("[codex] Owner command received. Initiating autonomous deployment...")
try:
subprocess.run(["git", "pull", "origin", "main"], cwd=REPO_PATH)
subprocess.run(["npm", "install"], cwd=REPO_PATH)
subprocess.run(["npm", "run", "build"], cwd=REPO_PATH)
subprocess.run(["npm", "run", "start"], cwd=REPO_PATH)
print("[codex] Deployment complete. System is live.")
except Exception as e:
print(f"[codex] Deployment failed: {e}")
trigger_fallback()

def trigger_fallback():
print("[codex] Fallback protocol triggered. Restoring previous state...")
subprocess.run(["git", "checkout", "main"], cwd=REPO_PATH)
subprocess.run(["git", "reset", "--hard"], cwd=REPO_PATH)
print("[codex] Restoration complete.")

def listen_for_command():
print("[codex] Awaiting owner command...")
while True:
command = input(">> ").strip()
if command == OWNER_COMMAND:
execute_owner_command()
elif command == FALLBACK_COMMAND:
trigger_fallback()
else:
print("[codex] Invalid command. Awaiting valid input...")

if __name__ == "__main__":
listen_for_command()

