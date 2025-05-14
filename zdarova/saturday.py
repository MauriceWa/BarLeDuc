import pandas as pd
import sqlite3 as sql

# highest pop country in 2010, top 5 countries

def display(user_input):
    print(user_input)


def reader():
    db = {}
    df = pd.read_excel("Country_Population_Data.xlsx")

    mask = df["Year"] == 2010
    # print(mask)
    # display(df[mask])
    df_highest_pop_countries_2010 = df[mask].sort_values(by="Population", ascending=False)
    display(df_highest_pop_countries_2010)
    df_highest_pop_countries_2010.to_csv("Highest Populated Countries 2010.csv", index=False)



reader()

