import os
import subprocess
from datetime import datetime

BLOG_REPO = r"C:\Projects\multi-agent-blog"

def push_blog_update(commit_msg: str = None):
    if not os.path.isdir(BLOG_REPO):
        raise FileNotFoundError(f"Blog repo not found at: {BLOG_REPO}")

    os.chdir(BLOG_REPO)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = commit_msg or f"🔄 Update blog: {timestamp}"

    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", commit_msg],
        ["git", "push", "origin", "main"]
    ]

    for cmd in commands:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"$ {' '.join(cmd)}")
        print(result.stdout)
        if result.returncode != 0:
            print("⚠️ Error:", result.stderr)
            break
    else:
        print("✅ Blog pushed successfully!")

