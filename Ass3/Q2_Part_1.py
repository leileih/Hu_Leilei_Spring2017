
# coding: utf-8

# # Question 2 Part 1
# - Use 'employee_compensation' data set
# - Find out the highest paid departments in each organization group by calculating mean of total compensation for every department
# - Output should contain the organization group and the departments in each organization group with the total compensation from highest to lowest value
# - Display a few rows of the output use df.head()
# - Generate a csv output
import pandas as pd

# select needed columns 
df = pd.read_csv('Data/employee_compensation.csv')
cols = ['Organization Group', 'Department', 'Total Compensation']
df = df[cols]
#df.head(3)

# calculate mean of total compensation for every department
output = df.groupby(['Organization Group','Department'],as_index=False).mean()
#output.head(3)

# sort the department of each organization by average total compensation
output = output.sort_values(['Organization Group','Total Compensation'], ascending = False)
#output.head(3)

print(output.head(3))
output.to_csv('Ass3_output/Q2_P1_output.csv',index=False,header=True)
