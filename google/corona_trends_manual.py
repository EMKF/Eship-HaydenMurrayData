# data downloaded manually from: https://trends.google.com/trends/explore?date=all&geo=US&q=business%20loan

import sys
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None

df = pd.DataFrame
def puller(topic, folder, title, save):
    trends = {}
    for x in topic:
        trends[x] = pd.read_csv('/Users/hmurray/Desktop/data/google/google_data/pulls/' + str(folder) + str(x) + '.csv', skiprows=2)
        trends[x].columns = ["Week", x]
        # print(trends[x].head())
    df = {i: j.set_index('Week') for i, j in trends.items()}
    df = pd.concat(df, axis=1, sort=True).reset_index(drop=False)
    df.columns = df.columns.droplevel(1)
    print(df)
    df.to_excel('/Users/hmurray/Desktop/calc.xlsx')
    df.plot(x='Week', y=topic)
    plt.xlabel('Week')
    plt.xticks(rotation=45)
    plt.ylabel('Search Popularity Index')
    plt.legend(title='Search Terms')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(save)
    plt.show()

# names of searches/files that are pulled into each topic
new_bus_help = ['new_business_loan', 'small_business_help', 'new_business_grant']
new_bus_exit = ['close_new_business', 'new_business_shutdown', 'how_to_close_my_business']
new_bus_opportunity = ['open_a_business', 'new_self_employed', 'new_small_business', 'independent_contractor', 'how_to_work_for_yourself']


# call the function for each topic
puller(new_bus_help, 'new_bus_help/', 'Search Terms Related to New Business Help', '/Users/hmurray/Desktop/data/google/google_data/plots/new_bus_help.png')
puller(new_bus_exit, 'new_bus_exit/', 'Search Terms Related to New Business Exit', '/Users/hmurray/Desktop/data/google/google_data/plots/new_bus_exit.png')
puller(new_bus_opportunity, 'new_bus_opportunity/', 'Search Terms Related to New Business Opportunities', '/Users/hmurray/Desktop/data/google/google_data/plots/new_bus_opportunity.png')
sys.exit()




