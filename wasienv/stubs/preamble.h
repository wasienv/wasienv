#include <unistd.h>
#include <sys/types.h>
#include <limits.h>
#include <stdlib.h>

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

__attribute__((weak)) int getpagesize(void) { return PAGE_SIZE; }

__attribute__((weak)) int mprotect(void *addr, size_t len, int prot) { return 0; }

__attribute__((weak)) int sysctlbyname(const char *name, void *oldp,	size_t *oldlenp, const void *newp, size_t newlen) { return 0; }

__attribute__((weak)) pid_t getpid(void) { return 0; }

__attribute__((weak)) uid_t geteuid(void) { return 0; }

__attribute__((weak)) gid_t getgid(void) { return 0; }

__attribute__((weak)) gid_t getegid(void) { return 0; }

__attribute__((weak)) int chmod(const char *pathname, mode_t mode) { return 0; }

__attribute__((weak)) int signal(int signum, int handler) { return 0; }

__attribute__((weak)) int sigaction(int signum, const struct sigaction *act,
                     struct sigaction *oldact) { return 0; }

