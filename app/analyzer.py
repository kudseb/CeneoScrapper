#import bibliotek
import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


#wyswietlenie zawartosc katalogu 
print(*os.listdir('./opinions_json'))
#wczytanie idetyfikatora produktu, którego opinie bedą analizowanie
product_id = input("Podaj Kod produktu: ")
opinions=pd.read_json("./opinions_json/"+product_id+'.json')
opinions=opinions.set_index("opinion_id")

opinions['stars']=opinions["stars"].map(lambda x: float(x.split('/')[0].replace(',','.')))
#częstosc występowania poszczególnej liczby gwiadek
stars = opinions["stars"].value_counts().sort_index().reindex(list(np.arange(0,5.1,0.5)), fill_value=0)
fig, ax = plt.subplots()
stars.plot.bar(color='purple')
plt.xticks(rotation = 0)
ax.set_title('Częstość wytępowania poszczególnych cen')
ax.set_xlabel('liczba gwiazdek')
ax.set_ylabel('liczba opini')
plt.savefig("./figures_png/"+product_id+'_bar.png')
plt.close()
#udział poszczególnych rekomendacji w ogolne opinii
recommendation = opinions["recommendation"].value_counts()
fig, ax = plt.subplots()
recommendation.plot.pie(label='',autopct='%.1f%%')
ax.set_title('Udizał poszczególnych rekomendacji w ogolne opini')
plt.savefig("./figures_png/"+product_id+'_pie.png')
plt.close()
stars_avarega= opinions['stars'].mean()
pros= opinions['pros'].count()
cons= opinions['cons'].count()
purchased = opinions['purchased'].sum()
print(stars_avarega,pros,cons,purchased)

stars_purchased = pd.crosstab(opinions["stars"],opinions["purchased"])
print(stars_purchased)