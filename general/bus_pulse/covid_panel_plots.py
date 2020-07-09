# Original data downloaded from: https://portal.census.gov/pulse/data/#downloads

import pandas as pd
import sys
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None


# read in stacked covid panel dataset
df = pd.read_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/python/small_bus_pulse/clean_bus_pulse_data.xlsx')


sns.set_style("whitegrid")  # , {'axes.grid': False})
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)
for ID in df['ID'].unique():
    df_temp = df[df['ID'] == ID]
    ax.plot(df_temp['WEEK'], df_temp['ESTIMATE_PERCENTAGE'], label='26Apr' if ID == '26Apr20_2May20' else 'other')
    plt.show()


sys.exit()
