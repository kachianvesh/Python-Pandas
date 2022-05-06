import numpy as np
import pandas as pd
a = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                  'B': ['B0', 'B1', 'B2', 'B3']}, index=np.arange(1201,1205)) 
  
b = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'], 
                  'D': ['D0', 'D1', 'D2', 'D3']}, index=np.arange(1201,1205)) 
x=a.join(b)

c = pd.DataFrame({'E': ['E0', 'E1', 'E2', 'E3'], 
                  'F': ['F0', 'F1', 'F2', 'F3']}, index=np.arange(1201,1205)) 
x2=x.join(c)
print(x2)