import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
#s = pd.Series(data)
#If index is passed, the values in data corresponding 
#to the labels in the index will be pulled out.
s = pd.Series(data,index=['b','c','d','a'])
print (s)

