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

########################################
# 5. LOAD KINGS DATA
########################################
# URL for kings data
url = "http://robjhyndman.com/tsdldata/misc/kings.dat"
headers = {'User-Agent': 'Mozilla/5.0'}

# Download data
response = requests.get(url, headers=headers)
if response.status_code == 200:
    # skip first 3 lines (header)
    data_text = "\n".join(response.text.splitlines()[3:])
    data = StringIO(data_text)
    kings = pd.read_csv(data, header=None).squeeze()
    print("Kings data loaded successfully")
else:
    raise Exception("Download failed:", response.status_code)

########################################
# 6. CREATE KINGS TIME SERIES
########################################
kingstimeseries = pd.Series(kings.values)
print(kingstimeseries.head())

########################################
# 7. PLOT KINGS TIME SERIES
########################################
plt.figure(figsize=(10,4))
plt.plot(kingstimeseries)
plt.title("Kings Series")
plt.xlabel("Observation")
plt.ylabel("Value")
plt.show()
########################################
# 8. MOVING AVERAGE SMOOTHING (ORDER 3)
########################################
kingstimeseriesSMA3 = kingstimeseries.rolling(window=3, center=True).mean()

plt.figure(figsize=(10,4))
plt.plot(kingstimeseriesSMA3)
plt.title("Kings Series - Moving Average (Order 3)")
plt.xlabel("Observation")
plt.ylabel("Smoothed Value")
plt.show()

########################################
# 9. MOVING AVERAGE SMOOTHING (ORDER 8)
########################################
kingstimeseriesSMA8 = kingstimeseries.rolling(window=8, center=True).mean()

plt.figure(figsize=(10,4))
plt.plot(kingstimeseriesSMA8)
plt.title("Kings Series - Moving Average (Order 8)")
plt.xlabel("Observation")
plt.ylabel("Smoothed Value")
plt.show()
