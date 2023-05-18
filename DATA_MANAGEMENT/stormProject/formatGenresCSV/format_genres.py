# format column Genres of genres.csv to add row based on the number of genres that is in the array of the column
import pandas as pd
import json

df = pd.read_csv('genres.csv')

# iterate over each row with all columns
newCSV = []

for row in df.itertuples(index=False):
    # get the genres column
    id = row[0] 
    genres = row[1].strip('][').split(',')
    
    # iterate over each genre
    for genre in genres:
        newCSV.append((id,genre))

newCSV = pd.DataFrame(newCSV,columns=['id','genre'])
newCSV.to_csv('genres_2.csv',index=False)