import pandas as pd
import kauffman.constants as c
from kauffman.tools.etl import read_zip
import sys

def _col_names_lowercase(df):
    df.columns = df.columns.str.lower()
    return df


def _shed_data_create():
    return pd.concat(
        [
            read_zip(c.shed_dic[year]['zip_url'], c.shed_dic[year]['filename']). \
                pipe(_col_names_lowercase).\
                assign(
                    time=year,
                    fips=lambda x: x['ppstaten'].map(c.shed_state_codes).map(c.state_abb_fips_dic),
                    region=lambda x: x['ppstaten'].map(c.shed_state_codes).map(c.state_abb_name_dic),
                    e2=lambda x: x['e2'].map({-1: "refused", 0: "no", 1: "yes"}),
                    ppethm=lambda x: x['ppethm'].map({1: "White, Non‐Hispanic", 2: "Black, Non‐Hispanic", 3: "Other, Non‐Hispanic", 4: "Hispanic", 5: "2+ Races, Non‐Hispanic"}),
                    ppgender=lambda x: x['ppgender'].map({1: "Male", 2: "Female"})
                ). \
                rename(columns={"caseid": "id", "e2": "med_exp_12_months", "ppethm": "race_ethnicity", "ppage": "age", "ppgender": "gender"}) \
                [['id', 'time', 'fips', 'region', 'med_exp_12_months', 'race_ethnicity', 'age', 'gender']]
            for year in range(2013, 2021)
        ]
    )

if __name__ == '__main__':
    df = _shed_data_create()
    print(df.head())
    sys.exit()

    # if obs_level == 'us':
    #     return df.groupby(['time']).mean()
    # # to do - change all categorical variables to 0-1
    # # to do - add other aggregating functions? e.g. sum, mean
    # elif obs_level == 'individual':
    #     return df



    def shed(series_lst, obs_level='individual'):
        # def shed(series_lst, obs_level='individual', strata=[]):
        # def shed(obs_level='individual', demographic_lst, series_lst):
        """ Create a pandas data frame with results from a SHED query. Column order: fips, region, time, demographic_lst, series_lst.
        Keyword arguments:
            obs_level-- input for level of analysis
                values:
                    individual: respondent
                    us: aggregated to national level using population weights
            demographic_lst-- list of demographic variables to be pulled todo -
                Demographic variables:
                    gender: male, female
                    race_ethnicity: White, Non‐Hispanic, Black, Non‐Hispanic, Other, Non‐Hispanic, Hispanic, 2+ Races, Non‐Hispanic
                    age: continuous variable
            series_lst-- lst of variables to be pulled.
                Variables:
                    med_exp_12_months: 'During the past 12 months, have you had any unexpected major medical expenses that
                                        you had to pay out of pocket (that were not completely paid for by insurance)?'
                    man_financially: 'Which one of the following best describes how well you are managing financially these days?'
        todo
                - How to use the if-else-elif syntax to filter for region?
                        if type(obs_level) == list:
                            region_lst = obs_level
                        else:
                            if obs_level == 'us':
                                region_lst = ['US']
                            elif obs_level == 'state':
                                region_lst = c.states
                            else:
                                region_lst = ['US'] + c.states
                        --- pull other region variables for region (us, state, region1, region2)
                        --- create us level observation
                        --- will need to apply weights to get to the state, region, national level
                        --- create a function to aggregate based on weights
                - How do we want to handle the weights?
                - Do we want to filter for years?
                - What other inputs do we want?
                Tasks:
                1) get weight variable for final dataset
                    - look online for context about weights
                            - didn't find anything helpful
                            - don't think we can use 2013 or 2014 "sample weights"
                            - How do I concat each of the 3 datasets in _shed_data_create()?
                            - How do I pass inputs through _shed_data_create()?
                2) Aggregate to national, reigonal1, regional2, or state level:
                    - create a function in etl.py that allows users to specify the name of weight variable and observation level
                        e.g.
                            def survey_aggregate(df, weight_var, obs_level):
                                if obs_level == 'us':
                                #weighted average over all observations
                                elif obs_level == 'state':
                    - Use df.groupby('fips').mean() in the above function to get certain statistics
            """

        # if strata:
        #     if obs_level == 'individual':
        #         obs_level = 'us'

        # return _shed_data_create(obs_level, series_lst, strata)
        return _shed_data_create(obs_level, series_lst)

    # _shed_data_create(demographic_lst, series_lst)

    # def _shed_data_create(demographic_lst, series_lst):
    #     return pd.concat(
    #         [
    #             read_zip(c.shed_dic[year]['zip_url'], c.shed_dic[year]['filename']). \
    #                 pipe(_col_names_lowercase).\
    #                 assign(
    #                     time=year,
    #                     fips=lambda x: x['ppstaten'].map(c.shed_state_codes).map(c.state_abb_fips_dic),
    #                     region=lambda x: x['ppstaten'].map(c.shed_state_codes).map(c.state_abb_name_dic),
    #                     e2=lambda x: x['e2'].map({-1: "refused", 0: "no", 1: "yes"}),
    #                     b2=lambda x: x['b2'].map({-1: "refused", 1: "Finding it difficult to get by", 2: "Just getting by", 3: "Doing ok", 4: "Living comfortably"}),
    #                     ppethm=lambda x: x['ppethm'].map({1: "White, Non‐Hispanic", 2: "Black, Non‐Hispanic", 3: "Other, Non‐Hispanic", 4: "Hispanic", 5: "2+ Races, Non‐Hispanic"}),
    #                     ppgender=lambda x: x['ppgender'].map({1: "Male", 2: "Female", 'Male': "Male", "Female": "Female"})
    #                 ). \
    #                 rename(columns={"caseid": "id", "e2": "med_exp_12_months", "ppethm": "race_ethnicity", "ppage": "age", "ppgender": "gender", "b2": "man_financially"}) \
    #             [['fips', 'region', 'time',] + demographic_lst + series_lst]
    #             for year in range(2013, 2021)
    #         ]
    #     )
    #
