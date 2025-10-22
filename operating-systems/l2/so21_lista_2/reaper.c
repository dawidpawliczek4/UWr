#include "csapp.h"

static pid_t spawn(void (*fn)(void)) {
  pid_t pid = Fork();
  if (pid == 0) {    
    fn();
    printf("(%d) I'm done!\n", getpid());
    exit(EXIT_SUCCESS);
  }
  return pid;
}

static void grandchild(void) {
  printf("(%d) Waiting for signal!\n", getpid());

  /* TODO: Something is missing here! */
  pause();

  printf("(%d) Got the signal!\n", getpid());
}

static void child(void) {
  pid_t pid;
  
  /* TODO: Spawn a child! */
  setpgid(0, 0);
  pid = spawn(grandchild);

  printf("(%d) Grandchild (%d) spawned!\n", getpid(), pid);
}


/* Runs command "ps -o pid,ppid,pgrp,stat,cmd" using execve(2). */
static void ps(void) {
  char *argv[] = {"/bin/ps", "-o", "pid,ppid,pgrp,stat,cmd", NULL};
  execve("/bin/ps", argv, NULL);
}

int main(void) {
  /* TODO: Make yourself a reaper. */
#ifdef LINUX
  Prctl(PR_SET_CHILD_SUBREAPER, 1);
#endif
  printf("(%d) I'm a reaper now!\n", getpid());

  pid_t pid, pgrp;
  int status;

  pid = spawn(child);

  waitpid(pid, &status, 0);
  printf("(%d) Child (%d) terminated!\n", getpid(), pid);

  spawn(ps);

  kill(-pid, SIGTERM);
  waitpid(-1, &status, 0);
  printf("(%d) Grandchild terminated and waited for!\n", getpid());


  spawn(ps);

  return EXIT_SUCCESS;
}
