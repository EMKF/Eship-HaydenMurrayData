import sys
import pandas as pd
import kauffman
import matplotlib.pyplot as plt
import datetime
import numpy as np
from textwrap import wrap
from matplotlib.dates import date2num

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None



def data_create():
    # pull from local excel file
    df = pd.read_csv('/Users/hmurray/Desktop/data/presentation/data/qwi_emps_frmjbcr.csv')
    df = df[['year', 'quarter', 'EmpS', 'FrmJbC']]
    df = df.groupby(['year']).mean().reset_index()
    df.to_excel('/Users/hmurray/Desktop/data/presentation/data/cleaned_qwi_alljobs_emps.xlsx')
    return df

def plotter_1(df):
    df.plot(x='year', y=['EmpS'])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    plt.ylabel('Count')
    # plt.ylim(0, 600000)
    plt.yticks(rotation=45)
    leg_1_labels = ['Four quarter average of Emps for each year (QWI)']
    plt.legend(labels=leg_1_labels, loc='upper right')
    # title = (title)
    # plt.title("\n".join(wrap(title, 50)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/presentation/plots/emps_qwi.png')
    plt.show()
    return df

def plotter_2(df):
    df.plot(x='year', y=['FrmJbC'])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    plt.ylabel('Count')
    # plt.ylim(0, 600000)
    # plt.yticks(np.arange(0, 1150, step=100), rotation=45)
    leg_1_labels = ['Sum of FrmJbC (QWI)']
    plt.legend(labels=leg_1_labels)
    # title = (title)
    # plt.title("\n".join(wrap(title, 50)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/presentation/plots/FrmJbC_qwi.png')
    plt.show()
    return df

if __name__ == '__main__':
    df = data_create()
    df = plotter_1(df)
    df = plotter_2(df)

sys.exit()