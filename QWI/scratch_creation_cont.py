import pandas as pd
import sys
import time
import matplotlib.pyplot as plt
import requests
import numpy as np
import seaborn as sns
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# time
start = time.time()

# pull data from indicators.kauffman.org
df = pd.read_csv('https://indicators.kauffman.org/wp-content/uploads/sites/2/2020/08/Kauffman_Indicators_Multi-Dimensional_Private_Jobs_Data_2017.csv')

# reduce columns
df = df[['name', 'category', 'year', 'contribution', 'creation']]

# drop total
df = df.query('category != "Total"')

# cleaning
long_cont = df.pivot_table(index=['name', 'category'], columns='year', values='contribution').reset_index()
long_cont.to_excel('/Users/hmurray/Desktop/data/QWI/long_cont.xlsx', index=False)
long_create = df.pivot_table(index=['name', 'category'], columns='year', values='creation').reset_index()
long_create.to_excel('/Users/hmurray/Desktop/data/QWI/long_create.xlsx', index=False)

# pull data from indicators.kauffman.org
msa = pd.read_csv('/Users/hmurray/Desktop/data/QWI/msa_nej_2020.06.24.csv')
msa_cont_long = msa.pivot_table(index=['name', 'firmage'], columns='time', values='contribution').reset_index()
msa_cont_long.to_excel('/Users/hmurray/Desktop/data/QWI/msa_cont_long.xlsx', index=False)
msa_create_long = msa.pivot_table(index=['name', 'firmage'], columns='time', values='creation').reset_index()
msa_create_long.to_excel('/Users/hmurray/Desktop/data/QWI/msa_create_long.xlsx', index=False)

end = time.time()
print((end/60) - (start/60))
sys.exit()