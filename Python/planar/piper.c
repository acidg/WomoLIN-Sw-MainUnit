#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

static volatile int keepRunning = 1;

void intHandler(int dummy) {
    keepRunning = 0;
}

int main2(void)
{
  int c;
  int i=0;
  setbuf(stdout, NULL);

  signal(SIGINT, intHandler);

  while(keepRunning){
    c=getchar();
    if((i=!i)!=0)
      printf("%c",c);
  }
  exit(0);
}

int main(void)
{
  int c;
  int i=0;
  setbuf(stdout, NULL);

  while((c=getchar()) != EOF) {
    if((i=!i)!=0)
      printf("%c",c);
  }
  exit(0);
}
