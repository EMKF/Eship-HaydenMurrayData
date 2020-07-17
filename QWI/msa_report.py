import sys
import pandas as pd
from kauffman_data import bfs, pep
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
pd.options.mode.chained_assignment = None

# define dict with MSA names for each fip code
msa_fips_codes_names_dic = {
    '12060': 'Atlanta-Sandy Springs-Roswell, GA',
    '12420': 'Austin-Round Rock, TX',
    '12580': 'Baltimore-Columbia-Towson, MD',
    '13820': 'Birmingham-Hoover, AL',
    '15380': 'Buffalo-Cheektowaga-Niagara Falls, NY',
    '17460': 'Cleveland-Elyria, OH',
    '18140': 'Columbus, OH',
    '19100': 'Dallas-Fort Worth-Arlington, TX',
    '19740': 'Denver-Aurora-Lakewood, CO',
    '19820': 'Detroit-Warren-Dearborn, MI',
    '25540': 'Hartford-West Hartford-East Hartford, CT',
    '26420': 'Houston-The Woodlands-Sugar Land, TX',
    '26900': 'Indianapolis-Carmel-Anderson, IN',
    '27260': 'Jacksonville, FL',
    '29820': 'Las Vegas-Henderson-Paradise, NV',
    '31080': 'Los Angeles-Long Beach-Anaheim, CA',
    '33100': 'Miami-Fort Lauderdale-West Palm Beach, FL',
    '33340': 'Milwaukee-Waukesha-West Allis, WI',
    '34980': 'Nashville-Davidson--Murfreesboro--Franklin, TN',
    '35380': 'New Orleans-Metairie, LA',
    '36420': 'Oklahoma City, OK',
    '36740': 'Orlando-Kissimmee-Sanford, FL',
    '38060': 'Phoenix-Mesa-Scottsdale, AZ',
    '38300': 'Pittsburgh, PA',
    '39580': 'Raleigh, NC',
    '40060': 'Richmond, VA',
    '40140': 'Riverside-San Bernardino-Ontario, CA',
    '40900': 'Sacramento--Roseville--Arden-Arcade, CA',
    '41620': 'Salt Lake City, UT',
    '41700': 'San Antonio-New Braunfels, TX',
    '41740': 'San Diego-Carlsbad, CA',
    '41860': 'San Francisco-Oakland-Hayward, CA',
    '41940': 'San Jose-Sunnyvale-Santa Clara, CA',
    '42660': 'Seattle-Tacoma-Bellevue, WA',
    '45300': 'Tampa-St. Petersburg-Clearwater, FL',
    '47900': 'Washington-Arlington-Alexandria, DC-VA-MD-WV',
    '47260': 'Virginia Beach-Norfolk-Newport News, VA-NC',
    '41180': 'St. Louis, MO-IL',
    '39300': 'Providence-Warwick, RI-MA',
    '38900': 'Portland-Vancouver-Hillsboro, OR-WA',
    '35620': 'New York-Newark-Jersey City, NY-NJ-PA',
    '14460': 'Boston-Cambridge-Newton, MA-NH',
    '16740': 'Charlotte-Concord-Gastonia, NC-SC',
    '16980': 'Chicago-Naperville-Elgin, IL-IN-WI',
    '17140': 'Cincinnati, OH-KY-IN',
    '28140': 'Kansas City, MO-KS',
    '31140': 'Louisville/Jefferson County, KY-IN',
    '32820': 'Memphis, TN-MS-AR',
    '33460': 'Minneapolis-St. Paul-Bloomington, MN-WI',
    '37980': 'Philadelphia-Camden-Wilmington, PA-NJ-DE-MD'
}

# define dict with age categories
age_categories = {
    '1': '0-1 years',
    '2': '2-3 years',
    '3': '4-5 years',
    '4': '6-10 years',
    '5': '11+ years'
}

# pull in msa data from S3
df = pd.read_csv('s3://emkf.data.research/indicators/nej/msa_nej_2020.06.24.csv')

# replace fips with name of MSAs
df['fips'] = df['fips'].astype(str)
df["fips"].replace(msa_fips_codes_names_dic, inplace=True)

# replace age number with string
df['firmage'] = df['firmage'].astype(str)
df["firmage"].replace(age_categories, inplace=True)
print(df.head())

# subset for table 1
msa_2017_all = df[df['time'] == 2017]

# subset for table 2 and sort by contribution
msa_contribution = df.pivot_table(index=['fips', 'firmage'], columns='time', values='contribution').reset_index()
msa_contribution = msa_contribution.sort_values(by=[2017], ascending=False).reset_index(drop=True)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/hmurray/Desktop/Jobs_Indicators/hm_draft/msa_report_tables.xlsx', engine='xlsxwriter')

# write each table to excel file
def msa_report_writer(table, tab_name):
    print(table.head())
    table.to_excel(writer, sheet_name=str(tab_name), index=False)

msa_report_writer(msa_2017_all, 'table_1')
msa_report_writer(msa_contribution, 'table_2')

writer.save()
sys.exit()

