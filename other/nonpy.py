import matplotlib.pyplot as plt
import random

def DicePlot(n, cast):
  x = [i+1 for i in range(n)]
  y = [0]*n
  for i in range(cast):
    d = random.randrange(n)
    y[d] += 1
  plt.bar(x, y)  #
  plt.show()

DicePlot(6, 5000)