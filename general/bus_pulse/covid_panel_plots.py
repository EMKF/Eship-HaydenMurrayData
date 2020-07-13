# Original data downloaded from: https://portal.census.gov/pulse/data/#downloads

import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None


short_month = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
}
def date_format(x):
    return pd.to_datetime(x.str[-5: -2].map(short_month) + '-' + x.str[-7: -5].apply(lambda x: x if x[0] != '_' else '0' + x[-1]) + '-' + '2020')
df = pd.read_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/python/small_bus_pulse/clean_bus_pulse_data.xlsx').\
    assign(
        week_end=lambda x: date_format(x['WEEK']),
        outcome=lambda x: x['ESTIMATE_PERCENTAGE'].str.replace('%', '').astype(float)
    )



print(df.head())
for question in range(1, 16):
    sns.set_style("whitegrid")
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1)
    df_question = df.query('INSTRUMENT_ID == {}'.format(question))
    pd.plotting.register_matplotlib_converters()
    for group in df_question[['week_end', 'outcome', 'ANSWER_TEXT']].groupby('ANSWER_TEXT'):
        ax.plot(group[1]['week_end'], group[1]['outcome'], label=group[0])
    plt.legend()
    plt.title('{}'.format(df_question['QUESTION'].iloc[0]))
    # plt.title("\n".join(wrap(question, 50)))
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/python/small_bus_pulse/plots/pulse_survey_{question}.png'.format(question=question))
    # plt.show()


sys.exit()



