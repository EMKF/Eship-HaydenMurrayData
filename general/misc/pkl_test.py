import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
import numpy as np
import time
import sys
import joblib
top_decile = joblib.load('/Users/hmurray/Desktop/data/NETS/inequality/transition_probabilities/top_decile.pkl')
transition_matrix = joblib.load('/Users/hmurray/Desktop/data/NETS/inequality/transition_probabilities/transition_matrix.pkl')
print(' ')
print(top_decile)
print(' ')
print(transition_matrix)

