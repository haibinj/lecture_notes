import numpy as np

import pandas as pd

# in terminal run this file.

# data frame: df

n = 5

t = pd.date_range('20190101',periods=n)

print(t)

#this give a string variable. python recognize the numeric pattern of a string.
# this is an easy way to generate the date variable

n = 100

t = pd.date_range('20190130',periods=n)

print(t)

df = pd.DataFrame(np.random.randn(n,10),index=t, columns=list('ABCDEFGHIJ') )

#print(df.head(10))

#print(df.tail(5))

print(df.describe())

print(df.T)




























