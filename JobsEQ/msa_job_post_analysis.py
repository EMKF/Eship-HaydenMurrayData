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
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull in merged rti job postings and employer database file
df = pd.read_csv('s3://emkf.data.research/other_data/chmura/rti_databaseUSA_2020-07-08.csv')

# remove time from startDate
df['month_post_start'] = df['dateStart'].str[:7]
df['year_post_start'] = df['dateStart'].str[:4]

# convert startDate to DateTime
df['dateStart'] = pd.to_datetime(df['dateStart'])
df['month_post_start'] = pd.to_datetime(df['month_post_start'])
df['year_post_start'] = pd.to_datetime(df['year_post_start'])
print(df.head())

# plot distribution of job postings over time
print(df.query('year_established == 2019').query('year_post_start == 2020')['month_post_start'].value_counts().plot())
plt.title('Freq 2020 Online Job Postings for Companies Founded in 2019')
plt.show()

# TO DO - how does histogram based on year_established relate to distribution from survival data?
df['year_established'].plot.hist(bins=50)
# plt.title('Distribution of year_established for Companies in MSA Employer Job Postings Dataset')
plt.title("\n".join(wrap("Distribution of year_established for Companies in MSA Employer Job Postings Dataset", 50)))
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/year_est_hist.png')
plt.show()


# survivor data
def _format_covars1(df):
    return df.assign(
            net_change=lambda x: x['net_change'].str.replace(',', ''),
            total_gains=lambda x: x['total_gains'].str.replace(',', ''),
            gross_job_gains_expanding_ests=lambda x: x['gross_job_gains_expanding_ests'].str.replace(',', ''),
            gross_job_gains_opening_ests=lambda x: x['gross_job_gains_opening_ests'].str.replace(',', ''),
            total_losses=lambda x: x['total_losses'].str.replace(',', ''),
            gross_job_losses_contracting_ests=lambda x: x['gross_job_losses_contracting_ests'].str.replace(',', ''),
            gross_job_losses_closing_ests=lambda x: x['gross_job_losses_closing_ests'].str.replace(',', ''),
        ).\
        astype(
            {
                'year': 'int',
                'net_change': 'int',
                'total_gains': 'int',
                'gross_job_gains_expanding_ests': 'int',
                'gross_job_gains_opening_ests': 'int',
                'total_losses': 'int',
                'gross_job_losses_contracting_ests': 'int',
                'gross_job_losses_closing_ests': 'int',
            }
        )


def table1():
    url = 'https://www.bls.gov/bdm/us_age_naics_00_table1.txt'

    lines = requests.get(url).text.split('\n')

    cohort = 1994
    age = 1
    data_lst = []
    for ind, line in enumerate(lines[9:-2]):
        if 'Less than one year' in line:
            data_lst.append([cohort] + ['age 0'] + line.split()[-7:])
        if 'Born before March' in line:
            data_lst.append([cohort] + ['pre 1993'] + line.split()[-7:])
        if 'Total' in line:
            data_lst.append([cohort] + ['total'] + line.split()[-7:])
            cohort += 1
            age = 1
        if '{} year'.format(age) in line:
            data_lst.append([cohort] + ['age {}'.format(age)] + line.split()[-7:])
            age += 1

    return pd.DataFrame(
            data_lst,
            columns=['year', 'age', 'net_change', 'total_gains', 'gross_job_gains_expanding_ests', 'gross_job_gains_opening_ests', 'total_losses', 'gross_job_losses_contracting_ests', 'gross_job_losses_closing_ests']
        ).\
        pipe(_format_covars1)


def _to_float(x):
    try:
        return float(x)
    except:
        return np.nan


def _format_covars7(df):
    return df.assign(
            establishments=lambda x: x['establishments'].str.replace(',', ''),
            employment=lambda x: x['employment'].str.replace(',', ''),
            survival_previous_year=lambda x: x['survival_previous_year'].str.replace('_', '').apply(_to_float),  # I have no idea why I can't "astype" this column
        ).\
        astype(
            {
                'year': 'int',
                'establishments': 'int',
                'employment': 'int',
                'survival_since_birth': 'float',
            }
        )


def table7_ingest():
    url = 'https://www.bls.gov/bdm/us_age_naics_00_table7.txt'

    lines = requests.get(url).text.split('\n')

    cohort = 1994
    data_lst = []
    for ind, line in enumerate(lines[11:-2]):
        if (not line.split()) or ('openings' in line) or ('ended' in line):
            continue
        data_lst.append([cohort] + line.split()[1:])
        if 'March 2019' in line:
            cohort += 1

    return pd.DataFrame(
            data_lst,
            columns=['cohort_year', 'year', 'establishments', 'employment', 'survival_since_birth', 'survival_previous_year', 'average_emp']
        ).\
        pipe(_format_covars7).\
        assign(age=lambda x: x['year'] - x['cohort_year'])


def harry_plotter(df):
    df.to_csv('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/tab7bls_survival.csv', index=False)
    df.query('age <= 10', inplace=True)
    print(df.head())

    sns.set_style("whitegrid", {'axes.grid': False})
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1)
    for year in range(1994, 2010, 5):
        df_temp = df.query('cohort_year == {}'.format(year))
        ax.plot(df_temp['age'], df_temp['survival_since_birth'], label='Cohort: {}'.format(year))
    plt.legend()
    plt.suptitle('Survival Since Birth Percentages, First Ten Years')
    plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/tab7bls_survival.png')
    plt.show()


if __name__ == '__main__':
    df = table1()
    print(df.info())
    print(df.head())
    table7_ingest().pipe(harry_plotter)

