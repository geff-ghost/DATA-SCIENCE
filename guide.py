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

print(df['Age'].max())
print(ages.max())

titanic = pd.read_csv("data/titanic.csv")

titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)

titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")

print(titanic.info())



