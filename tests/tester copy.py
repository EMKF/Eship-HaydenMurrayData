import sys
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import matplotlib.pyplot as plt
from textwrap import wrap
import kauffman.constants as c
from kauffman.data import acs, bfs, bds, pep, bed, qwi, shed

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 40000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

def col_names_type(df):
    return df['STEP2_Level_16-17'].astype(float)

def _col_names_lowercase(df):
    df = col_names_type(df)
    print(df.head())
    sys.exit()
    df.columns = df.columns.str.lower()
    return df

def _col_space_replace(df):
    char_dict = {' ': '_', '&': '', '-': ''}
    for k, v in char_dict.items():
        df.columns = df.columns.str.replace(k, v)
    return df

def _step_dictionary(df):
    df['level'] = df['f__p_reading_level'] + df.step_level.map(str)
    df = df.set_index('level').to_dict()['step_grade_level_equivalent']
    return df

def test(x):
    if x==x:
        return int(float(x))
    else:
        return x
    # print(x, isinstance(x, float), int(x))


def _col_step_combiner(df):
    # df.step2_level_1617.apply(test)
    # sys.exit()
    df['step1'] = df.step1_fp_1617.map(str) + df.step1_level_1617.map(str)
    # df['step2'] = df.step2_fp_1617.map(str) + df.step2_level_1617.map(str).apply(lambda x: int(x) if x==x else x)
    df['step2'] = df.step2_fp_1617.map(str) + df.step2_level_1617.map(str).apply(test)
    df['step3'] = df.step3_fp_1617.map(str) + df.step3_level_1617.map(str)
    df['step4'] = df.step4_fp_1617.map(str) + df.step4_level_1617.map(str)
    df['step5'] = df.step5_fp_1617.map(str) + df.step5_level_1617.map(str)
    df['current'] = df.current_fp_level.map(str) + df.current__step_level.map(str)
    return df

def _missing_valuer(df):
    df = df.replace('nannan', np.nan)
    # df['step2']= df['step2'].map(step_key)
    # df['step2_test'] = df.step2.map(step_key)
    print(df.head())
    sys.exit()
    return df


def step_key_creator():
    return pd.read_excel(
        '/Users/hmurray/Desktop/data/KS/data/Reading_Level_Performance_Task.xlsx',
        sheet_name='STEP_Grade_Level_Key',
        usecols="A:C"). \
        pipe(_col_names_lowercase). \
        pipe(_col_space_replace). \
        pipe(_step_dictionary)

def raw_data_create():
    return pd.read_excel(
                '/Users/hmurray/Desktop/data/KS/data/Reading_Level_Performance_Task.xlsx',
                sheet_name='Raw_STEP_Level_Data'
            ). \
                pipe(_col_names_lowercase). \
                pipe(_col_space_replace). \
                pipe(_col_step_combiner). \
                pipe(_missing_valuer). \
                assign(
                step1=lambda x: x['step1'].map(step_key),
                step2=lambda x: x['step2'].map(step_key),
                step3=lambda x: x['step3'].map(step_key),
                step4=lambda x: x['step4'].map(step_key),
                step5=lambda x: x['step5'].map(step_key),
                current=lambda x: x['current'].map(step_key),
            ). \
                rename(columns={"step1": "sept_19", "step2": "oct_19", "step3": "dec_19", "step4": "feb_20",
                        "step5": "april_20"}) \
        [['student', 'cohort', 'grade', 'reading_instructor', 'sept_19', 'oct_19', 'dec_19', 'feb_20', 'april_20', 'current']]

def grouper(df):
    # print(df.groupby('cohort', as_index=False)['sept_19', 'oct_19', 'dec_19', 'feb_20', 'april_20', 'current'].mean())
    print(df)





if __name__ == '__main__':
    # step_key = step_key_creator()
    df = raw_data_create()
    print(df.head())
    print(step_key)
    grouper(df)