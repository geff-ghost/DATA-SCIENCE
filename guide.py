import pandas as pd

df = pd.DataFrame(
    {
        'Name': [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth"
        ],
        "Age": [22, 35, 58],
        "Sex": ['male', 'male', 'female']
    }
)

ages = pd.Series([22, 35, 58], name="Age")

titanic = pd.read_csv("data/titanic.csv")

# titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)

# titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")

"""
-Getting data in to pandas from many diffrent file formats
or data sources is supported by read_* fuctions

-Exporting data out of pandas is provided by diffrent to_* methods

-The head/tail/info methods and the dtypes attribute are convenient
for a first check
"""

# titanic = pd.read_csv("data/titanic.csv")
# ages = titanic["Age"]

# age_sex = titanic[['Age', 'Sex']]
# print(age_sex.head())
# print(type(age_sex))
# print(age_sex.shape)

# above_35 = titanic[titanic['Age']>35]
# # print(above_35)

# # print(above_35.shape)

# print()
# class_23 = titanic[titanic['Pclass'].isin([2, 3])]
# # class_23 = titanic[(titanic['Pclass'] == 2) | (titanic['Pclass'] == 3)]
# """When combining multiple conditional statements, each condition must be
# surrounded by parenthesis()"""
# # print(class_23.sample(10))

# print()
# age_no_na = titanic[titanic['Age'].notna()]
# # print(age_no_na.shape)

# print()
# adult_names = titanic.loc[titanic['Age']>35, 'Name']
# # print(adult_names.head())

# print()
# # print(titanic.loc[[19, 27, 89, 56, 76], ['Name', 'Age', 'Sex']])

# print()
# print(titanic.iloc[9:25, 2:5])

# print()
# titanic.iloc[0:3, 3] = "anonymous"
# # print(titanic.iloc[:5, 3])

# """
# -When selecting subset of data, square brackets [] are used.

# -Inside these square brackets, you can use a single column/row label,
# a list of column/row labels, a slice of labels, a coditional expression or a colon

# -Use loc for label-based selection (using row/column names)

# -Use iloc for position-based selection (using table positions)

# -You can assign new values to a selection based on loc/iloc
# """


air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
print(air_quality)

