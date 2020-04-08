#import bibiliotek
import json
import pprint
import requests
from bs4 import BeautifulSoup
#funkcja do ekstrakcji składowych opini
def extract_feature(opinion,tag,tag_class,child=None):
    try:
        if child:
            return opinion.find(tag,tag_class).find(child).get_text().strip()
        else:
            return opinion.find(tag,tag_class).get_text().strip()
    except AttributeError:
        return None
#zdefiniowanie adresu url przykladowej strony z opiniami
url_prefix= 'https://www.ceneo.pl'
product_id=input('Podaj numer produktu: ')#"70863343"
url_postfix = '/'+product_id+'#tab=reviews'
url=url_prefix+url_postfix
opinions_list=[]
tags={
        "recommendation":["div","product-review-summary","em"],
        "stars":["span","review-score-count"],
        "author":["div","reviewer-name-line"],
        "content":["p","product-review-body"],
        "pros":["div", "pros-cell","ul"],
        "cons":["div", "cons-cell","ul"],
        "useful":["button","vote-yes","span"],
        "useless":["button","vote-no","span"],
        "purchased":["div", "product-review-pz","em"]
        }
#funkcja do usuwania znakow formatujacych
def remove_wspace(string):
    try:
        return features[string].replace('\n',', ').replace('\r',', ')
    except AttributeError:
        pass

while url:
    #pobranie kodu html tej strony
    page_response =requests.get(url)
    page_tree = BeautifulSoup(page_response.text, 'html.parser')
    opinions = page_tree.find_all('li', class_='js_product-review')
    #pusta lista na wszystkie opinie 
    
    #Wydobycie skladowych pojedynczej opinii
    for opinion in opinions:
        features ={key:extract_feature(opinion, *args)
                    for key,args in tags.items()}
        features["purchased"]=(features["purchased"]=="Opinia potwierdzona zakupem")
        features["opinion_id"]=int(opinion["data-entry-id"])
        features['useful']=int(features['useful'])
        features['useless']=int(features['useless'])
        features['content']=remove_wspace('content')
        features['pros']=remove_wspace('pros')
        features['cons']=remove_wspace('cons')
        dates =opinion.find("span", "review-time").find_all("time")
        features["review_date"] = dates.pop(0)["datetime"]
        try:
            features["purchase_date"] = dates.pop(0)["datetime"]
        except IndexError:
            purchase_date = None

        opinions_list.append(features)
    print(url)
    try:
        url=url_prefix + page_tree.find("a", class_="pagination__next")["href"]
    except TypeError:
        url= None
with open("./opinions_json/"+product_id+'.json','w',encoding="utf-8") as fp:
    json.dump(opinions_list,fp,ensure_ascii=False,indent=4,separators=(',',':'))
#print(len(opinions_list))
#pprint.pprint(opinions_list)



