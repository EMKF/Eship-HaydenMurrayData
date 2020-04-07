import jobseq
import json
from pandas.io.json import json_normalize
import os
import sys
import shutil
import xlrd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
from textwrap import wrap
from kauffman_data import bfs, pep

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None


COMPANY_NAME = 'IBM'

# Retrieve our auth token from JobsEQ using the jobseq module
token = jobseq.get_token()
#print("Auth Token Received:\n{0}".format(token))

# create the analytic parameters for running the 'RTI' analytic
analytic_id = 'fb9d934a-17db-4a9d-94d2-54a7c93b3a3d' # 'RTI Job Posts' analytic id

# analytic params that the 'RTI' analytic should be run with
analytic_params = {
    "region": {
        "code": 39,     # Region code '39' indicates the region of 'Ohio'
        "type": 4       # Region type '4' indicates that the region is a state
    },
    "filters": [{
        "type": "comp",     # Filter based on company
        "filterType": "contains", # Filter comparison type
        "key": COMPANY_NAME   # Company name to filter results for
    }],
    "timeframe": 90,     # Last 90 days
    "rawOnly": True
}

# Run the analytic via an API call and get its response
analytic_response = jobseq.run_analytic(token, analytic_id, analytic_params)

# print("Analytic Response Received:\n{0}".format(analytic_response))
df = pd.DataFrame((analytic_response['data']))
print(df)


sys.exit()

