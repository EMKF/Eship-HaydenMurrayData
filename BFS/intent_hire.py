import sys
import pandas as pd
from kauffman_data import bfs, pep
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.f' % x)
pd.options.mode.chained_assignment = None


# BFS
bfs = bfs.get_data(['BA_BA', 'BA_WBA', 'BA_CBA', 'BA_HBA', 'BF_SBF4Q', 'BF_SBF8Q'], 'us', 2005, annualize=True)

# Pep
pep = pep.get_data('us', 2005, 2019)
pep.rename(columns={"year": "time"},inplace=True)

# merge bfs and pep
data = pd.merge(bfs, pep, on=['time'])

# population adjustment
data['BF8Q_POP'] = (data['BF_SBF8Q']/data['population'])*100000
data['BF4Q_POP'] = (data['BF_SBF4Q']/data['population'])*100000
data['WBA_POP'] = (data['BA_WBA']/data['population'])*100000
data['CBA_POP'] = (data['BA_CBA']/data['population'])*100000
data['HBA_POP'] = (data['BA_HBA']/data['population'])*100000
data['BA_POP'] = (data['BA_BA']/data['population'])*100000
data['non_8QBF'] = ((data['BA_BA'] - data['BF_SBF8Q'])/data['population'])*100000

# share of BA
data['wba_share'] = (data['BA_WBA']/data['BA_BA'])*100
data['cba_share'] = (data['BA_CBA']/data['BA_BA'])*100
data['hba_share'] = (data['BA_HBA']/data['BA_BA'])*100

# share of 8Q formations that occured in 4Q
data['share_4Q'] = (data['BF_SBF4Q']/data['BF_SBF8Q'])*100

# actualization
data['8Q_act'] = (data['BF_SBF8Q']/data['BA_BA'])*100

# export the table to excel
data.to_excel('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/outputs/ba_bf_pop.xlsx', index=False)
print(data)


##########################################################################################################################################
####################################################### Plot 1 ###########################################################################
##########################################################################################################################################


# New Business Applications and New Employer Businesses
data.plot(x='time', y=['BA_BA', 'BF_SBF8Q'])
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.xlim(2005, 2019)
plt.ylabel('Count')
# plt.yticks(np.arange(0, 1150, step=100), rotation=45)
leg_1_labels = ['Business Applications', 'New Employer Businesses']
plt.legend(labels=leg_1_labels, loc=7)
title = ('Business Applications are Increasing & New Employer Businesses are Decreasing')
plt.title("\n".join(wrap(title, 50)))
plt.tight_layout()
plt.grid()
plt.savefig('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/outputs/ba_bf.png')
plt.show()



##########################################################################################################################################
####################################################### Plot 2 ###########################################################################
##########################################################################################################################################



# WBA/BA and BF/BA
data.plot(x='time', y=['wba_share', '8Q_act'])
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.xlim(2005, 2019)
plt.ylabel('Percent')
plt.yticks(np.arange(0, 40, step=5), rotation=45)
leg_2_labels = ['Share of business applications with intent to hire','Share of business applications that actually hire']
plt.legend(labels=leg_2_labels, loc=0)
title = ('The share of business applications that intend to hire declined faster than the share of business applications that went on to hire')
plt.title("\n".join(wrap(title, 75)))
plt.tight_layout()
plt.grid()
plt.savefig('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/outputs/wba&ba_bf&ba.png')
plt.show()



sys.exit()
