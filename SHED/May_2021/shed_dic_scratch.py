import io
import sys
import requests
import pandas as pd
from zipfile import ZipFile
import scratch.constants as c
from kauffman.tools.etl import read_zip


def append1():
    df = pd.DataFrame()
    for year in range(2013, 2021):
        url = c.shed_dic[year]['zip_url']
        file = c.shed_dic[year]['filename']

        r = requests.get(url)
        z = ZipFile(io.BytesIO(r.content))
        df_temp = pd.read_csv(z.open(file), low_memory=False, encoding='cp1252')

        df = df.append(df_temp)
    return df


def transformation_func(df):
    # do stuff
    return df

def append2():
    return pd.concat(
        [
            read_zip(c.shed_dic[year]['zip_url'], c.shed_dic[year]['filename']).\
                assign(time=year).\
                rename(c.shed_dic[year]['col_name_dic']).\
                pipe(transformation_func)
            for year in range(2013, 2015)
        ]
    )


def main():
    # append1()
    df = append2()
    print(df.head())
    print(df.tail())

if __name__ == '__main__':
    main()
