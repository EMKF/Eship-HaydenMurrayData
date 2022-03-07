# data downloaded from csv link at the bottom of this webpage: https://www.census.gov/econ/bfs/data.html
# csv link: https://www.census.gov/econ/bfs/csv/bfs_quarterly.csv
# pulling from Kauffman library

import sys
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib import pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# first tutorial: https://www.youtube.com/watch?v=cm03ir2Lews

# import data
df = pd.read_excel('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/2021/updated_data/covid_bfs_industry.xlsx')
print(df.head())
sys.exit()
# filter for dates and naics
df = df[(df['industry'] == 'All NAICS Sectors')]

# drop columns
df = df[['time', 'BA_BA']]

# drop NaN
df.dropna(axis=0, inplace=True)

# set index to time
df.set_index('time', inplace=True)
print(df.head())
print(df.index)
print(df.describe().transpose())

# check plot
df.plot()
plt.show()

# create time_series so we don't have to keep calling the column
time_series = df['BA_BA']
print(type(time_series))

# get rolling mean
time_series.rolling(12).mean().plot(label='12 month rolling mean')
time_series.rolling(12).std().plot(label='12 month rolling std')
time_series.plot()
plt.legend()
plt.show()

# check out ETS decomposition plot (error, trend, and seasonallity)
decomp = seasonal_decompose(time_series)
decomp.plot()
plt.show()


# second tutorial: https://www.youtube.com/watch?v=8FCDpFhd1zk

from statsmodels.tsa.stattools import adfuller

def ad_test(df):
    dftest = adfuller(df, autolag='AIC')
    print("1. ADF: ", dftest[0])
    print("2. P-Value: ", dftest[1])
    print("3. Num Of Lags: ", dftest[2])
    print("4. Num of Observations Used For ADF Regression and Critical Values Calculation: ", dftest[3])
    print("5. Critical Values: ")
    for key, val in dftest[4].items():
        print('\t',key, ": ", val)

def dicky_fuller_test(df):
    results = adfuller(df['BA_BA'])
    print(results)

def stationary_transformation(df):
    df_stationary = df.diff().dropna()
    df_stationary.plot()
    plt.show()
    return df_stationary

def ad_test(df_stationary):
    dftest = adfuller(df_stationary, autolag='AIC')
    print("1. ADF: ", dftest[0])
    print("2. P-Value: ", dftest[1])
    print("3. Num Of Lags: ", dftest[2])
    print("4. Num of Observations Used For ADF Regression and Critical Values Calculation: ", dftest[3])
    print("5. Critical Values: ")
    for key, val in dftest[4].items():
        print('\t',key, ": ", val)

def dicky_fuller_test(df_stationary):
    results = adfuller(df_stationary['BA_BA'])
    print(results)

def stepwisefit(df_stationary):
    stepwisefit = auto_arima(df_stationary['BA_BA'], trace=True, suppress_warnings=True)
    print(stepwisefit.summary())
    sys.exit()

def arima(df_stationary):
    print(df_stationary)
    print(df_stationary.shape)
    # assign train and test (video: 5:40)
    train = df_stationary.iloc[:-22]
    test = df_stationary.iloc[-22:]
    print(train.shape, test.shape)
    # fit the model
    model = ARIMA(train['BA_BA'], order=(5,0,0))
    model = model.fit()
    print(model.summary())
    # predict
    start = len(train)
    end = len(train) + len(test) - 1
    pred = model.predict(start=start, end=end)
    print(pred)
    pred.plot(label='Prediction', legend=True)
    test['BA_BA'].plot(label='Actual Business Applications', legend=True)
    plt.show()

if __name__ == '__main__':
    # # run tests on original df
    # ad_test(df['BA_BA'])
    # """ The p-value shows our dataset is NOT stationary """
    # dicky_fuller_test(df)


    """ Because the first item in the tuple above is negative, this also shows our dataset is NOT stationary """
    df_stationary = stationary_transformation(df)

    # rerun the tests with stationary dataset
    ad_test(df_stationary['BA_BA'])
    dicky_fuller_test(df_stationary)

    # import pmdarima
    from pmdarima import auto_arima
    import warnings
    warnings.filterwarnings("ignore")

    stepwisefit(df_stationary)

    # import arima and actually fit model
    from statsmodels.tsa.arima_model import ARIMA
    arima(df_stationary)



