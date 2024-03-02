import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from matplotlib.gridspec import GridSpec
sns.set(style='dark')


# Load dataset
day_new = pd.read_csv("https://raw.githubusercontent.com/Arfi3/submission/main/dashboard/day_new.csv")
# Set page configuration
st.set_page_config(page_title="BIKERS",
                   page_icon="🚴‍♂️",
                   layout="wide")
st.image("https://raw.githubusercontent.com/Arfi3/gambar/main/bike.png")
st.markdown("---")

st.title("🚲 BIKERS : Bike-sharing Analysis Dashboard")
st.markdown("---")
st.subheader("Dataframe Jumlah Penyewa sepeda:")
st.dataframe(day_new)
with st.container():
    col1, col2, col3 = st.columns(3, gap='large')
    with col1:
        total_all_rides = day_new['cnt'].sum()
        st.metric("Total Rides", value=total_all_rides)
    with col2:
        total_casual_rides = day_new['casual'].sum()
        st.metric("Total Casual Rides", value=total_casual_rides)
    with col3:
        total_registered_rides = day_new['registered'].sum()
        st.metric("Total Registered Rides", value=total_registered_rides)


st.image("https://www.gambaranimasi.org/data/media/1125/animasi-bergerak-bersepeda-0060.gif")

with st.sidebar:
    st.image("https://raw.githubusercontent.com/Arfi3/gambar/main/logo.png")
    st.sidebar.header("Options")
    
# Buttons for different analysis options
show_answer = st.sidebar.markdown("[Bagian 1](#bagian-1)")
show_main = st.sidebar.markdown("[Bagian 2](#bagian-2)")

st.markdown("## Bagian 1")
st.subheader(
    "1. Bagaimana musim, cuaca, temperatur, temperatur yang dirasakan, dan kelembapan memengaruhi peminjaman sepeda?"
)
st.write("Pada bagian ini akan dibahas analisa pengaruh musim, cuaca, temperatur, temperatur yang dirasakan, dan kelembapan dalam mempengaruhi jumlah penyewa sepeda.")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Season", "Weather", "Temp", "Atemp", "Humidity"])
with tab1:
    fig = plt.figure(figsize=(12, 10))
    gs1 = GridSpec(4, 4, fig, wspace=0.5, hspace=0.5)
    plt.suptitle("Jumlah Penyewa Berdasarkan Musim", fontsize=16)
    plt.subplot(gs1[:2, 1:3])
    sns.boxplot(x='season', y='cnt', data=day_new, palette="Set2", hue='season', legend=False)
    plt.xlabel("Musim", fontsize=12)
    plt.ylabel("Jumlah Penyewa", fontsize=12)
    plt.subplot(gs1[2:, :2])
    sns.boxplot(x='season', y='casual', data=day_new, palette="Set2", hue='season', legend=False)
    plt.xlabel("Musim", fontsize=12)
    plt.ylabel("Jumlah Penyewa Non-Registered(casual)", fontsize=12)
    plt.subplot(gs1[2:, 2:])
    sns.boxplot(x='season', y='registered', data=day_new, palette="Set2", hue='season', legend=False)
    plt.xlabel("Musim", fontsize=12)
    plt.ylabel("Jumlah Penyewa Registered(registered)", fontsize=12)
    st.pyplot(fig)

    st.error("Jumlah penyewa Registered naik pada musim semi, dan turun pada musim semi,\
        sedangkan jumlah penyewa Non-registered(Casual) naik pada musim panas dan musim gugur,\
        dan turun pada musim semi.\
        Sehingga untuk keseluruhan penyewa sepeda akan naik pada musim gugur dan turun pada musim semi.")
