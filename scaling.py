import pandas as pd
import numpy as np
from sklearn import preprocessing
x=np.array([[1,2,3,4],[11,22,33,36],[45,52,23,36]])
print(x)
print('-----Lets apply scaling-----')
data_scaler = preprocessing.MinMaxScaler(feature_range = (1,10))
data_scaled = data_scaler.fit_transform(x)
print ("\nMin max scaled data =\n ", data_scaled)
#Note: you can observe all the values have been scaled to given range