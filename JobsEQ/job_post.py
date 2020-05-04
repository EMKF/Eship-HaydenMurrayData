import jobseq
import os
import sys
import pandas as pd
import requests

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

COMPANY_NAME = 'Kauffman Foundation'

# Retrieve our auth token from JobsEQ using the jobseq module

token = jobseq.get_token(os.getenv('JOBSEQ_USERNAME'), os.getenv('JOBSEQ_PASSWORD'))

#print("Auth Token Received:\n{0}".format(token))

# create the analytic parameters for running the 'RTI' analytic
analytic_id = 'fb9d934a-17db-4a9d-94d2-54a7c93b3a3d' # 'RTI Job Posts' analytic id

# analytic params that the 'RTI' analytic should be run with

analytic_params = {
    "region": {
        "code": 0,     # Region code '39' indicates the region of 'Ohio'
        "type": 10       # Region type '4' indicates that the region is a state
    },
    "filters": [{
        "type": "comp",     # Filter based on company
        "filterType": "contains", # Filter comparison type
        "key": COMPANY_NAME   # Company name to filter results for
    }],
    "timeframe": 7,     # Last 90 days
    "rawOnly": True
}

# Run the analytic via an API call and get its response
analytic_response = jobseq.run_analytic(token, analytic_id, analytic_params)

# print("Analytic Response Received:\n{0}".format(analytic_response))
df = pd.DataFrame((analytic_response['data']))
print(df)

def _region_type_dict():
    request_url = 'http://jobseq.eqsuite.com/api/external/regiontypes'
    request_headers = {
        "Authorization": 'Bearer {}'.format(token),
        "Content-Type": "application/json"
    }
    r = requests.get(request_url, headers=request_headers)
    return {l['id']: l['name'] for l in r.json()}


request_url = 'http://jobseq.eqsuite.com/api/external/regions'
request_headers = {
    "Authorization": 'Bearer {}'.format(token),
    "Content-Type": "application/json"
}
r = requests.get(request_url, headers=request_headers)
params = pd.DataFrame(r.json()).\
    rename(columns=
    {
        'g': 'fips',
        'sid': 'state_fips',
        'd': 'name',
        't': 'region_type',
        'c': 'region_code',
    }
)
    # assign(region_type=lambda x: x['region_type'].map(_region_type_dict()))
print(params.head(100))

sys.exit()

