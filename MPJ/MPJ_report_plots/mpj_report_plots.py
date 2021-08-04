import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

def data_create():
    # import MPJ download file
    df = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/new_data_7.1.21/mpj_download.csv')
    return df

def filterer(df):
    df = df[(df.name == 'United States')].reset_index(drop=True)
    df = df[df['category'] != 'Total'].reset_index(drop=True)
    return df

def harry_plotter(df, key, ylimmin, ylimmax):
    # plot US contribution/compensation/constance/creation aka 'x' for each category of bus age over time
    temp_df = df.pivot_table(index='year', columns='category', values=key).reset_index()
    print(temp_df)
    categories = ['Ages 0 to 1', 'Ages 2 to 3', 'Ages 4 to 5', 'Ages 6 to 10', 'Ages 11+']
    for cat in categories:
        temp_df.plot(x='year', y=cat)
        plt.xlabel('time')
        plt.xticks(rotation=45)
        plt.xlim(2004, 2019)
        plt.ylabel(key)
        plt.ylim(ylimmin, ylimmax)
        leg_1_labels = cat
        plt.legend(labels=leg_1_labels)
        title = (str(key) + ' for business ' + str(cat) + ' in the United States')
        plt.title("\n".join(wrap(title, 70)))
        plt.tight_layout()
        plt.grid()
        plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/qc_reviews/7.30.21_mpj_report_data_qc/plots/' + str(key) + str(cat) + 'US' + '.png')
        # temp_df.to_excel('/Users/hmurray/Desktop/Jobs_Indicators/qc_reviews/7.30.21_mpj_report_data_qc/plots' + str(key) + '.xlsx')
        # plt.show()
        # sys.exit()
    return df

#loop to do this for every indicator x out of contribution, compensation, constancy, and creation
if __name__ == '__main__':
    df = data_create()
    df = filterer(df)
    print(df)
    # variables = {'contribution', 'compensation': ((.55, 1.1)), 'constancy': ((.5, .8)), 'creation': ((-16, 7))}
    # for key in variables:
    df = harry_plotter(df, 'contribution', 0, .85)
    df = harry_plotter(df, 'compensation', .55, 1.1)
    df = harry_plotter(df, 'constancy', .5, .8)
    df = harry_plotter(df, 'creation', -16, 7)
