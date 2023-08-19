# Import library yang diperlukan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca dataset
@st.cache  # Menyimpan hasil caching untuk mempercepat loading data
def load_data():
    data = df = pd.read_csv('Data/Credit Card Customer Data.csv',sep=';',engine='python')
    return data

data = load_data()

# Judul Aplikasi
st.title('Aplikasi Analisis Credit Cards Customer')

# Tampilkan dataset
st.subheader('Dataset Credit Cards Customer')
st.write(data.head())

# Visualisasi Data
st.subheader('Visualisasi Data')

# Histogram Avg_Credit_Limit
st.subheader('Histogram Avg_Credit_Limit')
plt.figure(figsize=(8, 6))
sns.histplot(data['Avg_Credit_Limit'], bins=20, kde=True)
st.pyplot()

# Scatter plot Total_Credit_Cards vs. Avg_Credit_Limit
st.subheader('Scatter plot Total_Credit_Cards vs Total_visits_bank')
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Total_Credit_Cards', y='Total_visits_bank', hue='Sl_No')
st.pyplot()

# Scatter plot Total_Credit_Cards vs. Avg_Credit_Limit
st.subheader('Scatter plot Total_Credit_Cards vs Total_visits_online')
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Total_Credit_Cards', y='Total_visits_online', hue='Sl_No')
st.pyplot()

# Scatter plot Total_Credit_Cards vs. Avg_Credit_Limit
st.subheader('Scatter plot Total_Credit_Cards vs Total_calls_made')
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Total_Credit_Cards', y='Total_calls_made', hue='Sl_No')
st.pyplot()

# Distribusi Total_visits_online
st.subheader('Outlier')
plt.figure(figsize=(8, 6))
sns.boxplot(data['Avg_Credit_Limit'])
st.pyplot()

# Statistik Deskriptif
st.subheader('Statistik Deskriptif')
st.write(data.describe())

# Footer
st.write('Sumber data: https://www.kaggle.com/datasets/aryashah2k/credit-card-customer-data')

