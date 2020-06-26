# data obtained manually from https://ledextract.ces.census.gov/static/data.html
# unemployment rate from BLS series number LNS14000000: https://data.bls.gov/timeseries/LNS14000000

# request to QC these MSAs:
# '47900': ['11', '24', '54', '51'], DC MSA, DC state, MD, WV, VA

# '47260': ['37', '51'],
# '41180': ['17', '29'],
# '39300': ['25', '44'],
# '38900': ['41', '53'],
# '35620': ['34', '36', '42'],
# '14460': ['25', '33'],
# '16740': ['37', '45'],
# '16980': ['17', '18', '55'],
# '17140': ['18', '21', '39'],
# '28140': ['20', '29'],
# '31140': ['18', '21'],
# '32820': ['05', '28', '47'],
# '33460': ['27', '55'],
# '37980': ['24', '34', '10', '42']

# state_abb_fips_codes_dic = {
#     'WA': '53', 'DE': '10', 'DC': '11', 'WI': '55', 'WV': '54', 'HI': '15',
#     'FL': '12', 'WY': '56', 'PR': '72', 'NJ': '34', 'NM': '35', 'TX': '48',
#     'LA': '22', 'NC': '37', 'ND': '38', 'NE': '31', 'TN': '47', 'NY': '36',
#     'PA': '42', 'AK': '02', 'NV': '32', 'NH': '33', 'VA': '51', 'CO': '08',
#     'CA': '06', 'AL': '01', 'AR': '05', 'VT': '50', 'IL': '17', 'GA': '13',
#     'IN': '18', 'IA': '19', 'MA': '25', 'AZ': '04', 'ID': '16', 'CT': '09',
#     'ME': '23', 'MD': '24', 'OK': '40', 'OH': '39', 'UT': '49', 'MO': '29',
#     'MN': '27', 'MI': '26', 'RI': '44', 'KS': '20', 'MT': '30', 'MS': '28',
#     'SC': '45', 'KY': '21', 'OR': '41', 'SD': '46'

import pandas as pd
import os
import sys
import requests
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# contribution: EMP(year, region, all age categories) / EMP(year, region, specific age categories)
# compensation: Payroll/ Payroll
# constancy: EmpS/Emp
# creation: FrmJbC/pep
#
# US, state, AL counties, OK counties, UT counties,
jobs = pd.DataFrame()
for csv in os.listdir('/Users/hmurray/Desktop/Jobs_Indicators/data_check/qwi_pulls/'):
    print(csv)
    df = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/data_check/qwi_pulls/' + str(csv))
    jobs = jobs.append(df, sort=True)

jobs = jobs[['geography', 'year', 'quarter', 'firmage', 'Emp', 'EmpEnd', 'EmpS', 'FrmJbC', 'EarnBeg']]
jobs = jobs.groupby(['geography', 'year', 'firmage']).agg({'Emp': 'sum', 'EmpEnd':'sum', 'EmpS':'sum', 'FrmJbC':'sum', 'EarnBeg':'sum'}).reset_index()

Emp_total = jobs.groupby(['geography', 'year']).agg({'Emp': 'sum'})
EmpEnd_total = jobs.groupby(['geography', 'year']).agg({'EmpEnd': 'sum'})
EmpS_total = jobs.groupby(['geography', 'year']).agg({'EmpS': 'sum'})
FrmJbC_total = jobs.groupby(['geography', 'year']).agg({'FrmJbC': 'sum'})
EarnBeg_total = jobs.groupby(['geography', 'year']).agg({'EarnBeg': 'sum'}).reset_index()
us_EarnBeg = EarnBeg_total.loc[EarnBeg_total['geography'] == 0]

# merge Emp
emps = jobs.merge(Emp_total, on=['geography', 'year'])
emps = emps[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd', 'EmpS', 'FrmJbC', 'EarnBeg']]

# merge EmpEnd
EmpEnd = emps.merge(EmpEnd_total, on=['geography', 'year'])
EmpEnd = EmpEnd[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd_x', 'EmpEnd_y', 'EmpS', 'FrmJbC', 'EarnBeg']]

# merge EmpS
emps_empSs = EmpEnd.merge(EmpS_total, on=['geography', 'year'])
emps_empSs = emps_empSs[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd_x', 'EmpEnd_y', 'EmpS_x', 'EmpS_y', 'FrmJbC', 'EarnBeg']]

# merge FrmJbC
emps_empSs_FrmJbC = emps_empSs.merge(FrmJbC_total, on=['geography', 'year'])
emps_empSs_FrmJbC = emps_empSs_FrmJbC[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd_x', 'EmpEnd_y', 'EmpS_x', 'EmpS_y', 'FrmJbC_x', 'FrmJbC_y', 'EarnBeg']]

# merge payroll
emps_empSs_FrmJbC_EarnBeg = emps_empSs_FrmJbC.merge(us_EarnBeg, on=['geography', 'year'])
emps_empSs_FrmJbC_EarnBeg = emps_empSs_FrmJbC_EarnBeg[['geography', 'year', 'firmage', 'Emp_x', 'Emp_y', 'EmpEnd_x', 'EmpEnd_y', 'EmpS_x', 'EmpS_y', 'FrmJbC_x', 'FrmJbC_y', 'EarnBeg_x', 'EarnBeg_y']]

# get some unemp
pep = pd.read_excel('/Users/hmurray/Desktop/Jobs_Indicators/data_check/pep/us_pep.xlsx', skiprows=11)
pep['sum'] = (pep['Jan'] + pep['Feb'] + pep['Mar'] + pep['Apr'] + pep['May'] + pep['Jun'] + pep['Jul'] + pep['Aug'] + pep['Sep'] + pep['Oct'] + pep['Nov'] + pep['Dec']) / 12
pep['unemp_rate'] = 1 - (pep['sum']/100)
pep.rename(columns={'Year': 'year'}, inplace=True)
pep = pep[['year', 'unemp_rate']]

# merge pep
data = emps_empSs_FrmJbC_EarnBeg.merge(pep, on=['year'])
print(data.head(100))
# calculate indicators
data['contribution'] = (data['Emp_x'] + data['EmpEnd_x']) / (data['Emp_y'] + data['EmpEnd_y'])
data['compensation'] = (data['EarnBeg_x'] / data['EarnBeg_y'])
data['constancy'] = (data['EmpS_x'] / data['EmpS_y'])
data['creation'] = (data['FrmJbC_x'] / data['Emp_y'])

data = data[['geography', 'year', 'firmage', 'contribution', 'compensation', 'constancy', 'creation']]
print(data)
data.to_excel('/Users/hmurray/Desktop/Jobs_Indicators/data_check/jobs_qc_output/jobs_QC.xlsx', index=False)

sys.exit()
