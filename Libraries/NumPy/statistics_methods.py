import numpy as np

marks = np.array([[54,68,96], [87,42,36],[75,55,99]])
print(marks)

print(np.mean(marks))               # Overall mean
print(np.mean(marks, axis=1))       # Mean per student (row)
print(np.mean(marks, axis=0))       # Mean per student (column)
print(np.max(marks))                # Highest marks
print(np.std(marks))                # Standard Deviation