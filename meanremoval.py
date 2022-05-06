import pandas as pd
import numpy as np
from sklearn import preprocessing
x=np.array([[1,2,3,4],[11,22,33,36],[45,52,23,36]])
print(x)
print('-----Lets apply mean removal-----')
data_standardized = preprocessing.scale(x)
print ("\nMean = ", data_standardized.mean(axis = 0))
print ("Std deviation = ", data_standardized.std(axis = 0))
#Note: Observe that in the output, mean is almost 0 and the standard deviation is 1