"""
Start a bash process, but with fork and exec.

This is what `subprocess.popen` eventually uses.
"""
import os

print("Starting bash process...")

# This makes a copy of the current process....
ret = os.fork()

if ret == 0:
    # `os.fork` returns 0 if we're now executing in the child
    # execve will replace entire current execution with new program given.
    # First argument is full path to the program to execute, second is the list
    # of arguments that are passed to the equivalent of `sys.argv`. First element
    # of the list of arguments should almost always be the path to your executable.
    os.execv('/bin/bash', ['/bin/bash'])
    # This line will never be executed!
else:
    # os.fork returns the pid of the child process if we're executing
    # in the parent
    # Wait for the child process to complete
    os.waitpid(ret, 0)
    print("Bash process completed")