
# coding: utf-8

# # Question 2 Part 2
# - Use 'employee_compensation' data set
# - Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee
# - Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# - For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value
# - Display the top 5 Job Families according to this percentage value using df.head()
# - Write the output (jobs and percentage value) to a csv

import pandas as pd

# select useful columns by caldendar year
df = pd.read_csv('Data/employee_compensation.csv')
df = df[df['Year Type'] == 'Calendar']
cols = ['Job Family', 'Employee Identifier' , 'Salaries', 'Overtime', 'Total Benefits', 'Total Compensation']
df = df[cols]
#df.head(3)

# calculate averages
df = df.groupby(['Job Family', 'Employee Identifier'], as_index=False).mean()
#df.head(3)

# find employees whose overtime > 5% of salaries
df = employee_ave[employee_ave['Overtime'] > employee_ave['Salaries']*0.05]
#df.head(3)

# find average of Total Benefits and Total Compensation
cols = ['Job Family', 'Total Benefits', 'Total Compensation']
df = df[cols].groupby(['Job Family'], as_index=False).mean()
#df.head(4)

df['Percentage_Total_Benefit'] = df['Total Benefits'] / df['Total Compensation'] * 100
output = df.sort_values(by='Percentage_Total_Benefit', ascending=False)
#output.head(3)

# write to csv
print(output.head(3))
output.to_csv('Ass3_output/Q2_P2_output.csv',index=False,header=True)

