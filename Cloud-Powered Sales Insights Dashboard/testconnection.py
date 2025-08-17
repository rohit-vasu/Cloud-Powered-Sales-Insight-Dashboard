import psycopg2

try:
    conn = psycopg2.connect(
        host="database-2.c1kuaaw46aza.us-east-1.rds.amazonaws.com",
        database="postgres",  # <-- Change this to your actual DB name
        user="postgres",
        password="pejdyw-ziVgix-pezku5",
        port=5432
    )
    print("✅ Connection successful!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
