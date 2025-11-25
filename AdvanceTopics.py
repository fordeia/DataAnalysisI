########################################
# 1. IMPORT LIBRARIES
########################################
import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

########################################
# 2. DOWNLOAD BIRTHS DATA
########################################
url = "http://robjhyndman.com/tsdldata/data/nybirths.dat"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = StringIO(response.text)
    births = pd.read_csv(data, header=None).squeeze()  # now births exists
    print("Data loaded successfully")
else:
    raise Exception("Download failed:", response.status_code)

########################################
# 3. CREATE TIME SERIES
########################################
birthstimeseries = pd.Series(
    births.values,
    index=pd.date_range(start='1946-01', periods=len(births), freq='ME')  # month-end frequency
)
print(birthstimeseries.head())

########################################
# 4. PLOT TIME SERIES
########################################
plt.figure(figsize=(10,4))
plt.plot(birthstimeseries)
plt.title("Monthly Births in New York (1946 onwards)")
plt.xlabel("Year")
plt.ylabel("Number of Births")
plt.show()
