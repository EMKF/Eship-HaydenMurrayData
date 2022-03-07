import sys
import pandas as pd
import numpy as np
import warnings
import requests
warnings.simplefilter(action='ignore', category=FutureWarning)
import matplotlib.pyplot as plt
from textwrap import wrap
import kauffman.constants as c
from kauffman.data import acs, bfs, bds, pep, bed, qwi, shed

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 40000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)





tab_1bf = bed(series='establishment age and survival', table='1bf', obs_level='us')
tab7 = bed(series='establishment age and survival', table=7, obs_level='us')
# print(tab_1bf)
print(tab7)
sys.exit()


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'United States': 'US'
}

state_abb_fips_dic = {
    'WA': '53', 'DE': '10', 'DC': '11', 'WI': '55', 'WV': '54', 'HI': '15',
    'FL': '12', 'WY': '56', 'PR': '72', 'NJ': '34', 'NM': '35', 'TX': '48',
    'LA': '22', 'NC': '37', 'ND': '38', 'NE': '31', 'TN': '47', 'NY': '36',
    'PA': '42', 'AK': '02', 'NV': '32', 'NH': '33', 'VA': '51', 'CO': '08',
    'CA': '06', 'AL': '01', 'AR': '05', 'VT': '50', 'IL': '17', 'GA': '13',
    'IN': '18', 'IA': '19', 'MA': '25', 'AZ': '04', 'ID': '16', 'CT': '09',
    'ME': '23', 'MD': '24', 'OK': '40', 'OH': '39', 'UT': '49', 'MO': '29',
    'MN': '27', 'MI': '26', 'RI': '44', 'KS': '20', 'MT': '30', 'MS': '28',
    'SC': '45', 'KY': '21', 'OR': '41', 'SD': '46', 'US': '00'
}

def _make_header(df):
    df.columns = df.iloc[0]
    return df.iloc[1:]

def pep_pre_2000(region):
    """Fetch population data for years: 1996 - 1999."""
    return pd.read_excel('http://www2.census.gov/library/publications/2011/compendia/statab/131ed/tables/12s0013.xls?', skiprows=3, skipfooter=9).\
        rename(columns={'State': 'region'}). \
        query('region not in ["Northeast", "Midwest", "South", "West "]') \
        [['region'] + [str(year) + " (July)" for year in range(1996, 2000)]].\
        query('region == "  United States "' if region == 'us' else 'region != "  United States "'). \
        rename(columns=lambda x: int(x[0:4]) if x != 'region' else x).\
        pipe(pd.melt, id_vars='region', value_vars=range(1996, 2000), var_name='time', value_name='population').\
        assign(
            region=lambda x: x.region.str.strip(),
            fips=lambda x: x.region.map(us_state_abbrev).map(state_abb_fips_dic),
            population=lambda x: x['population'] * 1000
        ).\
        astype({'time': 'int'}) \
        [['fips', 'region', 'time', 'population']]


def _us_2010_2019():
    url = 'https://api.census.gov/data/2019/pep/population?get=NAME,POP,DATE_CODE&for=us:*'

    return pd.DataFrame(requests.get(url).json()). \
        pipe(_make_header). \
        rename(columns={'NAME': 'region', 'DATE_CODE': 'date'}). \
        astype({'date': 'int'}). \
        query('3 <= date <= 12').\
        query('region not in ["Puerto Rico"]').\
        assign(
            time=lambda x: '20' + (x['date'] + 7).astype(str),
            fips=lambda x: x['region'].map(c.all_name_to_fips),
        ) \
        [['fips', 'region', 'time', 'POP']]


def pep_2020(region):
    """Fetch population data for 2020."""
    if region == 'us':
        return pd.read_excel('https://www2.census.gov/programs-surveys/popest/tables/2010-2019/national/totals/na-est2019-01.xlsx', skiprows=2, usecols=['Year and Month', 'Resident Population']).\
            iloc[128:139, :].\
            rename(columns={'Year and Month':'time', 'Resident Population': 'population'}).\
            query('time == ".July 1"').\
            assign(
                time=2020,
                fips='00',
                region='United States'
            ) \
            [['fips', 'region', 'time', 'population']]
    else:
        return pd.read_excel('https://www2.census.gov/programs-surveys/popest/tables/2010-2020/state/totals/nst-est2020.xlsx', skiprows=3, skipfooter=5).\
            rename(columns={'Unnamed: 0': 'region', 'July 1': 'population'}) \
            [['region', 'population']].\
            query('region not in ["Northeast", "Midwest", "South", "West", "United States"]').\
            dropna().\
            assign(
                region=lambda x: x.region.apply(lambda x: x.strip('.')),
                fips=lambda x: x.region.map(us_state_abbrev).map(state_abb_fips_dic),
                time=2020
            ) \
            [['fips', 'region', 'time', 'population']]

def pep_2021(region):
    """Fetch population data for 2021."""
    if region == 'us':
        return pd.read_excel('https://www2.census.gov/programs-surveys/popest/tables/2020-2021/national/totals/NA-EST2021-POP.xlsx', skiprows=2, usecols=['Year and Month', 'Resident Population']).\
            iloc[11:23, :].\
            rename(columns={'Year and Month':'time', 'Resident Population': 'population'}).\
            query('time == ".July 1"').\
            assign(
                time=2021,
                fips='00',
                region='United States'
            ) \
            [['fips', 'region', 'time', 'population']]
    else:
        return pd.read_excel('https://www2.census.gov/programs-surveys/popest/tables/2020-2021/state/totals/NST-EST2021-POP.xlsx', skiprows=3, skipfooter=5).\
            rename(columns={'Unnamed: 0': 'region', 2021: 'population'}) \
            [['region', 'population']].\
            query('region not in ["Northeast", "Midwest", "South", "West", "United States"]').\
            dropna().\
            assign(
                region=lambda x: x.region.apply(lambda x: x.strip('.')),
                fips=lambda x: x.region.map(us_state_abbrev).map(state_abb_fips_dic),
                time=2021
            ) \
            [['fips', 'region', 'time', 'population']]



if __name__ == '__main__':
    df = _us_2010_2019()
    # df = pepper()
    print(df)

