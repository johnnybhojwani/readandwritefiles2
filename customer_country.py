import pandas as pd
import numpy as np

df = pd.read_csv("customers.csv",usecols=["FirstName", "LastName", "Country"])
#print("Names and countries are:" )
#print(df)

df.to_csv("customer_country.csv", index=False)