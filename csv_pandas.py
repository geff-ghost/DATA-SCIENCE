import pandas as pd

covid_df = pd.read_csv('italy-covid-daywise.csv')

print(type(covid_df))
print()

print(covid_df)
print()

print(covid_df.info())
print()

print(covid_df.describe())
print()

print(covid_df.columns)
print()

print(covid_df.shape)
