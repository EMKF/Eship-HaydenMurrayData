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
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None


def phaser1():
    # pull data for Phase One, Two, and Three by looping over each url parameter
    p1dates = {'1': '26Apr20_2May20', '2': '3May20_9May20', '3': '10May20_16May20', '4': '17May20_23May20', '5': '24May20_30May20',\
              '6': '31May20_06Jun20', '7': '07Jun20_13Jun20', '8': '14Jun20_20Jun20', '9': '21Jun20_27Jun20'}
    pulse = pd.DataFrame()
    for key, value in p1dates.items():
        # pull in each df by looping over url for each week
        df = pd.read_excel('https://portal.census.gov/pulse/data/downloads/' + str(key) + '/national_sector_' + str(value) + '.xls', na_values='-')
        # rename columns in each df
        df.rename(columns={'NAICS_SECTOR': 'NAICS2'}, inplace=True)
        # drop rows that condition on industry
        df = df[pd.isnull(df['NAICS2'])].reset_index(drop=True)
        # create column that represents the week data was collected (value in dictionary)
        df['WEEK'] = value
        # concat question and answer columns
        df["ID"] = df["INSTRUMENT_ID"].astype(str) + ' - ' + df["ANSWER_ID"].astype(float).astype(str)
        # append each weekly df
        pulse = pulse.append(df, sort=True).reset_index(drop=True)
    # pull codebook
    phase1 = pd.read_excel('https://portal.census.gov/pulse/data/downloads/codebook_4_26.xls')
    phase1["ID"] = phase1["QUESTION_ID"].astype(str) + ' - ' + phase1["ANSWER_ID"].astype(str)
    # combine question - answer code column and merge
    p1 = pulse.merge(phase1, on='ID', how='left', indicator=True)
    # convert the estimate percentage to a float so you can export in a clean way
    p1['ESTIMATE_PERCENTAGE'] = p1['ESTIMATE_PERCENTAGE'].map(lambda x: x.rstrip('%'))
    p1['ESTIMATE_PERCENTAGE'] = p1['ESTIMATE_PERCENTAGE'].astype(float)
    # subset the dataframe
    p1 = p1[['WEEK', 'INSTRUMENT_ID', 'ID', 'QUESTION_TEXT', 'ANSWER_TEXT', 'ESTIMATE_PERCENTAGE']]
    # export xlsx for plots
    p1.to_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/2020_bus_pulse/phase1.xlsx',index=False)
    return p1

def phaser2():
    # pull data for Phase One, Two, and Three by looping over each url parameter
    p2dates = {'10': '09Aug20_15Aug20', '11': '16Aug20_22Aug20', '12': '23Aug20_29Aug20', '13': '30Aug20_05Sep20', '14': '06Sep20_12Sep20', '15': '13Sep20_19Sep20',\
              '16': '20Sep20_26Sep20', '17': '27Sep20_03Oct20', '18': '04Oct20_12Oct20'}
    pulse = pd.DataFrame()
    for key, value in p2dates.items():
        # pull in each df by looping over url for each week
        df = pd.read_excel('https://portal.census.gov/pulse/data/downloads/' + str(key) + '/national_sector_' + str(value) + '.xls', na_values='-')
        # rename columns in each df
        df.rename(columns={'NAICS_SECTOR': 'NAICS2'}, inplace=True)
        # drop rows that condition on industry
        df = df[pd.isnull(df['NAICS2'])].reset_index(drop=True)
        # create column that represents the week data was collected (value in dictionary)
        df['WEEK'] = value
        # concat question and answer columns
        df["ID"] = df["INSTRUMENT_ID"].astype(str) + ' - ' + df["ANSWER_ID"].astype(float).astype(str)
        # append each weekly df
        pulse = pulse.append(df, sort=True).reset_index(drop=True)
    # pull codebook
    phase2 = pd.read_excel('https://portal.census.gov/pulse/data/downloads/codebook_2020_08_10.xlsx')
    phase2.rename(columns={'QUESTION': 'QUESTION_TEXT'}, inplace=True)
    phase2["ID"] = phase2["QUESTION_ID"].astype(str) + ' - ' + phase2["ANSWER_ID"].astype(str)
    # combine question - answer code column and merge
    p2 = pulse.merge(phase2, on='ID', how='left', indicator=True)
    # convert the estimate percentage to a float so you can export in a clean way
    p2['ESTIMATE_PERCENTAGE'] = p2['ESTIMATE_PERCENTAGE'].map(lambda x: x.rstrip('%'))
    p2['ESTIMATE_PERCENTAGE'] = p2['ESTIMATE_PERCENTAGE'].astype(float)
    # subset the dataframe
    p2 = p2[['WEEK', 'INSTRUMENT_ID', 'ID', 'QUESTION_TEXT', 'ANSWER_TEXT', 'ESTIMATE_PERCENTAGE']]
    # export xlsx for plots
    p2.to_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/2020_bus_pulse/phase2.xlsx',index=False)
    return p2

