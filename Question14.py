# Q14. How do outliers affect measures of central tendency and dispersion? Provide an example

# Outliers really affects the Central Tendency as the Outlier is something which is more far then the other digits in a variable.
# We can easily Handle the Outliers by using the Median 

import numpy as np 
data = [1,2,3,4,5,6]

print(np.mean(data)) # O/P - 3.5 

data = [1,2,3,4,5,6,190] # data with Outliers

print(np.mean(data)) # O/P - 30.14 

# as we can see that the outliers in dataset is impacting the mean 

print(np.median(data)) # O/P - 4.0