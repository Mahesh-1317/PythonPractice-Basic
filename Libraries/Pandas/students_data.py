import pandas as pd
import csv
import re

data = {
    'Name': ['Dr Octopus    ','Vecna','Dr    Octopus','   Sambha','Ve  cna'],
    'Age': [21,19,22,20,19],
    'Marks': [85,65,75,99,56],
    'City': ['Rom','Berlin','Tokyo','Berlin','Rom']
}

df = pd.DataFrame(data)
print(df)

print(df.shape)
print(df.head(2))
print(df.dtypes)
print(df.describe)      # Statisticsl summary

print()
#   Select column
print("df['Name']: \n", df['Name'])
print(df[['Name', 'Marks']])        #   Multiple DataFrames

print()
#   Filter rows
print(df[df['Marks'] >= 85])
print(df[df['City'] == 'Berlin'])

print()
print(df[ (df['Marks'] >= 75) & (df['City'] == 'Tokyo')])

def get_grade(x):
    if x >= 90:
        return 'A#'
    elif x >= 70:
        return 'B*'
    else:
        return 'C$'
    
df['Grade'] = df['Marks'].apply(get_grade)
print(df['Grade'])
print()
print(df)

#   Groupby
city_avg = df.groupby('City')['Marks'].mean()
age_avg = df.groupby('Name')['Age'].min()
print(city_avg)
print()
print(age_avg)

#   Read csv file
print()

df.to_csv('Libraries/Pandas/students.csv',index=False)
df2 = pd.read_csv("Libraries/Pandas/students.csv")

# Clean all string columns (Name, City, Grade etc.)
for col in df2.select_dtypes(include='object').columns:
    df2[col] = (
        df2[col]
        .str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)  # Remove special characters
        .str.replace(r'\s+', ' ', regex=True)            # Remove extra spaces
        .str.strip()                                     # Remove leading/trailing spaces
    )

print(df2)
df2.to_csv('Libraries/Pandas/clean_output.csv',index=False)