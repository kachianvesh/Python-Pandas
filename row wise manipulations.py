import numpy as np
import pandas as pd
li=[["shiva", 23,24,22,22,26, "IV"],
    ["Mahadev",30,12,20,33,65,"II"],
    ["Eeshwar",30,29,27,28,24,"I"],
    ["Hara",28,28,28,27,22,"I"],
    ["Rudra",12,13,11,10,15,"XX"],
    ["Nethra",25,26,23,22,20,"VI"]]
x=pd.DataFrame(li,               
               columns=["Name","s1","s2",'s3','s4','s5','Rank'])
print('\n----Display the complete data table-------------')
print(x)
#Selecting the rows by using label
print('----seleting the rows using its label--------')
print(x.loc[[3]])
#Selection by integer location
print("\n----Selecting the rows by integer location---------")
print(x.iloc[[1,4,3]])
#We can slice the required rows by using : operator
print("\n----Slicing the required rows-------")
print(x[1:4])

#Adding of rows
print('\n----Adding rows to the existing dataframe------')
x.loc[6]=["Kashi", 15,16,19,23,25,"X"]
#x.index=x.index+1
#x=x.sort_index()
print(x)
#dataframe.append() we can pass a dictionary of key value pairS
print("\n----Adding row using dictionary key and values-----")
y=x.append({"Name":"om", "s2":6,'s5':23,"Rank":"NIL"},ignore_index="False")
print(y)
#Adding multiple rows at a time
print("\n----Adding multiple rows in the dataframe.----")
los=[pd.Series(["Jaitra",25,26,23,22,20,"VI"], index=x.columns),
     pd.Series(["Shubam",25,26,13,20,10,"VIII"], index=x.columns),
     pd.Series(["Anvesh", 25,25,25,25,25,'I'], index=x.columns)]
z=x.append(los, ignore_index='True')
print(z)

#Deleting the rows
print("\n----Deleting the row in dataframe-------")
x=x.drop(2)
print(x)

