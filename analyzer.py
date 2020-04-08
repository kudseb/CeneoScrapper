#import bibliotek
import os
import pandas as pd
#wyswietlenie zawartosc katalogu 
print(*os.listdir('./opinions_json'))
#wczytanie idetyfikatora produktu, którego opinie bedą analizowanie
product_id = input("Podaj Kod produktu: ")
opinions=pd.read_json("./opinions_json/"+product_id+'.json')
opinions=opinions.set_index("opinion_id")
print(opinions)