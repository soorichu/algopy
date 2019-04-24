#include <stdio.h>

int count = 0;

void Hanoi(int n, char from, char to, char ext){
  if (n==1){
    count++;
    printf("%d %c -> %c\n", n, from, to);
  }
  else{
    Hanoi(n-1, from, ext, to);
    count++;
    printf("%d %c -> %c\n", n, from, to);
    Hanoi(n-1, ext, to, from);
  }
}


int main(void) {
  int hpan = 6;
  Hanoi(hpan, 'A', 'C', 'B');
  printf("%d개의 하노이 판은 %d번 옮겨야 함.\n", hpan, count);
  return 0;
}