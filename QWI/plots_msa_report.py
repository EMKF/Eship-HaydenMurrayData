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

# pull in msa data from S3
df = pd.read_excel('s3://emkf.data.research/sandbox/hayden/cleaned_msa_data.xlsx')

def sorter(indicator):
    # filter and select top 3 for each indicator
    temp_df = df[(df['time'] == 2017) & (df['firmage'] == '0-1 years')]\
        .reset_index(drop=True).sort_values(by=indicator, ascending=False).reset_index(drop=True)
    temp_df = temp_df[['fips', indicator]]
    temp_df = temp_df.head(3)
    print(temp_df)
    top_three = temp_df['fips'].values.tolist()

    # filter original df for the top 3 in that indicator
    for x in top_three:
        plot_df = df[(df['fips'] == x)].reset_index(drop=True)
        plot_df = plot_df[plot_df['firmage'] == '0-1 years'].reset_index(drop=True)
    print(plot_df)


    sys.exit()
    rne_max_min_med = rne_max_min_med[['STATE', 'year', 'RATE OF NEW ENTREPRENEURS']]
    rne_max_min_med = rne_max_min_med.pivot_table(index=['year'], columns='STATE',
                                                  values='RATE OF NEW ENTREPRENEURS').reset_index()
    rne_plot = rne_max_min_med.merge(med_rne, on='year')
    rne_plot.rename(columns={"RATE OF NEW ENTREPRENEURS": "Yearly Median"}, inplace=True)
    rne_plot['year'] = rne_plot['year'].astype(str)
    rne_plot.plot(x='year', y=['Rhode Island', 'Florida', 'Yearly Median'])
    plt.title("\n".join(
        wrap("FIGURE 19 RATE OF NEW ENTREPRENEURS OVER TIME (1998–2019) (LOWEST AND HIGHEST IN 2019 AND YEARLY MEDIAN)",
             50)))
    axes = plt.gca()
    plt.tight_layout()
    axes.set_ylim([0, .5])
    plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/rne2.png')
    plt.show()


sorter('contribution')
sorter('compensation')
sorter('constancy')
sorter('creation')
sorter('q2_index')

sys.exit()





