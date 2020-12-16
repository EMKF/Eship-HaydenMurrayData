# VAR:POP
# POP. List of modules
# 1 Current Freelancer
# 2 Former Entrepreneur
# 3 Former Freelancer
# 4 Entrepreneur Less Than 5
# 5 Entrepreneur More Than 5
# 7 Current Wantrapreneur
# 8 Former Wantrapreneur
# 9 General Population

# VAR:DRACE
# DRACE. To ensure we have a representative sample, please indicate your race. (IF BLACK/WHITE/OTHER) Do you consider yourself a Hispanic, Latino, or Spanish-speaking American?
# 1 Black/African-American
# 2 White/Caucasian
# 3 Hispanic/Latino
# 4 Asian-American
# 5 Native American
# 6 Other
# 7 (Refused)


import pandas as pd
import sys
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# read in data and rename columns
def data_create():
    # pull from s3
    df = pd.read_csv('/Users/hmurray/Desktop/data/EPOP/survey_documentation/epop_raw_8.11.csv', low_memory=False)
    # print(df.head())
    return df

def renamer(df):
    # rename columns
    df = df.rename(columns={'DRACE_1': 'black_african_american', 'DRACE_2': 'white_caucasian', 'DRACE_3': 'hispanic_latino',\
                            'DRACE_4': 'asian_american', 'DRACE_5': 'native_american', 'DRACE_6': 'other'})
    # recode values
    df['black_african_american'] = df['black_african_american'].astype(str).replace(str(1), 'black_african_american')
    df['white_caucasian'] = df['white_caucasian'].astype(str).replace(str(1), 'white_caucasian')
    df['hispanic_latino'] = df['hispanic_latino'].astype(str).replace(str(1), 'hispanic_latino')
    df['asian_american'] = df['asian_american'].astype(str).replace(str(1), 'asian_american')
    df['native_american'] = df['native_american'].astype(str).replace(str(1), 'native_american')
    df['other'] = df['other'].astype(str).replace(str(1), 'other')
    return df

def all_counter(df):
    # weighted frequency distribution of demographics
    black_african_american = pd.crosstab(df['black_african_american'], df['black_african_american'],\
                                         values=df['WEIGHT'], aggfunc='sum', normalize='index', margins=True)
    white_caucasian = pd.crosstab(df['white_caucasian'], df['white_caucasian'], \
                                         values=df['WEIGHT'], aggfunc='sum', normalize='index', margins=True)
    hispanic_latino = pd.crosstab(df['hispanic_latino'], df['hispanic_latino'],\
                                         values=df['WEIGHT'], aggfunc='sum', normalize='index', margins=True)
    asian_american = pd.crosstab(df['asian_american'], df['asian_american'], \
                                  values=df['WEIGHT'], aggfunc='sum', normalize='index', margins=True)
    native_american = pd.crosstab(df['native_american'], df['native_american'], \
                                  values=df['WEIGHT'], aggfunc='sum', normalize='index', margins=True)
    other = pd.crosstab(df['other'], df['other'], \
                                  values=df['WEIGHT'], aggfunc='sum', normalize='index', margins=True)
    print(black_african_american)
    print(white_caucasian)
    print(hispanic_latino)
    print(asian_american)
    print(native_american)
    print(other)
    print(' ')
    print(' ')
    print(' ')
    return df


if __name__ == '__main__':
    df = data_create()
    df = renamer(df)
    current_freelancer = df[df['POP_1'] == 1]
    former_entrepreneur = df[df['POP_2'] == 1]
    former_freelancers = df[df['POP_3'] == 1]
    entrepreneur_less_5 = df[df['POP_4'] == 1]
    entrepreneur_more_5 = df[df['POP_5'] == 1]
    current_wantrapreneur = df[df['POP_7'] == 1]
    former_wantrapreneur = df[df['POP_8'] == 1]
    general_population = df[df['POP_9'] == 1]
    print('ALL RESPONDENTS')
    df = all_counter(df)
    print('CURRENT FREELANCERS')
    current_freelancer = all_counter(current_freelancer)
    print('FORMER ENTREPRENEUR')
    former_entrepreneur = all_counter(former_entrepreneur)
    print('FORMER FREELANCERS')
    former_freelancers = all_counter(former_freelancers)
    print('ENTREPRENEUR LESS THAN 5')
    entrepreneur_less_5 = all_counter(entrepreneur_less_5)
    print('ENTREPRENEUR MORE THAN 5')
    entrepreneur_more_5 = all_counter(entrepreneur_more_5)
    print('CURRENT WANTRAPRENEUR')
    current_wantrapreneur = all_counter(current_wantrapreneur)
    print('FORMER WANTRAPRENUER')
    former_wantrapreneur = all_counter(former_wantrapreneur)
    print('GENERAL POPULATION')
    general_population = all_counter(general_population)


sys.exit()
