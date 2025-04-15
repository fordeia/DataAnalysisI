import pandas as pd

# Read the excel file
df = pd.read_excel(r"C:\Users\fordeia\Desktop\Spring2025\STT3850semII20242025\Data\Data_Cleaning.xlsx")

# Print the DataFrame
print(df)

# Delete rows where 'col1' is 'B'
df = df[df['Age'] == 999]
print(df)
