# Q3. Measure the three measures of central tendency for the given height data:

#  [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]

# Answer - 
import numpy as np
data = [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]

# Mean//
mean = np.mean(data)
print(mean)

# Median//
median = np.median(data)
print(median)

# Mode//
from scipy import stats
mode = stats.mode(data)
print(mode) 
