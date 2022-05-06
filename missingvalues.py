import pandas as pd
import numpy as np
x=pd.DataFrame([[1,2,3,4],[1,3]],columns=['a','b','c','d'])
print(x)
print(pd.isna(x))
#Count the number of null values
print('---------Count the null values--------')
print(x.isnull().sum())
#Fill the empty values with some value
print('--------Fill the null value with 6--------')
print(x.fillna(6)) 

#Another dataset values
print(".........Lets see the faculty information...........")
y=pd.read_csv("C:/Users/sony/Desktop/python/PYTHON PROGS/Progs in spyder/pandas progs/faculty_info.csv")
print(y)
print(".....Show the null valued cols.....")
print(y.isnull())
print(".....Count the no. of null values.....")
print(y.isna().sum())

#Lets fill the null valued rowws

print(y.fillna(y.mean()))
#Lets drop the null valued rows
print("-----Lets drop the null valued rows from the dataset-----")
#print(y.dropna())
