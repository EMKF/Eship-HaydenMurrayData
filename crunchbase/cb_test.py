import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

def data_create():
    return pd.read_csv('/Users/hmurray/Desktop/data/crunchbase/funding_rounds_founded_after_1.1.21_in_US.csv',
                       usecols=['Organization Name', 'Funding Type', 'Money Raised', 'Announced Date', 'Money Raised Currency (in USD)'])

def calculator(df):
    df['fund_share_raised'] = df['Money Raised Currency (in USD)'] / df['Money Raised']
    return df
if __name__ == '__main__':
    df = data_create()
    df = calculator(df)
    print(df)


sys.exit()