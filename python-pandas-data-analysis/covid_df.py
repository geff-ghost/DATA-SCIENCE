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

# # Pandas format is similar to this
# covid_data_dict = {
#     'date': ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
#     'new_cases': [144, 1365, 996, 95, 1326],
#     'new_deaths': [1, 4, 6, 8, 6],
#     'new_test': [53541, 42583, 54395, None, None]
# }

# print(covid_data_dict['new_cases'])

# print(covid_df['new_cases'][23])

# print(covid_df['new_deaths'][45])

# print(covid_df.at[34, 'new_tests'])

# cases_df = covid_df[['date', 'new_cases']]
# # print(cases_df)

covid_df_copy = covid_df.copy()

# print(covid_df.loc[43])

# print(covid_df.new_tests.first_valid_index())

# print(covid_df.loc[13 : 16])

# Q: What is the total number of reported cases and deaths related
# to Covid 19 in Italy
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
# print(f"The total number of reported cases: '{total_cases}' and total reported deaths: '{total_deaths}'")

# Q: What is the overall death rate (ratio of reported deaths to reported cases)

death_ratio = covid_df.new_deaths.sum() / covid_df.new_cases.sum()

# print(f"The overall death ratio: '{death_ratio:.2f}'")

# Q: What is the overall number of tests conducted? A total of 935310 tests were conducted
# before daily test numbers were being reported

initial_tests = 935310
total_tests = covid_df.new_tests.sum() + initial_tests

# print(f"Total number of tests conducted in Italy: '{total_tests}'")

# Q: What fraction of test returned a positive result?

positive_rate = total_cases / total_tests

# print('{:.2f}% of tests in Italy led to a positive diagnosis'.format(positive_rate))

"Querying and Sorting rows"
high_new_cases = covid_df[covid_df.new_cases > 1000]
# print(high_new_cases)


high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate]
# print(high_ratio_df)

covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests

covid_df.drop(columns = ['positive_rate'], inplace = True)

# print(covid_df.sort_values('new_cases', ascending=False).head(10))
# print()
# print(covid_df.sort_values('new_deaths', ascending=False).head(10))
# print()
# print(covid_df.sort_values('new_cases').head(10))
# print(covid_df.loc[36: 40])

covid_df.at[38, 'new_cases'] = (covid_df.at[37, 'new_cases'] + covid_df.at[39, 'new_cases']) / 2
print(covid_df.at[38, 'new_cases'])

covid_df['date'] = pd.to_datetime(covid_df.date)

covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

# Query the rows for May
covid_df_may = covid_df[covid_df.month == 5]

# Extract the subset of columns to be aggregated
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]
# print(covid_df_may_metrics)

# Get the column-wise sum
covid_may_totals = covid_df_may_metrics.sum()

# Single operation statement
covid_may_totals = covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()
# print(covid_may_totals)

# Overall average
new_cases_mean = covid_df.new_cases.mean()
# print('New cases mean',new_cases_mean)

# Average for Sundays
sundays_mean = covid_df[covid_df.weekday == 6].new_cases.mean()
# print('Sunday mean: ', sundays_mean)

covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
print(covid_month_df)
print()

covid_weekday_df = covid_df.groupby('weekday')[['new_cases', 'new_deaths', 'new_tests']].mean()
print(covid_weekday_df)
print()

covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests

print(covid_df)

