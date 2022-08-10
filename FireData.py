import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('FW_Veg_Rem_Combined.csv')
data = df[(df['longitude']<-100) & (df['fire_size']>30000)]
data = data.sort_values('fire_size', ascending = False).groupby('state').head(200)
plt.figure()
sns.lmplot(x='longitude', y='fire_size', data=data, hue='state', height=5)
plt.ylabel('fire size')
plt.show()