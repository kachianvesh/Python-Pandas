import pandas as pd
import numpy as np
x=pd.DataFrame({'project1':[20,30,10,50,30],
                'project2':[30,63,52,20,10],
                'project3':[10,20,32,9,63],
                'project4':[10,30,50,40,2]},index=np.arange(601,606))
y=pd.DataFrame({'project1':[21,30,10,50,30],
                'project2':[3,63,52,20,10],
                'project3':[101,20,12,9,63],
                'project4':[10,11,20,40,2]},index=np.arange(606,611))
z=pd.DataFrame({'project1':[10,30,10,51,20],
                'project2':[10,63,42,20,10],
                'project3':[10,20,32,9,63],
                'project4':[10,34,50,40,112]},index=np.arange(611,616))
a=pd.concat([x,y,z])
print(a)