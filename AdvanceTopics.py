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


########################################
# 10. DECOMPOSE BIRTHS TIME SERIES
########################################
from statsmodels.tsa.seasonal import seasonal_decompose

birthstimeseriescomponents = seasonal_decompose(
    birthstimeseries,
    model='additive',
    period=12
)


########################################
# 11. PRINT SEASONAL, TREND, RANDOM COMPONENTS
########################################
print("Seasonal Component:\n", birthstimeseriescomponents.seasonal)
print("\nTrend Component:\n", birthstimeseriescomponents.trend)
print("\nRandom Component:\n", birthstimeseriescomponents.resid)


########################################
# 12. PLOT OBSERVED, TREND, SEASONAL, RANDOM
########################################
fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)

# Observed
axes[0].plot(birthstimeseries, label="Observed", color="black")
axes[0].set_title("Observed")
axes[0].set_ylabel("Births")

# Trend
axes[1].plot(birthstimeseriescomponents.trend, label="Trend", color="blue")
axes[1].set_title("Trend")
axes[1].set_ylabel("Value")

# Seasonal
axes[2].plot(birthstimeseriescomponents.seasonal, label="Seasonal", color="green")
axes[2].set_title("Seasonal")
axes[2].set_ylabel("Value")

# Random / Residual
axes[3].plot(birthstimeseriescomponents.resid, label="Random", color="red")
axes[3].set_title("Random (Residual)")
axes[3].set_ylabel("Value")
axes[3].set_xlabel("Time")

plt.tight_layout()
plt.show()
########################################
# 13. Seasonal Decomposition (Additive)
########################################
from statsmodels.tsa.seasonal import seasonal_decompose

decomp = seasonal_decompose(
    birthstimeseries,
    model='additive',
    period=12
)

seasonal = decomp.seasonal
trend = decomp.trend
resid = decomp.resid

########################################
# 14. Seasonally Adjusted Series
########################################
births_seasonally_adjusted = birthstimeseries - seasonal

########################################
# 15. Plot: Seasonally Adjusted Series
########################################
plt.figure(figsize=(10,4))
plt.plot(births_seasonally_adjusted, label="Seasonally Adjusted")
plt.title("Seasonally Adjusted Births Time Series (Additive)")
plt.xlabel("Year")
plt.ylabel("Births")
plt.legend()
plt.show()

########################################
# 16. Load Rainfall Data (corrected index)
########################################
url = "http://robjhyndman.com/tsdldata/hurst/precip1.dat"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Skip the header line
    data_text = "\n".join(response.text.splitlines()[1:])

    # Read fixed-width file without header
    rain_df = pd.read_fwf(StringIO(data_text), header=None)

    # Flatten the dataframe into a 1D array
    rain_values = rain_df.values.flatten()

    # Convert to numeric and drop any non-numeric entries
    rain_values = pd.to_numeric(rain_values, errors='coerce')
    rain_values = rain_values[~pd.isna(rain_values)]

    # Create proper yearly index with 100 periods from 1813
    rain_index = pd.date_range(start='1813', periods=len(rain_values), freq='YE')

    # Make the series
    rain_series = pd.Series(rain_values, index=rain_index, name='Rainfall')

    # Print first and last 5 entries
    print("First 5 years:")
    print(rain_series.head())
    print("\nLast 5 years:")
    print(rain_series.tail())

else:
    raise Exception("Failed to download data")

########################################
# 17. Plot Rainfall Time Series
########################################
plt.figure(figsize=(12,6))
rain_series.plot(color='blue', linewidth=1)
plt.title('Annual Rainfall Time Series (1813–1912)')
plt.xlabel('Year')
plt.ylabel('Rainfall')
plt.grid(True)

# Extend x-axis to 1920
plt.xlim(pd.Timestamp('1813'), pd.Timestamp('1920'))

plt.show()
