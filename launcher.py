import subprocess
import os
import time

bots = [
    ("Stree", "https://github.com/Sinchu-XD/Stree", "python3 Main.py"),
    ("Paglu", "https://github.com/Sinchu-XD/Paglu", "python3 Main.py"),
    ("Posting", "https://github.com/Sinchu-XD/Posting", "python3 Posting.py"),
]

processes = []

def prepare_repo(name, repo):
    if not os.path.isdir(name):
        print(f"📥 Cloning {name}")
        subprocess.run(f"git clone {repo} {name}", shell=True)
    else:
        print(f"🔄 Updating {name}")
        subprocess.run("git pull", shell=True, cwd=name)

for name, repo, cmd in bots:
    prepare_repo(name, repo)

    print(f"🚀 Starting {name}")
    p = subprocess.Popen(cmd, shell=True, cwd=name)
    processes.append((name, repo, cmd, p))


while True:
    for i, (name, repo, cmd, p) in enumerate(processes):
        if p.poll() is not None:
            print(f"❌ {name} crashed → restarting")
            p = subprocess.Popen(cmd, shell=True, cwd=name)
            processes[i] = (name, repo, cmd, p)

    time.sleep(5)
    
