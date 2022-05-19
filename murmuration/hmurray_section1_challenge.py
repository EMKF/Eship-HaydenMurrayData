import pandas as pd
import sys
from textwrap import wrap
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

def data_create():
    # read in precinct data and print head
    prec_df = pd.read_excel('/Users/hmurray/Desktop/search/murmuration/challenge/ADS_data_challenge/precinct_level_election_results.xlsx')
    print(prec_df.head())
    # inspect df for null and dtype
    print(prec_df.info())
    # further inspect county because of 'object' dtype
    print(prec_df['county'].unique())
    # convert 'county' column from object to category
    prec_df['county'] = prec_df['county'].astype('category')
    # check to see if 'county' column was changed correctly
    print(prec_df.info())
    return prec_df

def correlations(df):
    # create fig big enough for corr matrix
    plt.figure(figsize=(16, 8))
    # create heatmap corr matrix
    sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
    # adjust plot layout and save locally
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/search/murmuration/challenge/ADS_data_challenge/outputs/plots/sect1_corr_matrix.png')
    plt.show()
    return df

def dummy_create(x):
    # create dummies for county category
    x = pd.get_dummies(x, columns=['county'], prefix='', prefix_sep='')
    return x

def two_var_feat_imp(df, y_for_meas, y_against_meas):
    # create df for variables used to make classifications
    x = df.drop([y_for_meas, y_against_meas], axis=1).copy()
    # get dummy variables for county
    x = dummy_create(x)
    print(x.head())
    # create df for variables we want to predict
    y = df[[y_for_meas]].copy()
    print(y.head())
    # create test and train datsets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)
    # preprocess and scale variables
    ss = StandardScaler()
    x_train_scaled = ss.fit_transform(x_train)
    # initiate model
    model = LinearRegression()
    # fit model
    model.fit(x_train_scaled, y_train)
    # create df of importances
    importances = pd.DataFrame(data={
        'Attribute': x_train.columns,
        'Importance': model.coef_[0]
    })
    # sort importances
    importances = importances.sort_values(by='Importance', ascending=False)
    print(importances)
    # plot and save importances
    plt.bar(x=importances['Attribute'], height=importances['Importance'], color='#087E8B')
    plt.title('Feature importances obtained from coefficients estimating' + str(y_for_meas))
    plt.title("\n".join(wrap('Feature importances obtained from coefficients estimating ' + str(y_for_meas), 62)))
    plt.xticks(rotation='vertical')
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/search/murmuration/challenge/ADS_data_challenge/outputs/plots/feature_imp_' + str(y_for_meas) + '.png')
    plt.show()
    return df

def voter_turnout_feat_imp(df, y_turnout):
    # create df for variables used to make classifications
    x = df.drop([y_turnout], axis=1).copy()
    # get dummy variables for county
    x = dummy_create(x)
    print(x.head())
    # create df for variables we want to predict
    y = df[[y_turnout]].copy()
    print(y.head())
    # create test and train datsets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)
    # preprocess and scale variables
    ss = StandardScaler()
    x_train_scaled = ss.fit_transform(x_train)
    # initiate model
    model = LinearRegression()
    # fit model
    model.fit(x_train_scaled, y_train)
    # create df of importances
    importances = pd.DataFrame(data={
        'Attribute': x_train.columns,
        'Importance': model.coef_[0]
    })
    # sort importances
    importances = importances.sort_values(by='Importance', ascending=False)
    # plot and save importances
    plt.bar(x=importances['Attribute'], height=importances['Importance'], color='#087E8B')
    plt.title('Feature importances obtained from coefficients estimating' + str(y_turnout))
    plt.title("\n".join(wrap('Feature importances obtained from coefficients estimating ' + str(y_turnout), 62)))
    plt.xticks(rotation='vertical')
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/search/murmuration/challenge/ADS_data_challenge/outputs/plots/feature_imp_' + str(y_turnout) + '.png')
    plt.show()
    return df



if __name__ == '__main__':
    prec_df = data_create()
    prec_df = correlations(prec_df)
    prec_df = two_var_feat_imp(prec_df, 'precinct_votes_for_ballot_measure', 'precinct_votes_against_ballot_measure')
    prec_df = two_var_feat_imp(prec_df, 'precinct_votes_against_ballot_measure', 'precinct_votes_for_ballot_measure')
    prec_df = two_var_feat_imp(prec_df, 'precinct_registered_voters', 'precinct_total_ballots')
    prec_df = two_var_feat_imp(prec_df, 'precinct_total_ballots', 'precinct_registered_voters')
    prec_df = voter_turnout_feat_imp(prec_df, 'avg_turnout_score')
