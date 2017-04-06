
# coding: utf-8

# # Question 1 Part 2
# - Use ‘vehicle_collisions’ data set
# - For each borough, find out distribution of each collision scale. (One carinvolved? Two? Three? or more?) (From 2015 to present)
# - Display a few rows of the output use df.head()
# - Generate a csv output with five columns ('borough', 'one-vehicle', 'two- vehicles', 'three-vehicles', 'more-vehicles')

import pandas as pd

df = pd.read_csv('Data/vehicle_collisions.csv')
cols = ['BOROUGH', 'VEHICLE 1 TYPE', 'VEHICLE 2 TYPE', 'VEHICLE 3 TYPE', 'VEHICLE 4 TYPE']
df = df[cols]
#df.head(3)

df['VEHICLES_COUNT'] = df.count(axis=1) - 1 
#df.head(3)

# select columns needed
cols = ['BOROUGH', 'VEHICLES_COUNT']
df = df[cols]
#df.head(3)

df = df[pd.notnull(df['BOROUGH'])]
#df.head(3)

df = df[df['VEHICLES_COUNT'] != 0]
#df.head(3)

df['VEHICLES_COUNT'] = df['VEHICLES_COUNT'].apply(lambda x : str(x) if x < 4 else 'more than 3')
#df.head(4)

df = df.groupby(['BOROUGH', 'VEHICLES_COUNT'], as_index=False).size().reset_index()
df = df.rename(columns = {0:'COUNT'})
#df.head(4)

df = df.pivot(index='BOROUGH', columns='VEHICLES_COUNT', values= 'COUNT')
df.columns = ['ONE_VEHICLE_INVOLVED', 'TWO_VEHICLE_INVOLVED', 'THREE_VEHICLE_INVOLVED', 'MORE_VEHICLE_INVOLVED']
df = df.reset_index()
#df.head(3)

print(df.head(3))
df.to_csv('Ass3_output/Q1_P2_output.csv',index=False,header=True)
