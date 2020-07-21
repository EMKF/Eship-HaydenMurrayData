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
print(df.head())

#########################################################################################################################
################################################# Contribution ##########################################################
#########################################################################################################################

# select top 3 for contribution
contribution = df[(df['time'] == 2017) & (df['firmage'] == '0-1 years')] \
    .reset_index(drop=True).sort_values(by='contribution', ascending=False).reset_index(drop=True)
contribution = contribution[['fips', 'time', 'contribution']]

# filter original df for contribution top 3
contribution_plot = df[(df.fips == 'Nashville-Davidson--Murfreesboro--Franklin, TN') | (df.fips == 'Riverside-San Bernardino-Ontario, CA') |\
                       (df.fips == 'Los Angeles-Long Beach-Anaheim, CA')].reset_index(drop=True)
contribution_plot = contribution_plot[(contribution_plot.firmage == '0-1 years')].reset_index(drop=True)

# create pivot table to plot
contribution_plot = contribution_plot.pivot_table(index=['time'], columns='fips', values='contribution').reset_index()

# plot it
contribution_plot.plot(x='time', y=['Los Angeles-Long Beach-Anaheim, CA', 'Nashville-Davidson--Murfreesboro--Franklin, TN', 'Riverside-San Bernardino-Ontario, CA'])
plt.title("\n".join(wrap("Contribution: Top 3 Regions in 2017 over Time", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.15])
plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/hm_draft/plots/contribution_top3.png')
plt.show()

#########################################################################################################################
################################################# Compensation ##########################################################
#########################################################################################################################



# select top 3 for contribution
compensation = df[(df['time'] == 2017) & (df['firmage'] == '0-1 years')] \
    .reset_index(drop=True).sort_values(by='compensation', ascending=False).reset_index(drop=True)
compensation = compensation[['fips', 'time', 'compensation']]

# filter original df for contribution top 3
compensation_plot = df[(df.fips == 'Washington-Arlington-Alexandria, DC-VA-MD-WV') | (df.fips == 'Philadelphia-Camden-Wilmington, PA-NJ-DE-MD') |\
                       (df.fips == 'New York-Newark-Jersey City, NY-NJ-PA')].reset_index(drop=True)
compensation_plot = compensation_plot[(compensation_plot.firmage == '0-1 years')].reset_index(drop=True)
# create pivot table to plot
compensation_plot = compensation_plot.pivot_table(index=['time'], columns='fips', values='compensation').reset_index()

# plot it
compensation_plot.plot(x='time', y=['Washington-Arlington-Alexandria, DC-VA-MD-WV', 'Philadelphia-Camden-Wilmington, PA-NJ-DE-MD', 'New York-Newark-Jersey City, NY-NJ-PA'])
plt.title("\n".join(wrap("Compensation: Top 3 Regions in 2017 over Time", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0, 4.5])
plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/hm_draft/plots/compensation_top3.png')
plt.show()

#########################################################################################################################
################################################# constancy ##########################################################
#########################################################################################################################



# select top 3 for contribution
constancy = df[(df['time'] == 2017) & (df['firmage'] == '0-1 years')] \
    .reset_index(drop=True).sort_values(by='constancy', ascending=False).reset_index(drop=True)
constancy = constancy[['fips', 'time', 'constancy']]

# filter original df for contribution top 3
constancy_plot = df[(df.fips == 'Nashville-Davidson--Murfreesboro--Franklin, TN') | (df.fips == 'Hartford-West Hartford-East Hartford, CT') |\
                       (df.fips == 'San Francisco-Oakland-Hayward, CA')].reset_index(drop=True)
constancy_plot = constancy_plot[(constancy_plot.firmage == '0-1 years')].reset_index(drop=True)
# create pivot table to plot
constancy_plot = constancy_plot.pivot_table(index=['time'], columns='fips', values='constancy').reset_index()

# plot it
constancy_plot.plot(x='time', y=['Nashville-Davidson--Murfreesboro--Franklin, TN', 'Hartford-West Hartford-East Hartford, CT', 'San Francisco-Oakland-Hayward, CA'])
plt.title("\n".join(wrap("Constancy: Top 3 Regions in 2017 over Time", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([.4, .7])
plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/hm_draft/plots/constancy_top3.png')
plt.show()

#########################################################################################################################
################################################# creation ##########################################################
#########################################################################################################################



# select top 3 for contribution
creation = df[(df['time'] == 2017) & (df['firmage'] == '0-1 years')] \
    .reset_index(drop=True).sort_values(by='creation', ascending=False).reset_index(drop=True)
creation = creation[['fips', 'time', 'creation']]

# filter original df for contribution top 3
creation_plot = df[(df.fips == 'Los Angeles-Long Beach-Anaheim, CA') | (df.fips == 'Austin-Round Rock, TX') |\
                       (df.fips == 'Nashville-Davidson--Murfreesboro--Franklin, TN')].reset_index(drop=True)
creation_plot = creation_plot[(creation_plot.firmage == '0-1 years')].reset_index(drop=True)

# create pivot table to plot
creation_plot = creation_plot.pivot_table(index=['time'], columns='fips', values='creation').reset_index()

# plot it
creation_plot.plot(x='time', y=['Los Angeles-Long Beach-Anaheim, CA', 'Austin-Round Rock, TX', 'Nashville-Davidson--Murfreesboro--Franklin, TN'])
plt.title("\n".join(wrap("Creation: Top 3 Regions in 2017 over Time", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([3, 12])
plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/hm_draft/plots/creation_top3.png')
plt.show()

#########################################################################################################################
################################################# q2_index ##########################################################
#########################################################################################################################



# select top 3 for contribution
q2_index = df[(df['time'] == 2017) & (df['firmage'] == '0-1 years')] \
    .reset_index(drop=True).sort_values(by='q2_index', ascending=False).reset_index(drop=True)
q2_index = q2_index[['fips', 'time', 'q2_index']]

# filter original df for contribution top 3
q2_index_plot = df[(df.fips == 'Washington-Arlington-Alexandria, DC-VA-MD-WV') | (df.fips == 'San Francisco-Oakland-Hayward, CA') |\
                       (df.fips == 'New York-Newark-Jersey City, NY-NJ-PA')].reset_index(drop=True)
q2_index_plot = q2_index_plot[(q2_index_plot.firmage == '0-1 years')].reset_index(drop=True)

# create pivot table to plot
q2_index_plot = q2_index_plot.pivot_table(index=['time'], columns='fips', values='q2_index').reset_index()

# plot it
q2_index_plot.plot(x='time', y=['Washington-Arlington-Alexandria, DC-VA-MD-WV', 'San Francisco-Oakland-Hayward, CA', 'New York-Newark-Jersey City, NY-NJ-PA'])
plt.title("\n".join(wrap("Jobs Q2 Index: Top 3 Regions in 2017 over Time", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([1, 1.25])
plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/hm_draft/plots/q2_index_top3.png')
plt.show()