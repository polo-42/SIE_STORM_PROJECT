# load games.csv and sales.csv with pandas
# replace Title on sales.csv with Id from games.csv that has the same title
# save the new sales.csv as sales2.csv

import pandas as pd

games = pd.read_csv('games.csv')
sales = pd.read_csv('sales.csv')

games_as_dict = {}
for index, row in games.iterrows():
    games_as_dict[row['Title']] = row['Id']

for index, row in sales.iterrows():
    if row['Title'] in games_as_dict:
        sales.at[index, 'Title'] = games_as_dict[row['Title']]
    else:
        # remove row if title is not in games.csv
        sales.drop(index, inplace=True)

sales.to_csv('sales2.csv', index=False)
