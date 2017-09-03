"""
Start a bash process, but with fork and exec.

This is what `subprocess.popen` eventually uses.
"""
from fork_syscall import lib, ffi
import os

print("Starting bash process...")

# This makes a copy of the current process....
ret = lib.fork()

if ret == 0:
    # `fork` returns 0 if we're now executing in the child
    # execve will replace entire current execution with new program given.
    # First argument is full path to the program to execute, second is the list
    # of arguments that are passed to the equivalent of `sys.argv`. First element
    # of the list of arguments should almost always be the path to your executable.
    ret = lib.execv('/bin/bash'.encode('utf-8'), [ffi.new('char[]', '/bin/bash'.encode()), ffi.NULL])
    # If we are here, that means an error happened!
    if ret == -1:
        print(ffi.errno)
    # This line will never be executed!
else:
    # os.fork returns the pid of the child process if we're executing
    # in the parent
    # Wait for the child process to complete
    ret = lib.waitpid(ret, ffi.NULL, 0)
    print("Bash process completed")