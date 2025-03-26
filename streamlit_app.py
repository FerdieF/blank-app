# prompt: berdasarkan data hasil_pemisahan_tahun.csv, buatlah grafik untuk menunjukkan alumni-alumni yang lulus pada tahun 2021 hingga 2024, supaya tahu berapa saja jumlah lulusan tiap tahun. Buatkan dalam streamlit

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Membaca file CSV
data = pd.read_csv('hasil_pemisahan_tahun.csv')

# Filter data untuk tahun 2021 hingga 2024
data_filtered = data[data['tahun_lulus'].between(2021, 2024)]

# Menghitung jumlah lulusan tiap tahun
jumlah_lulusan_per_tahun = data_filtered.groupby('tahun_lulus')['tahun_lulus'].count()

# Pastikan index tidak memiliki nama
jumlah_lulusan_per_tahun.index.name = None

# Membuat grafik batang
st.title('Jumlah Lulusan Alumni per Tahun')
st.bar_chart(jumlah_lulusan_per_tahun)

# Menampilkan data dalam tabel (opsional)
st.write('Data Lulusan:')
st.dataframe(data_filtered) 
