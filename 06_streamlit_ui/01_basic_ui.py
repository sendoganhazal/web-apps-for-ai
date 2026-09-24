"""
    Streamlit Nedir?
        - python ile web arayüzü geliştirme framework 

    Yapay zeka ve veri bilimi projelerinde neden kullanılır?
        - ui ile hızlı demo hazırlamak için
        - eğitilen bir modelin arayüzünü oluşturma
        - chatbot örneği
        - model tahmini gösterme

    Amaç:
        - streamlit temel bileşenlerini öğrenme
        - fastapi ile bir ml projesi yapmış gibi yapacağız

    Temel bileşenler:
        1. sayfa ayarları
        2. başlık ve metinler
        3. sidebar örneği
        4. metin giriş işlemleri
        5. sayısal giriş örneği
        6. seçim bileşenleri
        7. checkbox bileşenleri
        8. tarih ve saat
        9. dosya yükleme
        10. buton
        11. mesaj kutuları
        12. dataframe gösterimi
        13. sütun yapısı
        14. son bilgilendirme

    gerekli kütüphanelerin kurulması
        pip install streamlit pandas
"""

import streamlit as st
import pandas as pd
from datetime import date, time


# 1. sayfa ayarları
st.set_page_config(
    page_title="Streamlit Temel Bileşenler",
    page_icon="./pets.svg",
    layout="wide"
)

# 2. başlık ve metinler
st.title("Streamlit Temel Bileşenler Sayfası")
st.header("Python ile Web Uygulamalarına Giriş")
st.subheader("İlk Ders Uygulaması")
st.write("Bu bir örnek streamlit çalışmasıdır. Burada amacımız temel bileşenleri öğrenmektir.")

# 3. sidebar örneği
st.sidebar.title("Yan menü")
st.sidebar.write("Burası streamlit sidebar alanıdır")

sidebar_name = st.sidebar.text_input("Adınızı giriniz.")
sidebar_theme = st.sidebar.selectbox(
    "Sevdiğiniz alanı seçiniz",
    ["yapay zeka", "nlp", "veri bilimi", "image processing"]
)
st.sidebar.info(f"isim: {sidebar_name}") # bunu ben ekledim

st.sidebar.success(f"seçilen alan: {sidebar_theme}")

# 4. metin giriş işlemleri
st.header("Metin Giriş İşlemleri")
name = st.text_input("Ad soyad giriniz", placeholder = "Örn: John Doe")
email = st.text_input("email: ", placeholder = "johndoe@gmail.com")
about = st.text_area(
    "Kısaca kendinizi tanıtın",
    placeholder = "Buraya birkaç cümle yazın ...",
    height = 120
)

st.write(f"İsim: {name} - email: {email}") # bunu ben ekledim
st.write(f"About: {about}") # bunu ben ekledim

# 5. sayısal giriş örneği
st.header("Sayısal Giriş")
age = st.number_input("yaşınızı giriniz: ", min_value = 0, max_value = 120, value = 25, step = 1)
experience = st.slider("Python deneyim seviyenizi seçin (yıl)", min_value = 0, max_value = 15, value = 2)

st.write(f"Yaş: {age} - deneyim: {experience}") # bunu ben ekledim

# 6. seçim bileşenleri
st.header("Seçim bileşenleri")

city = st.selectbox(
    "şehrinizi seçiniz",
    ["Ankara", "İstanbul", "İzmir", "Bursa"]
)

education_level = st.radio(
    "Eğitim seviyenizi seçin:",
    ["lise", "lisans", "yüksek lisans"]
)

interests = st.multiselect(
    "İlgili alanları seçiniz",
    ["Python", "yapay zeka", "Derin öğrenme"]
)

st.write(f"Şehir: {city} - Eğitim seviyesi: {education_level}") # bunu ben ekledim
for interest in interests:
    st.write(f"İlgi alanı: {interest}") # bunu ben ekledim
    
# 7. checkbox bileşenleri
st.header("Checkbox Kullanımı")

is_student = st.checkbox("Öğrenciyim")
accept_rules = st.checkbox("Kuralları okudum ve kabul ediyorum")

if is_student:
  st.write(f"Ben öğrenciyim") # bunu ben ekledim

if accept_rules:
  st.write(f"Kuralları okudum ve kabul ediyorum") # bunu ben ekledim
  
# 8. tarih ve saat
st.header("Tarih seçin")
selected_date = st.date_input("Bir tarih seçin", value = date.today())
selected_time = st.time_input("Bir saat seçin", value = time(10, 30))

st.write(f"{selected_date} / {selected_time}")

# 9. dosya yükleme
# 10. buton
# 11. mesaj kutuları
# 12. dataframe gösterimi
# 13. sütun yapısı
# 14. son bilgilendirme