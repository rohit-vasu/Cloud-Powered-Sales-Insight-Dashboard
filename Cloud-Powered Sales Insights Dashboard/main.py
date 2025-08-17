import pandas as pd

# Load CSV from local (or directly from S3 if configured)
df = pd.read_csv("sample_sales_data.csv")

# Clean data
df['Date'] = pd.to_datetime(df['Date'])
df['Total Sales'] = df['Units Sold'] * df['Unit Price']

# Example: Aggregate sales by region
region_sales = df.groupby('Region')['Total Sales'].sum().reset_index()

print(region_sales)
