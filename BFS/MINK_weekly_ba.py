import sys
import pandas as pd

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

us = pd.read_csv('https://www.census.gov/econ/bfs/csv/bfs_us_apps_weekly_nsa.csv')
mink = pd.read_csv('https://www.census.gov/econ/bfs/csv/bfs_state_apps_weekly_nsa.csv')
week = pd.read_csv('https://www.census.gov/econ/bfs/csv/date_table.csv')

us = us[['Year', 'Week', 'BA_NSA']]
us['region'] = 'US'
mink = mink[['Year', 'Week', 'State', 'BA_NSA']]
mink.rename(columns={'State': "region"},inplace=True)

def filterer(df):
    df = df[df['Year']==2020]
    return df
us = filterer(us)
mink = filterer(mink)
week = filterer(week)

mink = mink[(mink['region'] == 'IA') | (mink['region'] == 'MO') | (mink['region'] == 'NE') | (mink['region']=='KS')]

def merger(df):
    df = df.merge(week, on='Week')
    df = df[['Week', 'End date', 'region', 'BA_NSA']]
    return df
us = merger(us)
mink = merger(mink)

df = us.append(mink)
df.sort_values(by=['Week'], inplace=True)
df.reset_index(drop=True)
df.rename(columns={'BA_NSA': "New business applications"},inplace=True)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(
    '/Users/hmurray/Desktop/data/BFS/BA/mink_weekly_ba/mink_weekly_ba.xlsx',
    engine='xlsxwriter')

# look over unique region values to export each state to a sheet
book = {}
for x in df.region.unique():
    book[x] = df[df['region'] == x]
    print(book[x].head())
    book[x].to_excel(writer, sheet_name=str(x), index=False)

writer.save()
sys.exit()