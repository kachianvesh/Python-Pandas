import numpy as np
import pandas as pd
li=[["shiva", 23,24,22,22,26, "IV"],
    ["Mahadev",30,12,20,33,65,"II"],
    ["Eeshwar",30,29,27,28,24,"I"],
    ["Hara",28,28,28,27,22,"I"],
    ["Rudra",12,13,11,10,15,"XX"],
    ["Nethra",25,26,23,22,20,"VI"]]
x=pd.DataFrame(li, 
               index=[np.arange(1201,1207)],                
               columns=["Name","s1","s2",'s3','s4','s5','Rank'])
print('------------Display the complete data frame-------------')
print(x)

#Selecting required columns
print('-----------Selecting required columns------------')
print(x[['Name','Rank','s3']])
#Adding new columns
print('-----------Adding new columns------------')
x['credits']=np.arange(5,17,2)
#Adding new coloumn by taking reference of other columns
x['ToT']=(x['s1']+x['s2']+x['s3']+x['s4']+x['s5'])
print(x)
#Deleting  dataframe
print("-----------Deleting a dataframe-----------")
del x['credits']   #you can also use x.pop['credits']
print(x)
print("-----------Deleting multiple cols in a dataframe-----------")
x=x.drop(x.columns[[2,3,4]],axis=1)
print(x)