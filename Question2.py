# Q2. What is the difference between the mean, median, and mode? How are they used to measure the
# central tendency of a dataset?

import numpy as np

# 1. Mean is used to calculate the Average of a Data Set.
# Example - 

age = [23,33,45,66,77,38]

# We Can easily calculate the Central tendency by mean by using np.mean() function.
print(np.mean(age)) 

# 2. Meadian is used to calculate the Average of a Dataset which have outliers. 
age = [23,33,45,66,77,38,250]

# We Can easily calculate the Central tendency by median by using np.median() function.
print(np.median(age))

# 3. Mode is used to calculate the Frequency of data (Occurance in dataset)
age = [23,33,45,23,66,77,38,250]

# We Can easily calculate the Central tendency by Mode by using stats.mode() function.
from scipy import stats
mode = stats.mode(age)
print(mode)