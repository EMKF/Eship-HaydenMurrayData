import pandas as pd


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)




# # BRIEF2 - Regulations and Profitability - pull .dta and export xlsx
# df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_regs_profitability/SE1600CSCB32.dat', sep='|', low_memory=False)
# df.to_excel('/Users/hmurray/Desktop/data/ASE/ASE_regs_profitability/regulations_business_profitability.xlsx', index=False)
#
#
#
# # BRIEF3 - Business Profitability - pull .dta and export xlsx
# df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_bus_profitability/SE1600CSCB12.dat', sep='|', low_memory=False)
# df.to_excel('/Users/hmurray/Desktop/data/ASE/ASE_bus_profitability/business_profitability.xlsx', index=False)
#
#
#
# # BRIEF4 - funding and capital - pull .dta and export xlsx
#     # funding
# df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_funding_capital/conversions/funding/SE1600CSCB09.dat', sep='|', low_memory=False)
# df.to_excel('/Users/hmurray/Desktop/data/ASE/ASE_funding_capital/funding/funding.xlsx', index=False)
#     # capital source
# df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_funding_capital/conversions/capital/SE1600CSCB07.dat', sep='|', low_memory=False)
# df.to_excel('/Users/hmurray/Desktop/data/ASE/ASE_funding_capital/capital/source_capital.xlsx', index=False)
#     # capital amount
# df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_funding_capital/capital/SE1600CSCB08.dat', sep='|', low_memory=False)
# df.to_excel('/Users/hmurray/Desktop/data/ASE/ASE_funding_capital/capital/amuount_capital.xlsx', index=False)
#


# # BRIEF 5
# # ASE, Table SE1600CSA04 - "Sector, Gender, Ethnicity, Race, Veteran States, and Employment Size Firm" (Under Company Summary)
# df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_5/SE1600CSA04.dat', sep='|', low_memory=False)
# print(df.head(100))
# df.to_csv('/Users/hmurray/Desktop/data/ASE/ASE_5/ase_5.csv', index=False)

# ASE, Table SE1600CSA04 - "Owner Born a Citizen of the United States" (Under Characteristics of Bus Owners)
df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_5/SE1600CSCBO09.dat', sep='|', low_memory=False)
print(df.head(100))
df.to_csv('/Users/hmurray/Desktop/data/ASE/ASE_5/ase_5.2.csv', index=False)
#
#

# ASE, Employment Size https://www.census.gov/data/tables/2016/econ/ase/allcompanytables.html
df = pd.read_csv('/Users/hmurray/Downloads/SE1600CSA04.dat', sep='|', low_memory=False)
print(df.head(100))
df.to_csv('/Users/hmurray/Desktop/data/presentation/data/ase_explorer.csv', index=False)

#
# # BRIEF 6 - - Table: "Owner Born a Citizen of the US" (under characteristics of business owners)
# df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_6/SE1600CSCBO09.dat', sep='|', low_memory=False)
# print(df.head(100))
# df.to_csv('/Users/hmurray/Desktop/data/ASE/ASE_6/ase_6.csv', index=False)
