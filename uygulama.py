import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# 1. Başlık ve Açıklama
st.set_page_config(page_title="AI Stres Analizörü", page_icon="🧠")
st.title("🧠 Yapay Zeka Destekli Stres Analiz Paneli")
st.markdown("Bu uygulama, uyku verilerinizi analiz ederek stres seviyenizi tahmin eder.")

# 2. Veriyi ve Modeli Arka Planda Hazırla (Basitleştirilmiş)
@st.cache_data
def model_hazirla():
    df = pd.read_csv('SaYoPillow.csv')
    X = df.drop('sl', axis=1)
    y = df['sl']
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model

model = model_hazirla()

# 3. Yan Panel: Kullanıcı Girişleri
st.sidebar.header("Fizyolojik Verileriniz")
uyku_saati = st.sidebar.slider("Dün Gece Kaç Saat Uyudunuz?", 0.0, 12.0, 7.0)
nabiz = st.sidebar.slider("Ortalama Kalp Atış Hızı (Nabız)", 40, 120, 70)
horlama = st.sidebar.slider("Horlama Oranı", 0, 100, 50)
nefes_hizi = st.sidebar.slider("Solunum Hızı", 10, 30, 20)

# 4. Tahmin Butonu ve Sonuç
if st.button("Analiz Et"):
    # Diğer verileri ortalama değerlerle dolduruyoruz (Şimdilik)
    girdi = [[horlama, nefes_hizi, 90, 10, 90, 10, uyku_saati, nabiz]]
    tahmin = model.predict(girdi)[0]
    
    stres_durumlari = {
        0: ("Düşük/Yok", "🟢"), 1: ("Normal", "🟡"), 
        2: ("Orta", "🟠"), 3: ("Orta-Yüksek", "🔴"), 4: ("Yüksek", "🔥")
    }
    
    durum, emoji = stres_durumlari[tahmin]
    st.subheader(f"Tahmin Edilen Stres Seviyesi: {durum} {emoji}")
    
    if tahmin >= 3:
        st.warning("Psikolojik Not: Verileriniz yüksek stres altında olduğunuzu gösteriyor. Dinlenmeniz ve nefes egzersizi yapmanız önerilir.")
    else:
        st.success("Tebrikler! Fizyolojik verileriniz sağlıklı bir seviyede görünüyor.") 