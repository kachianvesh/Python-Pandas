import pandas as pd
import numpy as np
from sklearn import preprocessing
x=pd.read_csv("C:/Users/sony/seaborn-data/iris.csv")
print(x)
'''
#lets apply mean to the iris dataset
print(np.mean(x,axis=0))

#lets do the preprocessing on standardized data
data_standardized=preprocessing.scale(x)
print ("\nMean = ", data_standardized.mean(axis = 0))
print ("Std deviation = ", data_standardized.std(axis = 0))

'''