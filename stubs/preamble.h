#include <unistd.h>
#include <sys/types.h>
#include <limits.h>
#include <stdlib.h>

// #define __wasilibc_unmodified_upstream 1

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

