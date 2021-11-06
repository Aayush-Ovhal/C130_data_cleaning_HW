import pandas as pd

df = pd.read_csv("test.csv")
print(df.shape)

del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
print(df.shape)

df.to_csv("final_cleaned_data.csv")