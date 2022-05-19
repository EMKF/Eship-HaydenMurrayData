import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

def data_create():
    # read in precinct data and print head
    ball_df = pd.read_excel('/Users/hmurray/Desktop/search/murmuration/challenge/ADS_data_challenge/ballot_measure_poll.xlsx')
    print(ball_df.head())
    # inspect df for null and dtype
    print(ball_df.info())
    # create list of object columns and further inspect
    objects = ('support_initiative', 'region', 'county', 'education', 'ses', 'ethnicity', 'ideology', 'kids')
    for x in objects:
        print(ball_df[x].unique())
        # convert object columns to category
        ball_df[x] = ball_df[x].astype('category')
    # check to see if 'county' column was changed correctly
    print(ball_df.info())
    return ball_df

def correlations(df):
    # create fig big enough for corr matrix
    plt.figure(figsize=(16, 8))
    # create heatmap corr matrix
    sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
    # adjust plot layout and save locally
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/search/murmuration/challenge/ADS_data_challenge/outputs/plots/sect2_corr_matrix.png')
    plt.show()
    return df

if __name__ == '__main__':
    ball_df = data_create()
    ball_df = correlations(ball_df)
