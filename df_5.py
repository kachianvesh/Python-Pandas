import pandas as pd
'''data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)'''
dic=[{'s1':97, 's2':99, 's3':78, 's4':77},
   {'s1':78, 's2':85,'s3':69},
   {'s3':55,'s3':78,'s4':84},
   {'s3':99, 's4':93,'s1':100}]
x=pd.DataFrame(dic, index=['Ram', 'Rahim', 'Robert', 'shiva'])
print(x)