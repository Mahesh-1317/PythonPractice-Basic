import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats 

np.random.seed(42)
stu_hrs = np.random.uniform(2,10,60)
marks = stu_hrs * 8 + np.random.normal(0,10,60)
marks = np.clip(marks, 30, 100)
absent = 10 - stu_hrs + np.random.normal(0, 1, 60)

df = pd.DataFrame({'Study_Hours':stu_hrs,'Marks':marks,'Absent':absent})

corr_matrix = df.corr()
print(corr_matrix.round(3))

plt.figure(figsize=(6,4))
sns.heatmap(corr_matrix,annot=True, cmap='coolwarm',vmin=-1,vmax=1, fmt='.2f')
plt.title('Correlation Matrix'); plt.show()

#   Pearson correlation
print()
r, p_value = stats.pearsonr(stu_hrs,marks)
print(f'Study_Marks correlation: r={r:.3f}, p={p_value:.4f}')
print('Interpretation:', 'Strong positive' if r>0.7 else 'Moderate' if r>0.4 else 'Weak')