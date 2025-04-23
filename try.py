import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

# Generate a synthetic time series
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='MS')
values = np.random.randn(len(dates)) + np.arange(len(dates))
time_series_data = pd.DataFrame({'Date': dates, 'Value': values})
time_series_data.set_index('Date', inplace=True)

# Visualize the time series
plt.figure(figsize=(10, 6))
plt.plot(time_series_data['Value'], label='Time Series Data')
plt.title('Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Perform seasonal decomposition
decomposition = seasonal_decompose(time_series_data['Value'], model='additive', period=3)

# Plot the decomposed components
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(decomposition.observed, label='Observed')
plt.legend()
plt.subplot(4, 1, 2)
plt.plot(decomposition.trend, label='Trend')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(decomposition.seasonal, label='Seasonal')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(decomposition.resid, label='Residual')
plt.legend()

plt.tight_layout()
plt.show()

