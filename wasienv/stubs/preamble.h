#include <unistd.h>
#include <sys/types.h>
#include <limits.h>
#include <stdlib.h>
#include <stdarg.h>

#define __wasilibc_unmodified_upstream 1
#include <stdlib.h>
#undef __wasilibc_unmodified_upstream

char *realpath(const char *path, char *resolved_path);
uid_t getuid(void);
int getpagesize(void);

__attribute__((unused)) static uid_t getuid(void) { return 0; }
__attribute__((unused)) static char *realpath(const char *path, char *resolved_path) { return 0; }


///
#define PAGESIZE (0x10000)
#define PAGE_SIZE PAGESIZE
#define	_PATH_TMP	"/tmp/"

__attribute__((unused)) static int getpagesize(void) { return PAGE_SIZE; }

__attribute__((unused)) static int mprotect(void *addr, size_t len, int prot) { return 0; }

__attribute__((unused)) static int sysctlbyname(const char *name, void *oldp,	size_t *oldlenp, const void *newp, size_t newlen) { return 0; }

__attribute__((unused)) static pid_t getpid(void) { return 0; }

__attribute__((unused)) static uid_t geteuid(void) { return 0; }

__attribute__((unused)) static gid_t getgid(void) { return 0; }

__attribute__((unused)) static gid_t getegid(void) { return 0; }

__attribute__((unused)) static int chmod(const char *pathname, mode_t mode) { return 0; }

__attribute__((unused)) static int signal(int signum, int handler) { return 0; }

__attribute__((unused)) static int sigaction(int signum, const struct sigaction *act,
                     struct sigaction *oldact) { return 0; }



__attribute__((unused)) static void warn(const char * a1, ...) {}
__attribute__((unused)) static void vwarn(const char *a1, va_list a2) {}
__attribute__((unused)) static void warnx(const char *a1, ...) {}
__attribute__((unused)) static void vwarnx(const char *a1, va_list a2) {}

__attribute__((unused)) static  _Noreturn void err(int a1, const char *a2, ...) {}
__attribute__((unused)) static  _Noreturn void verr(int a1, const char *a2, va_list a3) {}
__attribute__((unused)) static _Noreturn void errx(int a1, const char *a2, ...) {}
__attribute__((unused)) static  _Noreturn void verrx(int a1, const char *a2, va_list a3) {}

__attribute__((unused)) static  int dup(int fd) {return -1;}
