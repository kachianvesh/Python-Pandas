#Retrieve the required rows using series
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

print("retrieve the first three element")
print (s[:3])
print("retrieve the last three elements")
print(s[-3:])