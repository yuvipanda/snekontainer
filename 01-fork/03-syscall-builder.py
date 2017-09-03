"""
Do the same fork and execve example, but by calling libc function wrappers for syscalls directly!
"""
import cffi

ffibuilder = cffi.FFI()

ffibuilder.set_source(
    'fork_syscall',
    r"""
    #include <sys/types.h>
    #include <unistd.h>
    #include <sys/wait.h>
    """,
    libraries=[]
)

ffibuilder.cdef(r"""
typedef int pid_t;
pid_t fork(void);
int execv (const char *filename, char *const argv[]);
pid_t waitpid(pid_t pid, int *wstatus, int options);

""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)