import pandas as pd

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

state_fips_abb_dic = {v: k for k, v in state_abb_fips_dic.items()}

state_name_abb_dic = {
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

state_abb_name_dic = dict(map(reversed, state_name_abb_dic.items()))


shed_dic = {
    2013: {
        'zip_url': 'https://www.federalreserve.gov/consumerscommunities/files/SHED_data_2013_(CSV).zip',
        'filename': 'SHED_public_use_data_2013.csv',
        'col_name_dic': {
            'v1_2013': 'v1_final',  # todo: at some point in the future there might be variables to rename...use as rename(c.shed_dic[year]['col_name_dic'])
        }
    },
    2014: {
        'zip_url': 'https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2014_(CSV).zip',
        'filename': 'SHED_public_use_data_2014_update (occupation industry).csv',
        'col_name_dic': {
            'v1_2014': 'v1_final',
        }
    },
    2015: {
        'zip_url': 'https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2015_(CSV).zip',
        'filename': 'SHED 2015 public use.csv',
        'col_name_dic': {
            'v1_2014': 'v1_final',
        }
    },
    2016: {
        'zip_url': 'https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2016_(CSV).zip',
        'filename': 'SHED_2016_Public_Data.csv',
        'col_name_dic': {
            'v1_2014': 'v1_final',
        }
    },
    2017: {
        'zip_url': 'https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2017_(CSV).zip',
        'filename': 'SHED_2017_Public_Use.csv',
        'col_name_dic': {
            'v1_2014': 'v1_final',
            'v2_2014': 'v2_final',
            'v3_2014': 'v3_final',
            'v4_2014': 'v4_final',
        }
    },
    2018: {
        'zip_url': 'https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2018_(CSV).zip',
        'filename': 'public2018.csv',
        'col_name_dic': {
            'v1_2014': 'v1_final',
            'v2_2014': 'v2_final',
            'v3_2014': 'v3_final',
            'v4_2014': 'v4_final',
        }
    },
    2019: {
        'zip_url': 'https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2019_(CSV).zip',
        'filename': 'public2019.csv',
        'col_name_dic': {
            'v1_2014': 'v1_final',
            'v2_2014': 'v2_final',
            'v3_2014': 'v3_final',
            'v4_2014': 'v4_final',
        }
    },
    2020: {
        'zip_url': 'https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2020_(CSV).zip',
        'filename': 'public2020.csv',
        'col_name_dic': {
            'v1_2014': 'v1_final',
            'v2_2014': 'v2_final',
            'v3_2014': 'v3_final',
            'v4_2014': 'v4_final',
        }
    },
}

shed_state_codes = {11: "ME", 12: "NH", 13: "VT", 14: "MA", 15: "RI", 16: "CT",
                            21: "NY", 22: "NJ", 23: "PA", 31: "OH", 32: "IN", 33: "IL", 34: "MI", 35: "WI",
                            41: "MN", 42: "IA", 43: "MO", 44: "ND", 45: "SD", 46: "NE", 47: "KS",
                            51: "DE", 52: "MD", 53: "DC", 54: "VA", 55: "WV", 56: "NC", 57: "SC", 58: "GA",
                            59: "FL", 61: "KY", 62: "TN", 63: "AL", 64: "MS", 71: "AR", 72: "LA", 73: "OK",
                            74: "TX", 81: "MT", 82: "ID", 83: "WY", 84: "CO", 85: "NM", 86: "AZ", 87: "UT",
                            88: "NV", 91: "WA", 92: "OR", 93: "CA", 94: "AK", 95: "HI"}
