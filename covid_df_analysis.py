import pandas as pd

covid_df = pd.read_csv('italy-covid-daywise.csv')


# Q1: What is the total number of reported cases and deaths related to Covid-19 in Italy
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()

print("The number of reported cases is {} and the number of reported deaths is {}".format(total_cases, total_deaths))

# Q2: What is the overall death rate(ratio of reported deaths to reported cases)
death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum()

print("The overall reported death rate in Italy is {:.2f}".format(death_rate))

# Q3: What is the overall number of tests conducted? A total of 93530 test were conducted befor daily
# test numbers were being reported
print(covid_df.new_tests.first_valid_index())
initial_tests = 93530
total_tests = initial_tests + covid_df.new_tests.sum()

print('Total tests conducted in Italy {}'.format(total_cases))

# Q4: What fraction of test returned a positive result?
positive_rate = total_cases / total_tests
print("{:.2f}% of tests in Italy led to a positive diagnosis.".format(positive_rate))