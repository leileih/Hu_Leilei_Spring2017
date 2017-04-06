
# coding: utf-8

# # Question 1 Part 1
# - Use ‘vehicle_collisions’ data set
# - For each month in 2016, find out the percentage of collisions in Manhattan out of that year's total accidents in New York City
# - Display a few rows of the output use df.head()
# - Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

import pandas as pd

df = pd.read_csv('Data/vehicle_collisions.csv')
df = df[df.apply(lambda x: x['DATE'].split('/')[2] == '16', axis=1)]

total_count = df['DATE'].apply(lambda x: x.split('/')[0]).value_counts()
df_manhattan = df[df.apply(lambda x: x['BOROUGH'] == 'MANHATTAN', axis=1)]
manhattan_count = df_manhattan['DATE'].apply(lambda x: x.split('/')[0]).value_counts()

output = pd.concat([manhattan_count, total_count], axis=1)

output.columns = ['MANHATTAN', 'NYC']
output.columns.name = 'MONTH'
output.index = output.index.map(int)
output.sort_index(inplace=True)
#output.head(3)
output = output.append(output.sum(numeric_only=True), ignore_index=True)
#output
output['PERCENTAGE'] = output['MANHATTAN']/output['NYC']
output = output.rename(index={0: 'Jan', 1: 'Feb', 2: 'Mar', 3: 'Apr', 4: 'May', 5: 'Jun', 6: 'Jul', 7: 'Aug', 8: 'Sep', 9: 'Oct', 10: 'Nov', 11: 'Dec', 12: 'Total'})
#output.head(3)

print(output.head(3))
output.to_csv('Ass3_output/Q1_P1_output.csv',index=True,header=True,index_label='MONTH')
