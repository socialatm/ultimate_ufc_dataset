import pandas as pd
import numpy as np

# load ufc-master into a dataframe
ufc_master = pd.read_csv('ufc-master.csv', usecols=['RedFighter', 'BlueFighter', "RedOdds", "BlueOdds", 'Date', 'Location'])
# ufc_master = pd.read_csv('ufc-master.csv')
print(ufc_master.head(25))
ufc_master.info()

column_names = ufc_master.columns.tolist()
print(column_names)

print(ufc_master.shape)

# print the length of ufc_master['red_odds']
print(len(ufc_master['RedOdds']))

# find rows where Location = Las Vegas, Nevada, USA and Date = 2024-01-13
rows = ufc_master[(ufc_master['Location'] == 'Las Vegas, Nevada, USA') & (ufc_master['Date'] == '2024-01-13')]
print(rows)







