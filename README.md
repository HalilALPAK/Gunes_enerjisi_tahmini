# 🌞 Güneş Enerjisi Üretimi Tahmin Uygulaması

Bu proje, **güneş enerjisi üretimi** tahminleri yapabilen bir **makine öğrenmesi modeline** dayalı bir web uygulaması geliştirmek için kullanılmıştır. Kullanıcılar, dünya genelindeki çeşitli şehirlerden hava durumu verilerini alıp, **güneş enerjisi** üretimi hakkında tahminler alabilirler.

Proje, kullanıcı dostu bir **Streamlit** arayüzü ile sunulmakta ve veriler **OpenWeatherMap API**'den çekilmektedir. Tahminler, **Rastgele Orman Regresyonu (Random Forest Regressor)** modelinden alınmaktadır. 🌍🔋

---

## 🚀 Proje Özellikleri

- **Güneş Enerjisi Tahmini:** Hava durumu verilerine dayalı olarak, **güneş ışınımı (sunshine)** ve diğer hava koşullarına göre **güneş enerjisi üretimi** tahmin edilir.
- **OpenWeatherMap API:** Gerçek zamanlı hava durumu verileri (sıcaklık, rüzgar hızı, nem, basınç, bulutluluk) çekilir.
- **Makine Öğrenmesi Modeli:** Güneş enerjisi üretimini tahmin etmek için en iyi parametrelerle eğitilmiş **RF(Random Forest Regressor)** modelini kullanıyoruz.
- **Grid Search:** Modelin performansını optimize etmek için **Grid Search** kullanarak en iyi hiperparametreleri bulduk.
- **Streamlit Arayüzü:** Kullanıcı dostu bir arayüz ile şehir seçimi, hava durumu görüntüleme ve enerji üretimi tahminleri yapılır.

---

## 🛠️ Kullanılan Teknolojiler

- **Python:** Proje, Python dilinde yazılmıştır.
- **Streamlit:** Web uygulaması geliştirmek için kullanıldı.
- **OpenWeatherMap API:** Gerçek zamanlı hava durumu verisi almak için kullanıldı.
- **Scikit-Learn:** Makine öğrenmesi modelini eğitmek için kullanıldı.
- **Pickle:** Modelin saklanması ve yüklenmesi için kullanıldı.
- **Folium:** Harita üzerinde şehir seçimi yapmak için kullanıldı.

---

## 📥 Gereksinimler

- Python 
- Gerekli kütüphaneler:
  - `streamlit`
  - `folium`
  - `requests`
  - `scikit-learn`
  - `numpy`
  - `pickle`

Yukarıdaki kütüphaneleri yüklemek için şu komutu kullanabilirsiniz:

```bash
pip install streamlit folium requests scikit-learn numpy

