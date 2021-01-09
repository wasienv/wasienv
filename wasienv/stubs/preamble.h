#include <unistd.h>
#include <sys/types.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <utime.h>
#include <errno.h>
#include <stdio.h>


#define __wasilibc_unmodified_upstream 1
#include <stdlib.h>
#undef __wasilibc_unmodified_upstream

char *realpath(const char *path, char *resolved_path);
uid_t getuid(void);
int getpagesize(void);

__attribute__((weak)) uid_t getuid(void) { return 0; }
__attribute__((weak)) char *realpath(const char *path, char *resolved_path) { return 0; }


///
#define PAGESIZE (0x10000)
#define PAGE_SIZE PAGESIZE

#define ESHUTDOWN 0
#define GRND_NONBLOCK 0

#define F_DUPFD  0

#define SIG_ERR  ((void (*)(int))-1)
#define SIG_DFL  ((void (*)(int)) 0)
#define SIG_IGN  ((void (*)(int)) 1)

// Poll fulfill. Since there are no important polls
// we identify all Important as normals
#define POLLPRI POLLIN
#define EPOLLPRI EPOLLIN

__attribute__((weak)) ssize_t getrandom(void * buffer, size_t len, unsigned flags) {
    // if (len > 256) {
    //     errno = EIO;
    //     return -1;
    // }

    // int r = __wasi_random_get(buffer, len);

    // if (r != 0) {
    //     errno = r;
    //     return -1;
    // }

    return -1;
}


__attribute__((weak)) char *getcwd(char *buf, size_t size) { return "";}

__attribute__((weak))  int clock_settime(clockid_t clk_id, const struct timespec *tp) { return 0;}
__attribute__((weak)) int chdir(const char *path) { return 0;
}
__attribute__((weak)) int grantpt(int fd);

#include <fcntl.h>

__attribute__((weak)) int dup(int fd) { 
    return -1;
    // int nfd = fcntl(fd, F_DUPFD, 0);
    // return nfd;
}

#define BADEXIT -1

__attribute__((weak)) int
dup2(int fd1, int fd2)
{
    return -1;
	// if (fd1 != fd2) {
	// 	if (fcntl(fd1, F_GETFL) < 0)
	// 		return BADEXIT;
	// 	if (fcntl(fd2, F_GETFL) >= 0)
	// 		close(fd2);
	// 	if (fcntl(fd1, F_DUPFD, fd2) < 0)
	// 		return BADEXIT;
	// }
	// return fd2;
}

__attribute__((weak)) int raise(int sig);
__attribute__((weak)) mode_t umask(mode_t mask);

__attribute__((weak)) int utime(const char *filename, const struct utimbuf *times);

__attribute__((weak)) int getpagesize(void) { return PAGE_SIZE; }

__attribute__((weak)) int mprotect(void *addr, size_t len, int prot) { return 0; }

__attribute__((weak)) int sysctlbyname(const char *name, void *oldp,	size_t *oldlenp, const void *newp, size_t newlen) { return 0; }

__attribute__((weak)) pid_t getpid(void) { return 0; }

__attribute__((weak)) uid_t geteuid(void) { return 0; }

__attribute__((weak)) gid_t getgid(void) { return 0; }

__attribute__((weak)) gid_t getegid(void) { return 0; }

__attribute__((weak)) int chmod(const char *pathname, mode_t mode) { return 0; }

__attribute__((weak)) int signal(int signum, int handler) { return 0; }

__attribute__((weak)) int sigaction(int signum, const /* struct sigaction */ void *act,
                     /* struct sigaction */ void *oldact) { return 0; }



// #include <dlfcn.h>

__attribute__((weak)) void *dlopen(const char *filename, int flag) {
    printf("[WASIENV] dlopen\n");fflush(stdout);
    return NULL;
}

__attribute__((weak)) const char *dlerror(void) {
    printf("[WASIENV] dlerror\n");fflush(stdout);
    return "";
}

__attribute__((weak)) void *dlsym(void *handle, const char *symbol) {
    printf("[WASIENV] dlsym\n");fflush(stdout);
    return NULL;
}

__attribute__((weak)) int dlclose(void *handle) {
    printf("[WASIENV] dlclose\n");fflush(stdout);
    return 0;
}

