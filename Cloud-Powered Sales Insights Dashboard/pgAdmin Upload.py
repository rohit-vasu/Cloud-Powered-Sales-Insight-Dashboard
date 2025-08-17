import psycopg2
import pandas as pd

# === 1. Load your CSV ===
csv_file = "/Users/rohitvasu/Documents/sample_sales_data.csv"  # update path if needed
df = pd.read_csv(csv_file)
print("CSV Columns:", df.columns.tolist())
print(df.head())

# === 2. Connect to AWS RDS ===
conn = psycopg2.connect(
    host="database-2.c1kuaaw46aza.us-east-1.rds.amazonaws.com",
    dbname="postgres",      # ✅ your DB name (use postgres unless you created another)
    user="postgres",        # ✅ master username
    password="pejdyw-ziVgix-pezku5",  # 🔑 replace with your real password
    port=5432
)
cur = conn.cursor()

# === 3. Create table if it doesn’t exist ===
cur.execute("""
    CREATE TABLE IF NOT EXISTS sales_data (
        date DATE,
        product TEXT,
        region TEXT,
        units_sold INTEGER,
        unit_price NUMERIC,
        total_sales NUMERIC
    )
""")

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO sales_data (date, product, region, units_sold, unit_price, total_sales)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row['Date'],
        row['Product'],
        row['Region'],
        int(row['Units Sold']),
        float(row['Unit Price']),
        float(row['Total Sales'])
    ))


conn.commit()
cur.close()
conn.close()

print("✅ Data uploaded successfully to RDS!")
