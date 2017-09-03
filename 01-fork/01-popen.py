"""
Exec a bash process and wait for it to die
"""
import subprocess

print("Starting bash process...")
child = subprocess.Popen(['/bin/bash'])
child.wait()
print("Bash process exited!")