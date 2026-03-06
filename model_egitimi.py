import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Veriyi yükle
df = pd.read_csv('SaYoPillow.csv')

# 2. X (Girdiler: Kalp atışı, uyku vb.) ve y (Hedef: Stres Seviyesi) ayır
X = df.drop('sl', axis=1) # Stres sütununu çıkarıyoruz
y = df['sl']              # Sadece stres sütununu alıyoruz

# 3. Veriyi %80 Eğitim, %20 Test olarak böl
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Yapay Zeka Modelini Oluştur ve Eğit
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 5. Modelin Başarısını Test Et
tahminler = model.predict(X_test)
basari_orani = accuracy_score(y_test, tahminler)

print(f"Yapay Zeka Başarı Oranı: %{basari_orani * 100:.2f}")
print("\nDetaylı Rapor:")
print(classification_report(y_test, tahminler))


# --- TAHMİN BÖLÜMÜ ---

def stres_tahmin_et(horlama, nefes_hizi, sicaklik, hareket, oksijen, rem, uyku_saati, nabiz):
    # Kullanıcıdan gelen verileri modelin anlayacağı formata sokuyoruz
    yeni_veri = [[horlama, nefes_hizi, sicaklik, hareket, oksijen, rem, uyku_saati, nabiz]]
    tahmin = model.predict(yeni_veri)
    
    stres_durumlari = {
        0: "Düşük/Yok (Huzurlu)",
        1: "Normal",
        2: "Orta Seviye",
        3: "Orta-Yüksek",
        4: "Yüksek (Acil Dinlenme Gerekli!)"
    }
    
    return stres_durumlari[tahmin[0]]

# ÖRNEK SENARYO: 
# Kişi az uyumuş (4 saat) ve nabzı yüksek (85). Bakalım AI ne diyecek?
sonuc = stres_tahmin_et(95.0, 28.0, 88.0, 15.0, 82.0, 12.0, 4.0, 85.0)

print(f"\nSenaryo Analizi Sonucu: {sonuc}")