import sqlite3 as sql
import pandas as pd

# syntax for connecting with SQL
conn = sql.connect("my_database.db")

data = {
    "Name": ["john", "Bob", "Ashley"],
    "Age": [20, 19, 17],
    "Hobby": ["Fighting", "Netflix", "Scrolling"]
}

data2 = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', "Amy"],
    'age': [25, 30, 35, 40, 45],
    'salary': [50000, 60000, 70000, 80000, 90000]
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
# print(df)

#Writes the data to sql
df.to_sql("information", conn, if_exists="replace", index=False)
df2.to_sql("employee", conn, if_exists="replace", index=False)

# shows 25-30 and 30- 35 and 35-40 and above it all it should say above 40 and below 25
readerr = pd.read_sql("SELECT * FROM information WHERE Age >= 19", conn)
reader_employee = pd.read_sql("""
    SELECT
        CASE
            WHEN age < 25 THEN 'Under 25'
            WHEN age BETWEEN 25 AND 30 THEN '25-30'
            WHEN age BETWEEN 30 AND 35 THEN '30-35'
            WHEN age BETWEEN 35 AND 40 THEN '35-40'
            ELSE 'Over 40'
        END as age_group,
        AVG(salary) as avg_salary
    FROM employee
    GROUP BY age_group
""", conn)
print(reader_employee)

reading_excel = pd.read_excel("Country_Population_Data.xlsx")

reading_excel.to_sql("countries", conn, if_exists="replace", index=False)
reader_excel = pd.read_sql("SELECT * FROM countries WHERE Continent == 'Asia' ORDER BY Population DESC LIMIT 5  ", conn)
reader_excel2 = pd.read_sql("SELECT * FROM countries ORDER BY Population DESC LIMIT 3", conn)


# print(readerr)
# print('')
# print(reader_excel)
