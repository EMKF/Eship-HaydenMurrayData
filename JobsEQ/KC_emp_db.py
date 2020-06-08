import pandas as pd
import sys
import numpy as np
import quantipy as qp

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# read in data
man = pd.read_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/emp_database/manuf_emp_list.xlsx', skiprows=1, skip_blank_lines=True)
acc_food = pd.read_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/emp_database/acc_food_serv_emp_list.xlsx', skiprows=1, skip_blank_lines=True)

# merge
df = man.append(acc_food, sort=False)

# export
df.to_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/emp_database/manuf_food_merge_emp_list.xlsx', index=False)

