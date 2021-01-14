
import time

now = int(time.time())
with open('README.md', 'w') as f:
    f.write(f"# {now}")
