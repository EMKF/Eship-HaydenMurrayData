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
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

df = pd.read_csv('s3://emkf.data.research/indicators/nej/msa_nej_2020.06.24.csv')
print(df.head())
print(df.info())
print(df['fips'].value_counts())
sys.exit()