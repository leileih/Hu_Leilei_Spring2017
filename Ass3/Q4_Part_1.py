
# coding: utf-8

# # Question 4 Part 1
# - Use ‘movies_awards’ data set
# - You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below
# - The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.)
# - You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award
# - If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated)
# - Create two separate columns for each award category (won and nominated)
# - Write your output to a csv file

import pandas as pd
import re 

# select needed columns and drop NaNs
df = pd.read_csv('Data/movies_awards.csv')
cols = ['imdbID', 'Title', 'Awards']
df = df[cols]  # select columns and then drop NaNs from these columns
df = df.dropna()
df.head(3)

# find number of named wins. Like Oscar'...
def find_named_wins(name, row):
    pattern = r'Won (\d+) '+name
    nums = re.findall(pattern, row)
    if len(nums)>0:
        return nums[0]
    else:
        return '0'

# find number of named Nominations. Like 'Oscar'...
def find_named_Nominated(name, row):
    pattern = r'Nominated for (\d+) '+name
    nums = re.findall(pattern, row)
    if len(nums)>0:
        return nums[0]
    else:
        return '0'

# find number of total wins. 
def find_all_wins(row):
    pattern = r'(\d+) win'
    named_wins = int(row['Oscar_Won'])+int(row['Prime_Won'])+int(row['Golden_Globe_Won'])+int(row['BAFTA_Won'])
    nums = re.findall(pattern, row['Awards'])
    if len(nums)>0:
        return int(nums[0])+named_wins
    else:
        return named_wins

# get total of nominations. total = other_nominations + Oscar_nominations + Prime_nominations + ...
def find_all_Nominated(row):
    pattern = r'(\d+) nomination'
    named_Nominated = int(row['Prime_Nominated'])+int(row['Oscar_Nominated'])+int(row['Golden_Globe_Nominated'])+int(row['BAFTA_Nominated'])
    nums = re.findall(pattern, row['Awards'])
    if len(nums)>0:
        return int(nums[0])+named_Nominated
    else:
        return named_Nominated


df['Oscar_Won'] = df.apply(lambda row: find_named_wins('Oscar', row['Awards']), axis=1)
df['Prime_Won'] = df.apply(lambda row: find_named_wins('Prime', row['Awards']), axis=1)
df['Golden_Globe_Won'] = df.apply(lambda row: find_named_wins('Golden', row['Awards']), axis=1)
df['BAFTA_Won'] = df.apply(lambda row: find_named_wins('BAFTA', row['Awards']), axis=1)
df.head(3)


df['Prime_Nominated'] = df.apply(lambda row: find_named_Nominated('Prime', row['Awards']), axis=1)
df['Oscar_Nominated'] = df.apply(lambda row: find_named_Nominated('Oscar', row['Awards']), axis=1)
df['Golden_Globe_Nominated'] = df.apply(lambda row: find_named_Nominated('Golden', row['Awards']), axis=1)
df['BAFTA_Nominated'] = df.apply(lambda row: find_named_Nominated('BAFTA', row['Awards']), axis=1)
df.head(3)


# After caculated Special wins and nominations, add those to total wins and nominations
df['Awards_won'] = df.apply(find_all_wins, axis=1)


df['Awards_Nominated'] = df.apply(find_all_Nominated, axis=1)
cols = df.columns.tolist()
cols = cols[0:3] + cols[-2:] + cols[3:-2]
df = df[cols]
#df.head(3)


# write to csv
print(df.head(3))
df.to_csv('Ass3_output/Q4_P1_output.csv',index=False,header=True)

