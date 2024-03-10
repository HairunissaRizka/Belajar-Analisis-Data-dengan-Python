import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit configuration to disable PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the data
df_day = pd.read_csv("day.csv")
df_hour = pd.read_csv("hour.csv")

# Data Cleaning
df_day["dteday"] = pd.to_datetime(df_day["dteday"])
df_hour["dteday"] = pd.to_datetime(df_hour["dteday"])

# Exploratory Data Analysis
# Tren Penggunaan Sepeda dari Waktu ke Waktu
def plot_bike_usage_over_time():
    plt.figure(figsize=(12, 6))
    plt.plot(df_day['dteday'], df_day['cnt'], color='b')
    plt.title('Tren Penggunaan Sepeda dari Waktu ke Waktu')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Sepeda yang Digunakan')
    st.pyplot()

# Pola Musiman dalam Penggunaan Sepeda
def plot_monthly_average():
    monthly_average = df_day.groupby('mnth')['cnt'].mean()
    plt.figure(figsize=(10, 5))
    monthly_average.plot(kind='bar', color='g')
    plt.title('Rata-Rata Penggunaan Sepeda per Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Rata-Rata Jumlah Sepeda yang Digunakan')
    plt.xticks(rotation=0)
    st.pyplot()

# Penggunaan Sepeda berdasarkan Kondisi Cuaca
def plot_weather_effect():
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='weathersit', y='cnt', data=df_day)
    plt.title('Pengaruh Cuaca terhadap Penggunaan Sepeda')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Sepeda yang Digunakan')
    st.pyplot()

# Distribusi Penggunaan Sepeda pada Hari Kerja vs. Hari Libur
def plot_workingday_distribution():
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='workingday', y='cnt', data=df_day)
    plt.title('Distribusi Penggunaan Sepeda pada Hari Kerja vs. Hari Libur')
    plt.xlabel('Hari Kerja (0 = Libur, 1 = Hari Kerja)')
    plt.ylabel('Jumlah Sepeda yang Digunakan')
    st.pyplot()

# Penggunaan Sepeda antara Jam Kerja dan Jam Non-Kerja
def plot_hourly_usage_diff():
    hourly_usage_diff = df_hour.groupby(['workingday', 'hr'])['cnt'].mean().unstack()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='hr', y='cnt', hue='workingday', data=df_hour, ci=None)
    plt.title('Perbedaan Pola Penggunaan Sepeda antara Jam Kerja dan Jam Non-Kerja')
    plt.xlabel('Jam')
    plt.ylabel('Jumlah Sepeda yang Digunakan')
    plt.legend(title='Hari Kerja')
    st.pyplot()

# Sidebar for Selection
st.sidebar.title('Pilih Visualisasi')
visualization = st.sidebar.radio('', ('Tren Penggunaan Sepeda dari Waktu ke Waktu', 
                                       'Pola Musiman dalam Penggunaan Sepeda', 
                                       'Penggunaan Sepeda berdasarkan Kondisi Cuaca',
                                       'Distribusi Penggunaan Sepeda pada Hari Kerja vs. Hari Libur',
                                       'Perbedaan dalam Pola Penggunaan Sepeda antara Jam Kerja dan Jam Non-Kerja'))

# Main Content
st.title('Dashboard Analisis Data Bike-sharing')

if visualization == 'Tren Penggunaan Sepeda dari Waktu ke Waktu':
    plot_bike_usage_over_time()
elif visualization == 'Pola Musiman dalam Penggunaan Sepeda':
    plot_monthly_average()
elif visualization == 'Penggunaan Sepeda berdasarkan Kondisi Cuaca':
    plot_weather_effect()
elif visualization == 'Distribusi Penggunaan Sepeda pada Hari Kerja vs. Hari Libur':
    plot_workingday_distribution()
elif visualization == 'Perbedaan dalam Pola Penggunaan Sepeda antara Jam Kerja dan Jam Non-Kerja':
    plot_hourly_usage_diff()
