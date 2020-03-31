# data downloaded manually from: https://www.federalreserve.gov/consumerscommunities/shed_data.htm

import os
import sys
import time
import joblib
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns
import constants as c
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from matplotlib.collections import PatchCollection
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


def aff_extractor():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=c.filenamer('ase/chromedriver'), options=chrome_options)
    driver.get('https://factfinder.census.gov/bkmk/table/1.0/en/ASE/2016/00CSCBO11')

    time.sleep(3)
    # try:
    #     WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'dnld_btn')))
    # finally:
    #     driver.find_element_by_id('dnld_btn').click()

    driver.find_element_by_id('dnld_btn').click()
    driver.find_element_by_id('dnld_decision_use').click()
    driver.find_element_by_id('dnld_formats_single_file').click()
    driver.find_element_by_id('dnld_formats_include_desc').click()
    driver.find_element_by_id('yui-gen0-button').click()

    time.sleep(10)
    # element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Download')]")))    # I couldn't get this to work.
    driver.find_element_by_id('yui-gen2-button').click()

    WebDriverWait(driver, 120, 2).until(every_downloads_chrome)
    driver.close()
    extracted_files_list = _unzip()
    _move_file()
    _cleanup(extracted_files_list)

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var elements = document
        .querySelector('downloads-manager')
        .shadowRoot.querySelector('#downloadsList').items;
        if (elements.every(e => e.state === "COMPLETE"))
        return elements.map(elements =>elements.fileUrl || elements.file_url);
        """
    )

def _unzip():
    zip_filepath = '/Users/thowe/Downloads/ASE_2016_00CSCBO11.zip'
    z = zipfile.ZipFile(zip_filepath)
    z.extractall('/Users/thowe/Downloads')
    return z.namelist() + ['ASE_2016_00CSCBO11.zip']

def _move_file():
    old_filepath = '/Users/thowe/Downloads/ASE_2016_00CSCBO11.csv'
    new_filepath = c.filenamer('ase/data/ASE_2016_00CSCBO11.csv')
    os.rename(
        old_filepath,
        new_filepath
    )

def _cleanup(files_list):
    files_list.remove('ASE_2016_00CSCBO11.csv')
    for file in files_list:
        os.remove('/Users/thowe/Downloads/' + file)


