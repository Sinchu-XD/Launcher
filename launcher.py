import subprocess
import os
import time

GIT_TOKEN = os.getenv("GIT_TOKEN")

bots = [
    ("Stree", f"https://{GIT_TOKEN}@github.com/Sinchu-XD/Stree", "python3 Main.py"),
    ("Paglu", f"https://{GIT_TOKEN}@github.com/Sinchu-XD/Paglu", "python3 Main.py"),
    ("Posting", f"https://{GIT_TOKEN}@github.com/Sinchu-XD/Posting", "python3 Posting.py"),
]

processes = []

def prepare_repo(name, repo):
    if not os.path.isdir(name):
        print(f"📥 Cloning {name}")
        result = subprocess.run(f"git clone {repo} {name}", shell=True)
        if result.returncode != 0:
            print(f"❌ Failed to clone {name}")
            exit(1)
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
