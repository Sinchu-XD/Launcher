import subprocess
import time

bots = [
    ("Stree", "python3 Main.py"),
    ("Paglu", "python3 Main.py"),
    ("Posting", "python3 Posting.py")
]

processes = []

for folder, cmd in bots:
    print(f"🚀 Starting {folder}")
    p = subprocess.Popen(cmd, shell=True, cwd=folder)
    processes.append((folder, p))

while True:
    for i, (folder, p) in enumerate(processes):
        if p.poll() is not None:
            print(f"❌ {folder} crashed → restarting")
            processes[i] = (
                folder,
                subprocess.Popen(bots[i][1], shell=True, cwd=folder)
            )
    time.sleep(5)
  
