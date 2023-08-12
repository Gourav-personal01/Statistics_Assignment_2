# Q10. Explain the difference between covariance and correlation. How are these measures used in
# statistical analysis?

# Answer - 

# Covariance is used to find the relationship of one variable to another and Correlation is used to find the relationship between the two variables.

# Answer - 
import pandas as pd

data = [[10,12,13],[34,23,45],[32,34,21]]

df = pd.DataFrame(data,columns=["A","B","C"])

# Covarriance//
print(df.cov())

# Pearson Correlation Coefficient 
print(df.corr(method='pearson'))

