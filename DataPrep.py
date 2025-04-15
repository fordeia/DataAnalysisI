import pandas as pd

# Read the excel file
df = pd.read_excel(r"C:\Users\fordeia\Desktop\Spring2025\STT3850semII20242025\Data\Data_Cleaning.xlsx")

# Print the DataFrame
print(df)

# Delete rows with impossible ages
#df.drop(df[df['Age'] == 999].index, inplace=True)
#print(df)
