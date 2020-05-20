import jobseq
import os
import sys
import pandas as pd
import requests

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
# print(params.head(100))

sys.exit()

