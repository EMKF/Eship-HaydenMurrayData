# Data downloaded from: https://portal.census.gov/pulse/data/#downloads
# Pulse Survey was conducted in three phases in 2020
# Phase 1: 4.16 - 6.27
# Phase 2: 8.9 - 10.10
# Phase 3: 11.9 - 1.10

import pandas as pd
import seaborn as sns
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

# pull the data we
df = pd.read_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/2020_bus_pulse/all_phases.xlsx')
print(df.head())

# pivot and export
pivot = pd.pivot_table(df, values='ESTIMATE_PERCENTAGE', index=['QUESTION_TEXT', 'ANSWER_TEXT'], columns=['week_end'])
print(pivot)
pivot.to_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/2020_bus_pulse/pivot_all_phases.xlsx', index=True)
