import pandas as pd

covid_df = pd.read_csv('italy-covid-daywise.csv')

# # Basic information about the data frame
# print(covid_df.info())

# print()

# # Statistical information
# print(covid_df.describe())

# print()

# # Columns in a data frame
# print(covid_df.columns)

# print()

# # Number of columns and rows
# print(covid_df.shape)

# Pandas format is similar to this
covid_data_dict = {
    'date': ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases': [144, 1365, 996, 95, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_test': [53541, 42583, 54395, None, None]
}

print(covid_data_dict['new_cases'])

print(covid_df['new_cases'][23])

print(covid_df['new_deaths'][45])

print(covid_df.at[34, 'new_tests'])

cases_df = covid_df[['date', 'new_cases']]
# print(cases_df)

covid_df_copy = covid_df.copy()

print(covid_df.loc[43])

print(covid_df.new_tests.first_valid_index())

print(covid_df.loc[13 : 16])
