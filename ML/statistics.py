import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats     #   open source Python library used for scientific, mathematical,

salaries = [22,25,28,60,74,80,54,52,36,73,45,55,21,33,64,67,65,74,81,20]

#   Centarl Tendency - where is the 'centre' of data?
mean = np.mean(salaries)
median = np.median(salaries)
mode = stats.mode(salaries,keepdims=True).mode[0]

print(f'Mean    (Average):       Rs.{mean:.1f}K')
print(f'Median  (Middle Value):  Rs.{median:.1f}K')
print(f'Mode    (Most common):   Rs.{mode:.1f}K')
print()

#   Spread - how varied is the data?
std = np.std(salaries)              # Standard Deviation
var = np.var(salaries)              # Variance (std squared)
rng = max(salaries) - min(salaries) # Range
q1 = np.percentile(salaries,25)     # 25th percentile   
q3 = np.percentile(salaries,75)     # 75th percentile   
iqr = q3 - q1                       # Interquartile range

print(f'Std Deviation: {std:.2f}K (most important spread measure)')
print(f'IQR: {iqr}K (Q1={q1}, Q3={q3})')
print()

#   Qutlier detection using IQR 
lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outliers = [x for x in salaries if x < lower or x > upper]
print(f'Outliers: {outliers}')