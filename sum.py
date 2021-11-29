#!/usr/bin/python
import sys
import numpy as np
sys.argv
x=int(sys.argv[1])
y=int(sys.argv[2])
a=np.arange(x,y+1,1)
print(np.sum(a))
