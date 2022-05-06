import pandas as pd
x=pd.read_csv('emp_dataset.csv')
print(x.shape)
#Listing the entire dataset
print("-----listing the entire dataset-----")
print(x)
#print(x.loc[:,['name','salary']])
print("-----printing the statistical summary of the dataset-----")
print(x.describe())
print("----breakdown data by class variable-----")
print(x.groupby("dept").size())