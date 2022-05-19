import sys
import pandas as pd
import kauffman.data as kauffman
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
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

def data_create():
    # pull 2021 neb data download
    df = pd.read_csv('s3://emkf.data.research/indicators/neb/data_outputs/2021/2021_neb_download.csv')
    # filter
    df = df[(df['name'] != 'United States')].reset_index(drop=True)
    df = df[(df['year'] != 2022)].reset_index(drop=True)
    # subset df by necessary columns
    df = df[['fips', 'name', 'year', 'actualization', 'bf_per_capita', 'velocity', 'newness', 'index']]
    # rename columns
    df = df.rename(columns={'bf_per_capita': 'rate_new_employer_business', 'index': 'NEBAS_index'})
    return df

def actualization_plot():
    # Min, Max, Median
    actualization = df.groupby('year', as_index=False)['actualization'].agg({'minimum': 'min', 'maximum': 'max', 'median': 'median'})
    actualization.reset_index(inplace=True, drop=True)
    print(actualization)
    actualization.to_excel('/Users/hmurray/Desktop/NEB/2021/data/plots/min_max_med/actual_min_max_med.xlsx', index=False)
    # plot min, max, median
    actualization.plot(x='year', y=['minimum', 'maximum', 'median'])
    plt.title("\n".join(wrap("Actualization Minimum, Maximum, and Median for each year between 2005-2021", 62)))
    plt.xlabel('Year')
    plt.ylabel('Actualization')
    plt.legend(labels=['Minimum', 'Maximum', 'Median'], loc='best', fontsize='small')
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/min_max_med/state_actualization1.png')
    plt.show()
    # histogram
    actual_hist = df[(df['year'] == 2021)].reset_index(drop=True)
    plt.hist(actual_hist['actualization'], density=True, bins=20)
    plt.title("\n".join(wrap("Distribution of Actualization in 2021", 62)))
    plt.xlabel('Year')
    plt.ylabel('Actualization')
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/state_actualization2.png')
    plt.show()
    return df

def rneb_plot():
    # Min, Max, Median
    rneb = df.groupby('year', as_index=False)['rate_new_employer_business'].agg({'minimum': 'min', 'maximum': 'max', 'median': 'median'})
    rneb.reset_index(inplace=True, drop=True)
    print(rneb)
    rneb.to_excel('/Users/hmurray/Desktop/NEB/2021/data/plots/min_max_med/rneb_min_max_med.xlsx', index=False)
    # plot min, max, median
    rneb.plot(x='year', y=['minimum', 'maximum', 'median'])
    plt.title("\n".join(wrap("Rate of New Employer Business Minimum, Maximum, and Median for each year between 2005-2021", 62)))
    plt.xlabel('Year')
    plt.ylabel('Rate of New Employer Business')
    plt.legend(labels=['Minimum', 'Maximum', 'Median'], loc='best', fontsize='small')
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/min_max_med/state_rneb1.png')
    plt.show()
    # histogram
    rneb_hist = df[(df['year'] == 2021)].reset_index(drop=True)
    plt.hist(rneb_hist['rate_new_employer_business'], density=True, bins=12)
    plt.title("\n".join(wrap("Distribution of the Rate of New Employer Business in 2021", 62)))
    plt.xlabel('Year')
    plt.ylabel('Rate of New Employer Business')
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/state_rneb2.png')
    plt.show()
    return df

def velocity_plot():
    # Min, Max, Median
    velocity = df.groupby('year', as_index=False)['velocity'].agg({'minimum': 'min', 'maximum': 'max', 'median': 'median'})
    velocity.reset_index(inplace=True, drop=True)
    print(velocity)
    velocity.to_excel('/Users/hmurray/Desktop/NEB/2021/data/plots/min_max_med/velocity_min_max_med.xlsx', index=False)
    # plot min, max, median
    velocity.plot(x='year', y=['minimum', 'maximum', 'median'])
    plt.title("\n".join(wrap("Velocity Minimum, Maximum, and Median for each year between 2005-2017", 62)))
    plt.xlabel('Year')
    plt.ylabel('Velocity')
    plt.legend(labels=['Minimum', 'Maximum', 'Median'], loc='best', fontsize='small')
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/min_max_med/state_velocity1.png')
    plt.show()
    # histogram
    velocity_hist = df[(df['year'] == 2017)].reset_index(drop=True)
    plt.hist(velocity_hist['velocity'], density=True, bins=20)
    plt.title("\n".join(wrap("Distribution of Velocity in 2017", 62)))
    plt.xlabel('Year')
    plt.ylabel('Velocity')
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/state_velocity2.png')
    plt.show()
    return df

def newness_plot():
    # Min, Max, Median
    newness = df.groupby('year', as_index=False)['newness'].agg({'minimum': 'min', 'maximum': 'max', 'median': 'median'})
    newness.reset_index(inplace=True, drop=True)
    print(newness)
    newness.to_excel('/Users/hmurray/Desktop/NEB/2021/data/plots/min_max_med/newness_min_max_med.xlsx', index=False)
    # plot min, max, median
    newness.plot(x='year', y=['minimum', 'maximum', 'median'])
    plt.title("\n".join(wrap("Newness Minimum, Maximum, and Median for each year between 2005-2019", 62)))
    plt.xlabel('Year')
    plt.ylabel('Newness')
    plt.legend(labels=['Minimum', 'Maximum', 'Median'], loc='best', fontsize='small')
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/min_max_med/state_newness1.png')
    plt.show()
    # histogram
    newness_hist = df[(df['year'] == 2019)].reset_index(drop=True)
    plt.hist(newness_hist['newness'], density=True, bins=12)
    plt.title("\n".join(wrap("Distribution of Newness in 2019", 62)))
    plt.xlabel('Year')
    plt.ylabel('Newness')
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/state_newness2.png')
    plt.show()
    return df

def nebas_index_plot():
    # Min, Max, Median
    nebas = df.groupby('year', as_index=False)['NEBAS_index'].agg({'minimum': 'min', 'maximum': 'max', 'median': 'median'})
    nebas.reset_index(inplace=True, drop=True)
    print(nebas)
    nebas.to_excel('/Users/hmurray/Desktop/NEB/2021/data/plots/min_max_med/nebas_index_min_max_med.xlsx', index=False)
    # plot min, max, median
    nebas.plot(x='year', y=['minimum', 'maximum', 'median'])
    plt.title("\n".join(wrap("NEBAS Index Minimum, Maximum, and Median for each year between 2005-2017", 62)))
    plt.xlabel('Year')
    plt.ylabel('NEBAS Index')
    plt.legend(labels=['Minimum', 'Maximum', 'Median'], loc='best', fontsize='small')
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/min_max_med/state_nebas_index1.png')
    plt.show()
    # histogram
    nebas_hist = df[(df['year'] == 2017)].reset_index(drop=True)
    plt.hist(nebas_hist['NEBAS_index'], density=True, bins=12)
    plt.title("\n".join(wrap("Distribution of NEBAS Index in 2017", 62)))
    plt.xlabel('Year')
    plt.ylabel('NEBAS Index')
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/state_nebas_index2.png')
    plt.show()
    return df

if __name__ == '__main__':
    df = data_create()
    df = actualization_plot()
    df = rneb_plot()
    df = velocity_plot()
    df = newness_plot()
    df = nebas_index_plot()
    print(df.head())