import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Veriyi oku
df = pd.read_csv('SaYoPillow.csv')

# Verinin ilk 5 satırını görerek her şeyin yolunda olduğunu teyit et
print("Veri Seti Başarıyla Yüklendi! İşte ilk 5 satır:")
print(df.head())

# Psikolojik Analiz: Hangi değişken stresi ne kadar etkiliyor?
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='RdYlGn')
plt.title('Fizyolojik Veriler Arasındaki İlişki (Korelasyon)')
plt.show()