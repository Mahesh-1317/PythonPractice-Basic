import pandas as pd

data = {
    'Name': ['Pankaj','Alia','Ram','Kajal','Aman'],
    'Age': [21,19,22,20,19],
    'Marks': [85,65,75,99,56],
    'City': ['Rom','Berlin','Tokyo','Moscow','London']
}

df = pd.DataFrame(data)
print(df)

print(df.shape)
print(df.head(2))
print(df.dtypes)
print(df.describe)      # Statisticsl summary