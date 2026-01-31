import pandas as pd

covid_df = pd.read_csv('italy-covid-daywise.csv')

# Basic information about the data frame
print(covid_df.info())

print()

# Statistical information
print(covid_df.describe())

print()

# Columns in a data frame
print(covid_df.columns)

print()

# Number of columns and rows
print(covid_df.shape)
