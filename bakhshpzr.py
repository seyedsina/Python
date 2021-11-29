#!/usr/bin/python
import numpy as np
import sys
sys.argv
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])
c=np.arange(x, y+1, 1)
print(np.sum(c%z==0))
