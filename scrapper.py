#import bibiliotek
import json
import pprint
import requests
from bs4 import BeautifulSoup
#zdefiniowanie adresu url przykladowej strony z opiniami
url_prefix= 'https://www.ceneo.pl'
product_id=input('Podaj numer produktu: ')#"70863343"
url_postfix = '/'+product_id+'#tab=reviews'
url=url_prefix+url_postfix
opinions_list=[]
while url:
    #pobranie kodu html tej strony
    page_response =requests.get(url)
    page_tree = BeautifulSoup(page_response.text, 'html.parser')
    opinions = page_tree.find_all('li', class_='js_product-review')
    #pusta lista na wszystkie opinie 
    
    #Wydobycie skladowych pojedynczej opinii
    for opinion in opinions:
        #Wydobycie z kodu html fragmentów odpowiadajacym poszczegolnym opiniom
        opinion_id = opinion["data-entry-id"]
        author = opinion.find("div", "reviewer-name-line").string
        try:
            recommendation = opinion.find("div","product-review-summary").find("em").string
        except AttributeError:
            recommendation = None
        stars = opinion.find("span", "review-score-count").string
        try:
            purchased = opinion.find("div", "product-review-pz").find("em").string
        except AttributeError:
            purchased = None
        dates = opinion.find("span", "review-time").find_all("time")
        review_date = dates.pop(0)["datetime"]
        try:
            purchase_date = dates.pop(0)["datetime"]
        except IndexError:
            purchase_date = None
        useful = opinion.find("button","vote-yes").find("span").string
        useless = opinion.find("button","vote-no").find("span").string
        content = opinion.find("p","product-review-body").get_text()
        try:
            pros = opinion.find("div", "pros-cell").find("ul").get_text()
        except AttributeError:
            pros = None
        try:
            cons = opinion.find("div", "cons-cell").find("ul").get_text()
        except AttributeError:
            cons = None
        opinion_dict={
        "opinion_id":opinion_id,
        "recommendation":recommendation,
        "stars":stars,
        "author":author,
        "pros":pros,
        "cons":cons,
        "useful":useful,
        "useless":useless,
        "purchased":purchased,
        "purchase_date":purchase_date,
        "review_date":review_date
        }
        opinions_list.append(opinion_dict)
    print(url)
    try:
        url=url_prefix + page_tree.find("a", class_="pagination__next")["href"]
    except TypeError:
        url= None
with open(product_id+'.json','w',encoding="utf-8") as fp:
    json.dump(opinions_list,fp,ensure_ascii=False,indent=4,separators=(',',':'))
#print(len(opinions_list))
#pprint.pprint(opinions_list)



