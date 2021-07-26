import pandas as pd
import numpy as np

'''
Customer Number,Customer Name,2016,2017,Percent Growth,Jan Units,Month,Day,Year,Active
"10002.0",Quest Industries,"$125,000.00",$162500.00,30.00%,500,1,10,2015,"Y"
552278,Smith Plumbing,"$920,000.00","$101,2000.00",10.00%,700,6,15,2014,"Y"
23477,ACME Industrial,"$50,000.00",$62500.00,25.00%,125,3,29,2016,"Y"
24900,Brekke LTD,"$350,000.00",$490000.00,4.00%,75,10,27,2015,"Y"
651029,Harbor Co,"$15,000.00",$12750.00,-15.00%,Closed,2,2,2014,"N"


'''

df = pd.read_csv("https://github.com/chris1610/pbpython/blob/master/data/sales_data_types.csv?raw=True")
df['Customer Number'] = df['Customer Number'].astype('int')

def convert_currency(val):
    """
    125000.00
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)

def convert_percent(val):
    """
    Convert the percentage string to an actual floating point percent
    """
    new_val = val.replace('%', '')
    return float(new_val) / 100

df['2016'] = df['2016'].apply(convert_currency)
df['2017'] = df['2017'].apply(convert_currency)
df['Percent Growth'] = df['Percent Growth'].apply(convert_percent)
df["Jan Units"] = pd.to_numeric(df['Jan Units'], errors='coerce').fillna(0)
df["Start_Date"] = pd.to_datetime(df[['Month', 'Day', 'Year']])
df["Active"] = np.where(df["Active"] == "Y", True, False)

print(df.astype({'Customer Number': 'int', 'Customer Name': 'str'}).dtypes)
print(df)