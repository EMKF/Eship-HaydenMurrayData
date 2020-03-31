# data obtained manually from Rob Fairlie on 3.27.20 @ 12:29pm

import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None


# pull,
data = pd.read_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/RFairlie_deliverables/2019_KESE_data/Kauffman Indicators Data State 1996_2019_v3.xlsx', sheet_name='Rate of New Entrepreneurs')
print(data)