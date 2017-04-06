
# coding: utf-8

# # Question 3 Part 1
# - Use ‘cricket_matches’ data set
# - Calculate the average score for each team which host the game and win the game
# - Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition
# - Display a few rows of the output use df.head()
# - Generate a csv output

import pandas as pd

# select teams host the game and win the game
df = pd.read_csv('Data/cricket_matches.csv')
df = df[df['home'] == df['winner']]
#df.head(3)

# select columns used
cols = ['winner', 'innings1' , 'innings2', 'innings1_runs', 'innings2_runs']
df = df[cols]
#df.head(3)

# find which innings they played in
def innings_in(row):
    if row['winner'] == row['innings1']:
        return row['innings1_runs']
    else:
        return row['innings2_runs']

# drop NaNs and add Score column
df['Score'] = df.apply(innings_in, axis=1)
#df.head(3)

# select useful data columns
cols = ['winner', 'Score']
df= df[cols]
#df.head(3)

# calculate average scores of each team
output = df.groupby(['winner'], as_index=False).mean()
#output.head(3)

# write to csv
print(output.head(3))
output.to_csv('Ass3_output/Q3_P1_output.csv',index=False,header=True)