def phaser3():
    # pull data for Phase One, Two, and Three by looping over each url parameter
    p3dates = {'19': '09Nov20_15Nov20', '20': '16Nov20_22Nov20'}
    pulse = pd.DataFrame()
    for key, value in p3dates.items():
        # pull in each df by looping over url for each week
        df = pd.read_excel('https://portal.census.gov/pulse/data/downloads/' + str(key) + '/national_sector_' + str(value) + '.xls', na_values='-')
        # rename columns in each df
        df.rename(columns={'NAICS_SECTOR': 'NAICS2'}, inplace=True)
        # drop rows that condition on industry
        df = df[pd.isnull(df['NAICS2'])].reset_index(drop=True)
        # create column that represents the week data was collected (value in dictionary)
        df['WEEK'] = value
        # concat question and answer columns
        df["ID"] = df["INSTRUMENT_ID"].astype(str) + ' - ' + df["ANSWER_ID"].astype(float).astype(str)
        # append each weekly df
        pulse = pulse.append(df, sort=True).reset_index(drop=True)
    # pull codebook
    phase3 = pd.read_excel('https://portal.census.gov/pulse/data/downloads/codebook_2020_08_10.xlsx')
    phase3.rename(columns={'QUESTION': 'QUESTION_TEXT'}, inplace=True)
    phase3["ID"] = phase3["QUESTION_ID"].astype(str) + ' - ' + phase3["ANSWER_ID"].astype(str)
    # combine question - answer code column and merge
    p3 = pulse.merge(phase3, on='ID', how='left', indicator=True)
    # convert the estimate percentage to a float so you can export in a clean way
    p3['ESTIMATE_PERCENTAGE'] = p3['ESTIMATE_PERCENTAGE'].map(lambda x: x.rstrip('%'))
    p3['ESTIMATE_PERCENTAGE'] = p3['ESTIMATE_PERCENTAGE'].astype(float)
    # subset the dataframe
    p3 = p3[['WEEK', 'INSTRUMENT_ID', 'ID', 'QUESTION_TEXT', 'ANSWER_TEXT', 'ESTIMATE_PERCENTAGE']]
    # export xlsx for plots
    p3.to_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/2020_bus_pulse/phase3.xlsx',index=False)
    return p3

if __name__ == '__main__':
    p1 = phaser1()
    p2 = phaser2()
    p3 = phaser3()


# append each of the 3 phases and create one large dataframe
temp = p1.append(p2, sort=True).reset_index(drop=True)
df = temp.append(p3, sort=True).reset_index(drop=True)

df['week_end'] = df['WEEK']
df['week_end'] = df['WEEK'].str.strip().str[8:15]
print(df.head(50))

# export the appended dataframe
df.to_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/2020_bus_pulse/all_phases.xlsx',index=False)

sys.exit()

# # create dict to recode survey weeks into a datatime variable
# short_month = {
#     'Jan': '01',
#     'Feb': '02',
#     'Mar': '03',
#     'Apr': '04',
#     'May': '05',
#     'Jun': '06',
#     'Jul': '07',
#     'Aug': '08',
#     'Sep': '09',
#     'Oct': '10',
#     'Nov': '11',
#     'Dec': '12'
# }
#
# #
# def date_format(x):
#     return pd.to_datetime(x.str[-5: -2].map(short_month) + '-' + x.str[-7: -5].apply(lambda x: x if x[0] != '_' else '0' + x[-1]) + '-' + '2020')
# df = pd.read_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/2020_bus_pulse/all_phases.xlsx').\
#     assign(week_end=lambda x: date_format(x['WEEK']), outcome=lambda x: x['ESTIMATE_PERCENTAGE']
#     )
#
#

# for question in range(1, 20):
#     sns.set_style("whitegrid")
#     fig = plt.figure(figsize=(12, 8))
#     ax = fig.add_subplot(1, 1, 1)
#     df_question = df.query('INSTRUMENT_ID == {}'.format(question))
#     pd.plotting.register_matplotlib_converters()
#     for group in df_question[['week_end', 'outcome', 'ANSWER_TEXT']].groupby('ANSWER_TEXT'):
#         ax.plot(group[1]['week_end'], group[1]['outcome'], label=group[0])
#     plt.legend()
#     plt.title('{}'.format(df_question['QUESTION_TEXT'].iloc[0]))
#     # plt.title("\n".join(wrap(question, 50)))
#     plt.grid()
#     plt.savefig('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/2020_bus_pulse/plots/pulse_survey_{question}.png'.format(question=question))
#     # plt.show()


