# code was pulled from DataCamp: https://campus.datacamp.com/courses/importing-and-managing-financial-data-in-python/importing-financial-data-from-the-web?ex=5

import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader.data import DataReader
from datetime import date

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None

# Set start date
start = date(1968, 1, 1)

# Set series code
series = 'GOLDAMGBD228NLBM'
data_source = 'fred'

# Import the data
gold_price = DataReader(series, data_source, start=start)
print(gold_price.head(100))

# Inspect the price of gold
gold_price.info()

# Plot the price of gold
gold_price.plot(title='Price of Gold')

# Show the plot
plt.show()
pd. show_versions()