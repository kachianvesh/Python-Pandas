import numpy as np
import pandas as pd
a = pd.DataFrame({'Course': ['btech', 'mtech', 'mba', 'R&D'], 
                    'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3']}) 
  
b = pd.DataFrame({'Course': ['btech', 'mtech', 'mba', 'R&D'], 
                      'C': ['C0', 'C1', 'C2', 'C3'], 
                      'D': ['D0', 'D1', 'D2', 'D3']}) 
x=pd.merge(a,b)
print(x)