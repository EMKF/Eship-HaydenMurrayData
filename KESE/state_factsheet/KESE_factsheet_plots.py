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
    return pd.read_excel('/Users/hmurray/Desktop/data/KESE/state_factsheet/maddi_copy_creation/all_factsheet_data_copy.xlsx')


def plotter(df, state):
    indicators = ['rne', 'ose', 'sjc', 'ssr']
    for indicator in indicators:
        df_temp = df[(df.name == 'United States') | (df.name == state)].reset_index(drop=True)
        df_temp = df_temp.pivot_table(index=['year'], columns=['name'], values=indicator).reset_index()
        df_temp.plot(x='year', y=[state, 'United States'])
        plt.xlim(1996, 2020)
        plt.xlabel('time')
        plt.xticks(rotation=45)
        plt.ylabel(indicator)
        leg_1_labels = [state, 'United States']
        plt.legend(labels=leg_1_labels)
        title = (str(state) + ' ' + (indicator))
        plt.title("\n".join(wrap(title, 70)))
        plt.tight_layout()
        plt.grid()
        plt.savefig('/Users/hmurray/Desktop/data/KESE/state_factsheet/maddi_copy_creation/plots/' + str(state) + '_' + str(indicator) + '.png')
    return df



if __name__ == '__main__':
    df = data_create()
    for state in df['name'].unique():
        df = plotter(df, state)

sys.exit()