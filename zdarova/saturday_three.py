import pandas as pd
import sqlite3 as sql



df_table1 = pd.read_csv("Table1.csv")
df_table2 = pd.read_csv("Table2.csv")

merge_tables = df_table1.merge(df_table2, how="left", on="FellowshipID")

joining = df_table1.join(df_table2, on="FellowshipID", how="left", lsuffix="df_table1", rsuffix="df_table2")

print(merge_tables)
print(joining)

