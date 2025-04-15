import pandas as pd

# Read the excel file
df = pd.read_excel(r"C:\Users\fordeia\DataAnalysisI\Data_Cleaning.xlsx")

# Print the DataFrame
print(df)

# Delete rows with impossible ages
df_cleaned = df.drop(df[df['Age'] == 999].index, inplace=True)
print(df_cleaned)

#df_cleaned = df.dropna()
   # print(df_cleaned)