with tab2:
    fig = plt.figure(figsize=(12, 10))
    gs1 = GridSpec(4, 4, fig, wspace=0.5, hspace=0.5)
    plt.suptitle("Jumlah Penyewa Berdasarkan Cuaca", fontsize=16)
    plt.subplot(gs1[:2, 1:3])
    sns.boxplot(x='weathersit', y='cnt', data=day_new, palette="Set2", hue='weathersit', legend=False)
    plt.xlabel("Cuaca", fontsize=12)
    plt.ylabel("Jumlah Penyewa", fontsize=12)
    plt.subplot(gs1[2:, :2])
    sns.boxplot(x='weathersit', y='casual', data=day_new, palette="Set2", hue='weathersit', legend=False)
    plt.xlabel("Cuaca", fontsize=12)
    plt.ylabel("Jumlah Penyewa Non-Registered(casual)", fontsize=12)
    plt.subplot(gs1[2:, 2:])
    sns.boxplot(x='weathersit', y='registered', data=day_new, palette="Set2", hue='weathersit', legend=False)
    plt.xlabel("Cuaca", fontsize=12)
    plt.ylabel("Jumlah Penyewa Registered(registered)", fontsize=12)
    plt.tight_layout()
    st.pyplot(fig)

    st.error("Jumlah penyewa Registered naik pada saat cuaca cerah,\
         dan turun pada saat cuaca bersalju, hal serupa pada jumlah penyewa Non-registered(Casual)\
              naik pada saat cuaca cerah, dan turun pada saat cuaca bersalju\
             Sehingga untuk keseluruhan penyewa sepeda akan naik pada saat cuaca cerah, dan turun\
              pada saat cuaca bersalju.")

with tab3:
    fig = plt.figure(figsize=(12, 10))
    gs1 = GridSpec(4, 4, fig, wspace=0.5, hspace=0.5)
    plt.suptitle("Jumlah Penyewa Berdasarkan Temperatur", fontsize=16)
    plt.subplot(gs1[:2, 1:3])
    sns.regplot(x='temp', y='cnt', data=day_new,
            line_kws={"color":"black", "linewidth":2})
    plt.subplot(gs1[2:, :2])
    sns.regplot(x='temp', y='casual', data=day_new,
            line_kws={"color":"black", "linewidth":2})
    plt.subplot(gs1[2:, 2:])
    sns.regplot(x='temp', y='registered', data=day_new,
            line_kws={"color":"black", "linewidth":2})
    st.pyplot(fig)

    st.error("Terdapat hubungan positif antara temperatur dan jumlah penyewa baik Registered,\
        Non-registered(Casual), maupun total keseluruhan penyewa dimana semakin tinggi temperatur semakin banyak jumlah penyewa.")


with tab4:
    fig = plt.figure(figsize=(12, 10))
    gs1 = GridSpec(4, 4, fig, wspace=0.5, hspace=0.5)
    plt.suptitle("Jumlah Penyewa Berdasarkan Temperatur yang dirasakan", fontsize=16)
    plt.subplot(gs1[:2, 1:3])
    sns.regplot(x='atemp', y='cnt', data=day_new,
            line_kws={"color":"black", "linewidth":2})
    plt.subplot(gs1[2:, :2])
    sns.regplot(x='atemp', y='casual', data=day_new,
            line_kws={"color":"black", "linewidth":2})
    plt.subplot(gs1[2:, 2:])
    sns.regplot(x='atemp', y='registered', data=day_new,
            line_kws={"color":"black", "linewidth":2})
    st.pyplot(fig)

    st.error("Terdapat hubungan positif antara temperatur yang dirasakan dan jumlah penyewa baik Registered,\
             Non-registered, maupun total keseluruhan penyewa dimana semakin tinggi temperatur semakin banyak jumlah penyewa.")


with tab5:
    fig = plt.figure(figsize=(12, 10))
    gs1 = GridSpec(4, 4, fig, wspace=0.5, hspace=0.5)
    plt.suptitle("Jumlah Penyewa Berdasarkan kelembapan", fontsize=16)
    plt.subplot(gs1[:2, 1:3])
    sns.regplot(x='hum', y='cnt', data=day_new,
            line_kws={"color":"black", "linewidth":2})
    plt.subplot(gs1[2:, :2])
    sns.regplot(x='hum', y='casual', data=day_new,
            line_kws={"color":"black", "linewidth":2})
    plt.subplot(gs1[2:, 2:])
    sns.regplot(x='hum', y='registered', data=day_new,
            line_kws={"color":"black", "linewidth":2})
    st.pyplot(fig)

    st.error("Tidak terlihat jelas antara kelembapan dan penyewa sepeda,\
        regresi linear yang digambarkan oleh garis hitam relatif datar atau\
        memiliki kemiringan yang sangat kecil, yang menunjukan bahwa kelembapan\
        mungkin tidak memiliki pengaruh yang signifikan terhadap jumlah penyewa sepeda.</font>")

