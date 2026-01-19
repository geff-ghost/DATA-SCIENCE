import pandas as pd

covid_df = pd.read_csv('italy-covid-daywise.csv')

# print(type(covid_df))
# print()

# print(covid_df)
# print()

# print(type(covid_df))
# print()

# print(covid_df)
# print()

# print(covid_df.info())
# print()

# print(covid_df.describe())
# print()

# print(covid_df.columns)
# print()

# print(covid_df.shape)

# print(covid_df.info())
# print()

# print(covid_df.describe())
# print()

# print(covid_df.columns)
# print()

# print(covid_df.shape)

# Pandas format is similar to this
covid_data_dict = {
    'data': ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases': [1444, 1365, 996, 975, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_tests': [53541, 42583, 54395, None, None]
}

print(covid_data_dict['new_cases'])
# print(covid_df['new_tests'])

print(covid_df['new_cases'][13])

print(covid_df.at[10, 'new_deaths'])

print(type(covid_df.new_cases))

cases_df = covid_df[['date', 'new_cases']]
print(type(cases_df))

covid_df_copy = covid_df.copy()

print(covid_df.loc[16])
print(type(covid_df.loc[16]))

print(covid_df.at[0, 'new_tests'])
print(type(covid_df.at[0, 'new_tests']))

print(covid_df.new_tests.first_valid_index())

print(covid_df.loc[3 : 6])

print(covid_df.sample(5))
