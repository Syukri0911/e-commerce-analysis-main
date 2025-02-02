# README: Analisis Data E-Commerce

## 1. Pendahuluan
Proyek ini bertujuan untuk menganalisis data transaksi e-commerce yang telah dikumpulkan dari beberapa file CSV. Proses yang dilakukan mencakup penggabungan data, eksplorasi data, pembersihan data, visualisasi, hingga mendapatkan insight dari data tersebut.

## 2. Langkah-Langkah Analisis Data

### **1. Pengumpulan Data (Data Gathering)**
- Semua file CSV dalam folder `data` digabungkan menjadi satu DataFrame menggunakan library `pandas`.
- File yang digunakan memiliki berbagai informasi seperti pelanggan, penjual, pesanan, pembayaran, dan ulasan.

### **2. Assessing Data (Penilaian Data)**
- Mengecek struktur data menggunakan `info()` untuk memahami tipe data dan jumlah data.
- Menggunakan `describe()` untuk melihat statistik deskriptif pada data numerik.
- Mengidentifikasi jumlah nilai yang hilang dengan `isnull().sum()`.
- Menentukan apakah ada outliers yang bisa memengaruhi analisis.

### **3. Data Cleaning (Pembersihan Data)**
- Mengisi nilai yang hilang pada kolom numerik dengan median.
- Mengisi nilai yang hilang pada kolom kategori dengan modus atau "Unknown".
- Menghapus baris yang memiliki lebih dari 50% nilai yang hilang.
- Mengonversi kolom tanggal menjadi format `datetime`.

### **4. Exploratory Data Analysis (EDA)**
- Visualisasi distribusi harga produk menggunakan histogram.
- Analisis hubungan antara harga dan skor ulasan menggunakan boxplot.
- Analisis rata-rata waktu pengiriman berdasarkan kode pos pelanggan.
- Analisis harga rata-rata per kategori produk.
- Analisis total pembayaran berdasarkan metode pembayaran.

## 3. Insight dari Assessing Data
### **1. Kualitas Data**
- Beberapa kolom memiliki nilai yang hilang, terutama pada data pengiriman dan ulasan.
- Tipe data tidak selalu sesuai, sehingga perlu dikonversi untuk keperluan analisis lebih lanjut.

### **2. Distribusi Data**
- Data memiliki outliers dalam harga produk, yang bisa disebabkan oleh produk premium.
- Rata-rata waktu pengiriman bervariasi tergantung lokasi pelanggan.

### **3. Kesimpulan dari Assessing Data**
- Data perlu dibersihkan dan dikonversi agar dapat digunakan secara optimal.
- Outliers dalam harga perlu diperiksa lebih lanjut apakah relevan atau perlu ditangani.
- Nilai yang hilang pada data pengiriman bisa mempengaruhi analisis terkait efisiensi logistik.

## 4. Kesimpulan dan Rekomendasi
- Produk dengan harga lebih tinggi memiliki variasi ulasan yang lebih besar.
- Waktu pengiriman lebih cepat berhubungan dengan rating lebih tinggi.
- Beberapa kategori produk memiliki harga yang lebih tinggi dan bisa dijadikan fokus untuk strategi penjualan.
- Kartu kredit adalah metode pembayaran yang paling banyak digunakan.

## 5. Teknologi yang Digunakan
- **Python**: `pandas`, `numpy`, `seaborn`, `matplotlib`
- **Jupyter Notebook** atau **Streamlit** untuk eksplorasi dan visualisasi data.

