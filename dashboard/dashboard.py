import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="E-Commerce Dashboard")

st.title("📊 E-Commerce Data Analysis Dashboard")

folder_path = '../data'  
all_files = os.listdir(folder_path)
csv_files = [file for file in all_files if file.endswith('.csv')]
data_list = [pd.read_csv(os.path.join(folder_path, file)) for file in csv_files]
combined_data = pd.concat(data_list, ignore_index=True)

combined_data['price'].fillna(combined_data['price'].median(), inplace=True)
combined_data['order_delivered_customer_date'].fillna('Unknown', inplace=True)
combined_data['order_status'].fillna('Unknown', inplace=True)
combined_data.dropna(thresh=len(combined_data.columns) * 0.5, inplace=True)

combined_data['order_purchase_timestamp'] = pd.to_datetime(combined_data['order_purchase_timestamp'])
combined_data['order_approved_at'] = pd.to_datetime(combined_data['order_approved_at'])
combined_data['order_delivered_customer_date'] = pd.to_datetime(combined_data['order_delivered_customer_date'], errors='coerce')

st.sidebar.header("Filter Data")
selected_category = st.sidebar.selectbox("Pilih Kategori Produk", combined_data['product_category_name'].dropna().unique())
filtered_data = combined_data[combined_data['product_category_name'] == selected_category]

col1, col2 = st.columns(2)

st.subheader("📈 Distribusi Harga Produk")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(combined_data['price'], kde=True, color='dodgerblue', ax=ax)
ax.set_xlabel("Harga")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

st.subheader("💰 Harga vs Skor Ulasan")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='review_score', y='price', data=combined_data, palette='Blues', ax=ax)
ax.set_xlabel("Skor Ulasan")
ax.set_ylabel("Harga")
st.pyplot(fig)

st.subheader("🚚 Rata-rata Waktu Pengiriman Berdasarkan Kode Pos Pelanggan")
combined_data['delivery_time'] = (combined_data['order_delivered_customer_date'] - combined_data['order_purchase_timestamp']).dt.days
delivery_by_zip = combined_data.groupby('customer_zip_code_prefix')['delivery_time'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='customer_zip_code_prefix', y='delivery_time', data=delivery_by_zip, palette='viridis', ax=ax)
ax.set_xlabel("Kode Pos Pelanggan")
ax.set_ylabel("Rata-rata Waktu Pengiriman (Hari)")
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
st.pyplot(fig)

st.subheader("📦 Harga Rata-rata per Kategori Produk")
category_price = combined_data.groupby('product_category_name')['price'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='price', y='product_category_name', data=category_price, palette='crest', ax=ax)
ax.set_xlabel("Harga Rata-rata")
ax.set_ylabel("Kategori Produk")
st.pyplot(fig)

st.subheader("💳 Total Pembayaran Berdasarkan Jenis Pembayaran")
payment_type_payment_value = combined_data.groupby('payment_type')['payment_value'].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='payment_type', y='payment_value', data=payment_type_payment_value, palette='Blues', ax=ax)
ax.set_xlabel("Jenis Pembayaran")
ax.set_ylabel("Total Pembayaran")
st.pyplot(fig)

st.subheader("📋 Data Berdasarkan Kategori Produk")
st.write(filtered_data)