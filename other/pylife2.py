import os
import time

def printA(a, n):
	for i in range(1, n+1):
		for j in range(1, n+1):
			if a[i][j]==0: print(" .", end="")
			else: print(" ■", end="")
		print()

now = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
	   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
	   [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
	   [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



def life2(a, n):
  print(">> Origin")
  printA(a, len(a)-2)
  next =[[0]*(len(a)) for i in range(len(a))]
  for k in range(n):
    for i in range(1, len(a)-1):
      for j in range(1, len(a)-1):
        around = sum(a[i-1][j-1:j+2])+sum(a[i][j-1:j+2])+sum(a[i+1][j-1:j+2])
        if (around == 3) or (around-a[i][j] == 3): next[i][j] = 1
        else: next[i][j] = 0
    time.sleep(1)
    clear = lambda: os.system('clear')
    clear()
    print(">> After %d" %(k+1))
    printA(next, len(next)-2)
    a = next

life2(now, 100)
