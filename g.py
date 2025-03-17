import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
import pickle
import numpy as np

# API'den hava durumu verisini almak için fonksiyon
def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        clouds = data['clouds']['all']  # Bulutluluk oranı (0-100)
        
        # Sunshine ve Radiation hesaplama
        sunshine = 100 - clouds  # Sunshine, bulutluluğun tamamlayanı olacak
        radiation = sunshine  # Radiation değerini Sunshine ile aynı kabul ediyoruz
        
        weather_info = {
            "Sıcaklık": data['main']['temp'],
            "Rüzgar Hızı": data['wind']['speed'],
            "Rüzgar Yönü": data['wind']['deg'],
            "Hava Basıncı": data['main']['pressure'],
            "Nem": data['main']['humidity'],
            "Sunshine": sunshine,  # Sunshine bilgisi
            "Radiation": radiation  # Radiation bilgisi
        }
        return weather_info
    else:
        return None

# 📌 Şehir Koordinatları (Örnek)
city_coordinates = {
    'İstanbul': [41.0082, 28.9784],
    'Ankara': [39.9334, 32.8597],
    'İzmir': [38.4192, 27.1287],
    'Bursa': [40.1954, 29.0601],
    'Antalya': [36.8841, 30.7056],
    'Adana': [37.0, 35.3213],
    'Konya': [37.8660, 32.4800],
    'Gaziantep': [37.0662, 37.3833],
    'Trabzon': [41.0019, 39.7190],
    'Kayseri': [38.7333, 35.3213]
}

# 📌 Şehir Seçimi
city = st.selectbox("📍 Şehir Seçin:", list(city_coordinates.keys()), index=0)

# 📌 Harita Üzerinde Konum Seçimi
st.subheader("🌍 Haritadan Konum Seçin")
m = folium.Map(location=city_coordinates[city], zoom_start=6)
folium.Marker(city_coordinates[city], tooltip=city).add_to(m)
map_data = st_folium(m, width=700, height=400)

# 📌 API'den Hava Durumu Verisini Çek
api_key = "601c0bdb3709bf5472c7a721ef457c42"
weather_data = get_weather_data(api_key, city)

# 📌 Hava Durumu Bilgilerini Göster
if weather_data:
    st.markdown(f"""
    **🌤️ Hava Durumu Bilgileri**  
    🌡️ **Sıcaklık:** {weather_data['Sıcaklık']}°C  
    💨 **Rüzgar Hızı:** {weather_data['Rüzgar Hızı']} m/s  
    🌬️ **Rüzgar Yönü:** {weather_data['Rüzgar Yönü']}°  
    📊 **Hava Basıncı:** {weather_data['Hava Basıncı']} hPa  
    💧 **Nem:** {weather_data['Nem']}%  
    🌞 **Sunshine (Radiation olarak alınmıştır):** {weather_data['Radiation']}%  
    """)
else:
    st.error("⚠️ Hava durumu verisi alınamadı!")

# Modeli yükle
with open("best_rf_model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)

# Butonları iki kutuya yerleştirme
col1, col2 = st.columns(2)

with col1:
    if st.button("Güneş Enerjisi Tahmin Et", key="solar"):
        if weather_data:
            # Modelden tahmin yap (örneğin, Güneş Enerjisi)
            features = np.array([[weather_data['Rüzgar Hızı'], weather_data['Hava Basıncı'], 
                                  weather_data['Sıcaklık'], weather_data['Nem'], 
                                  weather_data['Sunshine'], weather_data['Radiation']]])  # Model için gerekli 6 özellik
            prediction = loaded_model.predict(features)  # Modeli kullanarak tahmin yap
            st.success(f"Tahmin Edilen Güneş Enerjisi Üretimi: {prediction[0]:.2f} Watt")
        else:
            st.error("⚠️ Hava durumu verisi alınamadı!")

with col2:
    if st.button("Rüzgar Enerjisi Tahmin Et", key="wind"):
        if weather_data:
            # Modelden tahmin yap (örneğin, Rüzgar Enerjisi)
            features = np.array([[weather_data['Rüzgar Hızı'], weather_data['Hava Basıncı'], 
                                  weather_data['Sıcaklık'], weather_data['Nem'], 
                                  weather_data['Sunshine'], weather_data['Radiation']]])  # Model için gerekli 6 özellik
            prediction = loaded_model.predict(features)  # Modeli kullanarak tahmin yap
            st.success(f"Tahmin Edilen Rüzgar Enerjisi Üretimi: {prediction[0]:.2f} MW")
        else:
            st.error("⚠️ Hava durumu verisi alınamadı!")