st.markdown("## Bagian 2")
st.subheader(
    "2. Kapan waktu paling banyak peminjam sepeda?"
)
st.subheader("3. Kapan waktu paling sedikit peminjam sepeda?")
st.write("Pada bagian ini akan dibahas waktu penyewaan sepeda mencapai jumlah tertinggi dan terendah.")
tab1, tab2, tab3 = st.tabs(["Year", "Month", "Week"])

with tab1:
    st.header("Year")
    st.subheader("Count of Bike Rentals by Year")
    fig = plt.figure(figsize=(10, 8))
    gs1 = GridSpec(4, 4, fig, wspace=0.5, hspace=0.5)
    plt.suptitle("Jumlah Penyewa dari tahun ke tahun", fontsize=16)
    plt.subplot(gs1[:2, 1:3])
    sns.boxplot(x='yr', y='cnt', data=day_new, palette="flare", hue='yr', legend=False)
    plt.legend(loc='upper right', facecolor='none', labelcolor='yellow')
    plt.subplot(gs1[2:, :2])
    sns.boxplot(x='yr', y='casual', data=day_new, palette="flare", hue='yr', legend=False)
    plt.legend(loc='upper right', facecolor='none', labelcolor='yellow')
    plt.subplot(gs1[2:, 2:])
    sns.boxplot(x='yr', y='registered', data=day_new, palette="flare", hue='yr', legend=False)
    plt.legend(loc='upper right', facecolor='none', labelcolor='yellow')
    st.pyplot(fig)

    st.error("Jumlah penyewa sepeda meningkat dari tahun ke tahun,\
         sehingga jumlah penyewa sepeda mencapai jumlah terbanyak pada tahun 2012")
with tab2:
    st.header("Month")
    st.subheader("Count of Bike Rentals by Month")
    fig = plt.figure(figsize=(10, 8))
    gs1 = GridSpec(4, 4, fig, wspace=0.5, hspace=0.5)
    plt.suptitle("Jumlah Penyewa dari bulan ke bulan", fontsize=16)
    plt.subplot(gs1[:2, 1:3])
    sns.boxplot(x='mnth', y='cnt', data=day_new, palette="Set3", hue='mnth', legend=False)
    plt.subplot(gs1[2:, :2])
    sns.boxplot(x='mnth', y='casual', data=day_new, palette="Set3", hue='mnth', legend=False)
    plt.subplot(gs1[2:, 2:])
    sns.boxplot(x='mnth', y='registered', data=day_new, palette="Set3", hue='mnth', legend=False)
    st.pyplot(fig)

    st.error("Dapat dilihat bahwa jumlah penyewa sepeda cukup bervariasi setiap bulan nya.\
             Puncak jumlah penyewa sepeda terjadi pada bulan-bulan musim panas(dari bulan Mei sampai bulan September) \
            dan cenderung lebih rendah pada bulan-bulan musim dingin (dari bulan November sampai bulan Februari).")

with tab3:
    st.header("Week")
    st.subheader("Count of Bike Rentals by day of the Week")
    fig = plt.figure(figsize=(10, 8))
    gs1 = GridSpec(4, 4, fig, wspace=0.5, hspace=0.5)
    plt.suptitle("Jumlah Penyewa berdasarkan hari kerja dan hari libur", fontsize=16)
    plt.subplot(gs1[:2, 1:3])
    sns.boxplot(x='weekday', y='cnt', data=day_new, palette="rocket", hue='weekday', legend=False)
    plt.subplot(gs1[2:, :2])
    sns.boxplot(x='weekday', y='casual', data=day_new, palette="rocket", hue='weekday', legend=False)
    plt.subplot(gs1[2:, 2:])
    sns.boxplot(x='weekday', y='registered', data=day_new, palette="rocket", hue='weekday', legend=False)
    st.pyplot(fig)

    st.error("Dapat dilihat bahwa jumlah penyewa sepeda cukup bervariasi dari hari ke hari dalam seminggu,\
             pada jumlah penyewa sepeda Registered, penyewa sepeda tertinggi pada hari Jum'at,\
             sedangkan untuk Non-registered jumlah tertinggi pada hari Minggu.")



st.caption('Copyright (c), created by Arfi Nadhifa Hananti')