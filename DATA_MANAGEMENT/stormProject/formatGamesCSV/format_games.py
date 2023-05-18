# Read csv file and format column Release_date to YYYY-MM-DD
import pandas as pd
df = pd.read_csv('games.csv')

formatMonthToSql = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'oct.': '10',
    'nov.': '11',
    'Dec': '12'
}

newCSV = []
for row in df['Release_date']:
    try:
        (month_and_day,year) = row.split(',')
        year = year.strip()
        (month,day) = month_and_day.split(' ')
        if day[0] == '0':
            day = day[1:]
        month = formatMonthToSql[month]
        newCSV.append((year,month,day))
    except:
        (year,month,day) = ('','','')

newCSV = pd.DataFrame(newCSV,columns=['Year','Month','Day'])
# remove Release_date column
df = df.drop(columns=['Release_date'])
# add newCSV to df
df = pd.concat([df,newCSV],axis=1)
# write to csv
df.to_csv('games.csv',index=False)


