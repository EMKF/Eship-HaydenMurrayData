import pandas as pd
import sys
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# read in data
df = pd.read_csv('/Users/hmurray/Desktop/data/EPOP/survey_documentation/s3_final_epop_dataset.csv', low_memory=False)

# spot check
df = df[['POP_2', 'Q59_11',]]
df = df.query('POP_2 == 1')
print(df.head())

# for x in range(1, 10):
#     df = df[['POP_' + x]]
# print(df.head())

sys.exit()

df = df[['POP_1', 'POP_2', 'POP_3', 'POP_4', 'POP_5', 'POP_7', 'POP_8', 'POP_9',
         'B1Q24', 'B1Q25', 'B1Q26', 'B1Q27', 'B1Q28', 'B1Q29', 'B1Q30', 'B1Q31', 'B1Q32', 'B1Q33', 'B1Q34', 'B1Q35',
         'B2Q36', 'B2Q37', 'B2Q38', 'B2Q39', 'B2Q40', 'B2Q41', 'B2Q42', 'B2Q43', 'B2Q44', 'B2Q45', 'B2Q46', 'B2Q47',
         'Q22_1', 'Q22_2', 'Q22_3', 'Q22_4', 'Q22_5', 'Q22_6', 'Q22_7', 'Q22_8', 'Q22_9', 'Q22_10', 'Q22_11',
         'Q23_1', 'Q23_2', 'Q23_3', 'Q23_4', 'Q23_5', 'Q23_6', 'Q23_7', 'Q23_8', 'Q23_9', 'Q23_10', 'Q23_11', 'Q23_12', 'Q23_13',
         'B13Q225', 'B13Q226', 'B13Q227', 'B13Q228', 'B13Q229', 'B13Q230', 'B13Q231', 'B13Q232', 'B13Q233', 'B13Q234', 'B13Q235', 'B13Q236',
         'Q48_1', 'Q48_2', 'Q48_3', 'Q48_4', 'Q48_5', 'Q48_6', 'Q48_7', 'Q48_8', 'Q48_9', 'Q48_10', 'Q48_11', 'Q48_12', 'Q48_13', 'Q48_14', 'Q48_15', 'Q48_16', 'Q48_17']]
# print(df.head())

# subset for entrepreneurs less than 5
ent_less_5 = df.query('POP_4 == 1').drop(['POP_1', 'POP_2', 'POP_3', 'POP_5', 'POP_7', 'POP_8', 'POP_9'], axis=1).reset_index()
print(ent_less_5.head())

# subset for entrepreneurs more than 5
ent_more_5 = df.query('POP_5 == 1').drop(['POP_1', 'POP_2', 'POP_3', 'POP_4', 'POP_7', 'POP_8', 'POP_9'], axis=1).reset_index()
print(ent_more_5.head())


# print(str('POP_') + str(range(1, 3)))


sys.exit()