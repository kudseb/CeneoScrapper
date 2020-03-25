#import bibiliotek
import requests
from bs4 import BeautifulSoup
#zdefiniowanie adresu url przykladowej strony z opiniami

url = 'https://www.ceneo.pl/40546569#tab=reviews'
#pobranie kodu html tej strony
page_response =requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')
opinions = page_tree.find_all('li', class_='js_product-review')
for opinion in opinions:
    opinion_id = opinion["data-entry-id"]
    author = opinion.find("div", "reviewer-name-line").string
    try:
        recommendation = opinion.find("div","product-review-summary").find("em").string
    except AttributeError:
        recommendation = None
    stars = opinion.find("span", "review-score-count").string
    try:
        purchased = opinion.find("div", "product-review-pz").string
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
    print(opinion_id, recommendation, stars, content, author, pros, cons, useful, useless, purchased, purchase_date, review_date)

#Wydobycie z kodu html fragmentów odpowiadajacym poszczegolnym opiniom

#Wydobycie skladowych pojedynczej opinii

#

