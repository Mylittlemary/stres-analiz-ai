# 🧠 Yapay Zeka Destekli Uyku ve Stres Analizörü

Bu proje, bireylerin uyku sırasındaki fizyolojik verilerini analiz ederek **stres seviyelerini** tahmin eden bir makine öğrenmesi uygulamasıdır. Psikoloji ve veri bilimini birleştirerek, biyometrik verilerin ruh sağlığı üzerindeki etkilerini somutlaştırmayı amaçlar.

## 🚀 Proje Hakkında
Bu çalışma, **SaYoPillow (Smart-Yoga Pillow)** veri seti kullanılarak geliştirilmiştir. Model, uyku esnasındaki horlama, solunum hızı, vücut sıcaklığı ve kalp atışı gibi parametreleri inceleyerek 5 farklı stres seviyesinden (0-4) birini tahmin eder.

## 📊 Kullanılan Parametreler
- **sr (Snoring Rate):** Horlama şiddeti
- **rr (Respiration Rate):** Solunum hızı
- **hr (Heart Rate):** Kalp atış hızı
- **sr.1 (Sleeping Hours):** Toplam uyku süresi
- **rem (REM Sleep):** REM uykusu süresi
- **sl (Stress Level):** Hedef Değişken (0: Düşük, 4: Yüksek)

## 🛠️ Teknoloji Yığını
* **Dil:** Python 3.12
* **Kütüphaneler:** `Pandas`, `Scikit-learn`, `Seaborn`, `Matplotlib`
* **Model:** Random Forest Classifier (Rastgele Orman Sınıflandırıcısı)
* **Arayüz:** Streamlit

## 📈 Bulgular
Yapılan analizlerde uyku süresi ile stres seviyesi arasında **-0.97** oranında çok güçlü bir negatif korelasyon saptanmıştır. Bu, yetersiz uykunun stres seviyesini doğrudan ve şiddetli şekilde artırdığını göstermektedir. Modelin genel başarı oranı (Accuracy) **%98**'in üzerindedir.


## 💻 Kurulum ve Çalıştırma
Projeyi kendi bilgisayarınızda çalıştırmak için:

1. Depoyu klonlayın: `git clone https://github.com/kullanici-adiniz/stres-analiz-ai.git`
2. Gerekli kütüphaneleri kurun: `pip install -r requirements.txt`
3. Uygulamayı başlatın: `streamlit run uygulama.py`
<img width="500"<img width="1919" height="812" alt="Ekran görüntüsü 2026-03-06 120944" src="https://github.com/user-attachments/assets/a1cad8c8-f561-413a-b2d6-e141d599bd1b" />


<img width="1919" height="812" alt="Ekran görüntüsü 2026-03-06 121047" src="https://github.com/user-attachments/assets/9689473a-0650-4bb3-b92a-38426b8b816d" />


---
