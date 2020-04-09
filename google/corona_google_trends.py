# pitrends code found here: https://pypi.org/project/pytrends/#interest-by-region

import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
import pytrends
from pytrends.request import TrendReq

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None



# connect to google
pytrends = TrendReq(hl='en-US', tz=360)




# 1) build payload daily searches
kw_list = ["Entrepreneurship", "new business"]

# .get_historical_interest
df = pytrends.get_historical_interest(kw_list, year_start=2018, year_end=2018, cat=0, geo='US', sleep=0)
print(df)



# # 2) country searches for "start a business"
# # build payload
# pytrends.build_payload(kw_list=["start a business"])
# # get .interest_by_region
# df = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
# print(df)
# # plot
# df.reset_index().plot(x="geoName", y="start a business", figsize=(120, 10), kind ="bar")



# # 3) today's top searches
# df = pytrends.trending_searches(pn="united_states")
# print(df)



# # 4) related searches
# df = pytrends.related_topics("startup")
# print(df)
