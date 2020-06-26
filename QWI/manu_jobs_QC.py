# data obtained manually from https://ledextract.ces.census.gov/static/data.html
# unemployment rate from BLS series number LNS14000000: https://data.bls.gov/timeseries/LNS14000000

import pandas as pd
import os
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None


# US, state, AL counties, OK counties, UT counties,
jobs = pd.DataFrame()
for csv in os.listdir('/Users/hmurray/Desktop/Jobs_Indicators/data_check/qwi_pulls/'):
    print(csv)
    df = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/data_check/qwi_pulls/' + str(csv))
    jobs = jobs.append(df, sort=True)

# pull US values
us_denom = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/data_check/us_total.csv')

# subset
jobs = jobs[['geography', 'year', 'quarter', 'firmage', 'Emp', 'EmpEnd', 'EmpS', 'EmpTotal', 'FrmJbC', 'EarnBeg']]
us_denom = us_denom[['geography', 'year', 'quarter', 'firmage', 'EarnBeg']]

# groupby to sum quarters
jobs = jobs.groupby(['geography', 'year', 'firmage']).agg({'Emp': 'sum', 'EmpEnd':'sum', 'EmpS':'sum', 'EmpTotal':'sum', 'FrmJbC':'sum', 'EarnBeg':'sum'}).reset_index()
us_denom = us_denom.groupby(['geography', 'year', 'firmage']).agg({'EarnBeg':'sum'}).reset_index()

# groupby to sum age categories
Emp_total = jobs.groupby(['geography', 'year']).agg({'Emp': 'sum'})
EmpEnd_total = jobs.groupby(['geography', 'year']).agg({'EmpEnd': 'sum'})
EmpS_total = jobs.groupby(['geography', 'year']).agg({'EmpS': 'sum'})
EmpTotal_total = jobs.groupby(['geography', 'year']).agg({'EmpTotal': 'sum'})
FrmJbC_total = jobs.groupby(['geography', 'year']).agg({'FrmJbC': 'sum'})
EarnBeg_total = jobs.groupby(['geography', 'year']).agg({'EarnBeg': 'sum'}).reset_index()

# merge Emp
emps = jobs.merge(Emp_total, on=['geography', 'year'])
emps = emps[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd', 'EmpS', 'EmpTotal', 'FrmJbC', 'EarnBeg']]

# merge EmpEnd
EmpEnd = emps.merge(EmpEnd_total, on=['geography', 'year'])
EmpEnd = EmpEnd[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd_x', 'EmpEnd_y', 'EmpS', 'EmpTotal', 'FrmJbC', 'EarnBeg']]

# merge EmpS
emps_empSs = EmpEnd.merge(EmpS_total, on=['geography', 'year'])
emps_empSs = emps_empSs[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd_x', 'EmpEnd_y', 'EmpS_x', 'EmpS_y', 'EmpTotal', 'FrmJbC', 'EarnBeg']]

# merge EmpS
EmpTotal_EmpTotals = emps_empSs.merge(EmpTotal_total, on=['geography', 'year'])
EmpTotal_EmpTotals = EmpTotal_EmpTotals[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd_x', 'EmpEnd_y', 'EmpS_x', 'EmpS_y', 'EmpTotal_x', 'EmpTotal_y', 'FrmJbC', 'EarnBeg']]

# merge FrmJbC
emps_empSs_FrmJbC = EmpTotal_EmpTotals.merge(FrmJbC_total, on=['geography', 'year'])
emps_empSs_FrmJbC = emps_empSs_FrmJbC[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd_x', 'EmpEnd_y', 'EmpS_x', 'EmpS_y', 'EmpTotal_x', 'EmpTotal_y', 'FrmJbC_x', 'FrmJbC_y', 'EarnBeg']]

# merge payroll
emps_empSs_FrmJbC_EarnBeg = emps_empSs_FrmJbC.merge(EarnBeg_total, on=['geography', 'year'])
emps_empSs_FrmJbC_EarnBeg = emps_empSs_FrmJbC_EarnBeg[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd_x', 'EmpEnd_y', 'EmpS_x', 'EmpS_y', 'EmpTotal_x', 'EmpTotal_y', 'FrmJbC_x', 'FrmJbC_y', 'EarnBeg_x', 'EarnBeg_y']]

# get some unemp
pep = pd.read_excel('/Users/hmurray/Desktop/Jobs_Indicators/data_check/pep/us_pep.xlsx', skiprows=11)
pep['sum'] = (pep['Jan'] + pep['Feb'] + pep['Mar'] + pep['Apr'] + pep['May'] + pep['Jun'] + pep['Jul'] + pep['Aug'] + pep['Sep'] + pep['Oct'] + pep['Nov'] + pep['Dec']) / 12
pep['unemp_rate'] = 1 - (pep['sum']/100)
pep.rename(columns={'Year': 'year'}, inplace=True)
pep = pep[['year', 'unemp_rate']]

# merge pep
temp = emps_empSs_FrmJbC_EarnBeg.merge(pep, on=['year'])
data = us_denom.merge(temp, on=['year'])

# calculate indicators
data['contribution'] = (data['Emp_x'] + data['EmpEnd_x']) / (data['Emp_y'] + data['EmpEnd_y'])
data['compensation'] = (data['EarnBeg_x'] / data['EarnBeg'])
data['constancy'] = (data['EmpS_x'] / data['EmpTotal_x'])
data['creation'] = (data['FrmJbC_x'] / data['Emp_y'])

data = data[['geography_y', 'year', 'firmage_y', 'contribution', 'compensation', 'constancy', 'creation']]
print(data)
data.to_excel('/Users/hmurray/Desktop/Jobs_Indicators/data_check/jobs_qc_output/jobs_QC.xlsx', index=False)

sys.exit()
