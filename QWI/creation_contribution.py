import pandas as pd
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

# pull MDJ indicators
df = pd.read_csv('s3://emkf.data.research/indicators/nej/data_outputs/nej_download_names_2020.06.24.csv')

# subset for creation and contribution analysis
df = df[['name', 'fips', 'year', 'category', 'contribution', 'creation']]

# rename columns
df.rename(columns={'category': 'age_category'}, inplace=True)

# delete the "total" age category that was created for Alley
df = df.query('age_category != "Total"')
print(df.head(50))

# export the cleaned version for Daniel Sparks
df.to_excel('/Users/hmurray/Desktop/Contractors/data_brief_contractors/data_brief_contractors/Daniel_Sparks/data/creation_contribution.xlsx', index=False)



