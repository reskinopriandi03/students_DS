import pandas as pd
from sqlalchemy import create_engine

# === Load CSV ===
df = pd.read_csv('dataset.csv')

# === Ganti dengan database URL dari Supabase ===
DATABASE_URL = "postgresql://postgres.cobvjbvizfxiddtrkuvl:submissionAkhir@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

# Buat koneksi engine
engine = create_engine(DATABASE_URL)

# Simpan ke Supabase sebagai tabel baru (akan menimpa jika sudah ada)
df.to_sql('submissonAkhirTable', engine, index=False, if_exists='replace')

print("✅ Data dari dataset.csv berhasil diunggah ke Supabase.")
