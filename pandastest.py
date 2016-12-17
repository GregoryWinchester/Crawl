from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import os, sys
import matplotlib

#%matplotlib inline
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names,births))

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
df.to_csv('births1880.csv', index=False, header=False)

csvPath = sys.path[0] + r'\births1880.csv'

df = pd.read_csv(csvPath, names=['Names','Births'])

os.remove(csvPath)

print(df.Births.dtype)
