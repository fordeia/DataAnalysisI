########################################
# 1. IMPORT LIBRARIES
########################################
import pandas as pd
import requests
from io import StringIO

########################################
# 2. DEFINE DATA URL AND HEADERS
########################################
url = "http://robjhyndman.com/tsdldata/data/nybirths.dat"
headers = {'User-Agent': 'Mozilla/5.0'}

########################################
# 3. DOWNLOAD DATA FROM URL
########################################
response = requests.get(url, headers=headers)

########################################
# 4. CHECK RESPONSE AND LOAD DATA
########################################
if response.status_code == 200:
    data = StringIO(response.text)
    births = pd.read_csv(data, header=None).squeeze()
    print(births)
else:
    print("Download failed:", response.status_code)
