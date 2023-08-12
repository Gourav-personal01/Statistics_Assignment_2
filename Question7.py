# Q7. For the two given sets A = (2,3,4,5,6,7) & B = (0,2,6,8,10). Find:

# (i) 	A Intersection B

# (ii)	A ⋃ B

# Answer - 
import numpy as np
A = (2,3,4,5,6,7) 
B = (0,2,6,8,10)

# Intersection//
print(np.intersect1d(A,B))

# Union//
print(np.union1d(A,B))