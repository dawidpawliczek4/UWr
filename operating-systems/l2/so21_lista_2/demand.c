#include "csapp.h"

/* First address of handled region. */
#define ADDR_START ((void *)0x10000000)
/* Last address of handled region (not inclusive). */
#define ADDR_END ((void *)0x10010000)

static size_t pagesize;

/* Maps anonymouse page with `prot` access permissions at `addr` address. */
static void mmap_page(void *addr, int prot) {
  Mmap(addr, pagesize, prot, MAP_ANONYMOUS | MAP_PRIVATE | MAP_FIXED, -1, 0);
}

/* Changes protection bits to `prot` for page at `addr` address. */
static void mprotect_page(void *addr, int prot) {
  Mprotect(addr, pagesize, prot);
}

static inline void raise_signum_ignore_handler(int signum) {
  struct sigaction act = {0};
  act.sa_handler = SIG_IGN;
  sigemptyset(&act.sa_mask);
  sigaction(signum, &act, NULL);
  raise(signum);
  _exit(128 + signum);
}

static void sigsegv_handler(int signum, siginfo_t *info, void *data) {
  ucontext_t *uc = data;
  intptr_t rip;

  /* TODO: You need to get value of instruction pointer register from `uc`.
   * Print all useful data from `info` and quit in such a way that a shell
   * reports program has been terminated with SIGSEGV. */
  rip = (intptr_t)uc->uc_mcontext.gregs[REG_RIP];
  void* fault_addr = info->si_addr;

  uintptr_t a = (uintptr_t)fault_addr;
  uintptr_t page_base = a - (a % pagesize);
  void* page = (void*)page_base;

  safe_printf("Fault at rip=%p accessing %p!", (void*)rip, fault_addr);

  if (fault_addr < ADDR_START || fault_addr >= ADDR_END) {
    safe_printf(" Address not mapped - terminating!\n");
    raise_signum_ignore_handler(signum);
  }

  if (info->si_code == SEGV_MAPERR) {
    safe_printf(" Map missing page at %p.\n", fault_addr);
    mmap_page(page, PROT_READ);
    return;
  } else if (info->si_code == SEGV_ACCERR) {
    safe_printf(" Make page at %p writable.\n", fault_addr);
    mprotect_page(page, PROT_READ | PROT_WRITE);
    return;
  } else {
    safe_printf(" Unknown si_code=%d - terminating!\n", info->si_code);
    raise_signum_ignore_handler(signum);
  }


}

int main(int argc, char **argv) {
  pagesize = sysconf(_SC_PAGESIZE);

  /* Register signal handler for SIGSEGV */
  struct sigaction action = {.sa_sigaction = sigsegv_handler,
                             .sa_flags = SA_SIGINFO};
  sigaction(SIGSEGV, &action, NULL);

  /* Initially all pages in the range are either not mapped or readonly! */
  for (void *addr = ADDR_START; addr < ADDR_END; addr += pagesize)
    if (random() % 2)
      mmap_page(addr, PROT_READ);

  /* Generate lots of writes to the region. */
  volatile long *array = ADDR_START;
  long nelems = (ADDR_END - ADDR_START) / sizeof(long);

  for (long i = 0; i < nelems * 2; i++) {
    long index = random() % nelems;
    array[index] = (long)&array[index];
  }

  /* Perform off by one access - triggering a real fault! */
  array[nelems] = 0xDEADC0DE;

  return EXIT_SUCCESS;
}



// static void sigsegv_handler(int signum, siginfo_t *info, void *data) {
//   ucontext_t *uc = (ucontext_t *)data;
//   /* RIP (instruction pointer) — na x86_64 w gregs[REG_RIP] */
//   intptr_t rip = (intptr_t)uc->uc_mcontext.gregs[REG_RIP];

//   void *fault_addr = info->si_addr;
//   /* align fault address down to page boundary */
//   uintptr_t page_base = (uintptr_t)fault_addr & ~(pagesize - 1);
//   void *page = (void *)page_base;

//   /* Print basic diagnostic info */
//   safe_printf("Fault at rip=%p accessing %p! ", (void *)rip, fault_addr);

//   /* If address is outside handled region -> terminate as if killed by SIGSEGV */
//   if (fault_addr < ADDR_START || fault_addr >= ADDR_END) {
//     safe_printf("Address not mapped - terminating!\n");
//     /* restore default handler and re-raise the signal so process is killed
//        with the original signal (so shell reports e.g. "Segmentation fault") */
//     struct sigaction act = {0};
//     act.sa_handler = SIG_DFL;
//     sigemptyset(&act.sa_mask);
//     sigaction(SIGSEGV, &act, NULL);
//     /* re-raise the same signal */
//     raise(signum);
//     /* if raise returns, ensure _exit */
//     _exit(128 + signum);
//   }

//   /* Handle particular si_code values */
//   if (info->si_code == SEGV_MAPERR) {
//     /* missing mapping: map the page (map it read-only so later write triggers ACCERR) */
//     safe_printf("Map missing page at %p.\n", page);
//     mmap_page(page, PROT_READ);
//     return;
//   } else if (info->si_code == SEGV_ACCERR) {
//     /* access error (e.g., write to read-only): make page writable */
//     safe_printf("Make page at %p writable.\n", page);
//     mprotect_page(page, PROT_READ | PROT_WRITE);
//     return;
//   } else {
//     /* unknown code — be conservative and terminate as if killed */
//     safe_printf("Unknown si_code=%d - terminating!\n", info->si_code);
//     struct sigaction act = {0};
//     act.sa_handler = SIG_DFL;
//     sigemptyset(&act.sa_mask);
//     sigaction(SIGSEGV, &act, NULL);
//     raise(signum);
//     _exit(128 + signum);
//   }
// }
