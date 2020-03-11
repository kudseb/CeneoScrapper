#import bibiliotek
import requests
from bs4 import BeautifulSoup
#zdefiniowanie adresu url przykladowej strony z opiniami

url = 'https://www.ceneo.pl/40546569#tab=reviews'
#pobranie kodu html tej strony
page_response =requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')
opinions = page_tree.find_all('li', class_='js_product-review')
opinion = opinions.pop()
opinion_id = opinion["data-entry-id"]
print(opinion_id )
author= opinion.find("div",class_='reviewer-name-line').string
print(author)
# gwiazdki             : span.review-score-count
# - potwierdzona zakupem : div.product-review-pz
# - data wystawienia     : span.review-time > time["datatime"] -pierwsyz el listy
# - data zakupu          : span.review-time > time["datatime"] -drugi el listy
# - przydatna            : button.vote-yes['data-total-vote']
#                        : span[id=^votes-yes]
#                        : button.vote-yes>span
# - nieprzydatna         : button.vote-no['data-total-vote']
#                        : span[id=^votes-no]
#                        : button.vote-no>span
# - treść                : p.product-review-body
# - wady                 : div.cons-cell > ul
# - zalety               : div.pros-cell > ul

recommendation = opinion.find('div' ,class_='product-review-summary').find('em').string
print(recommendation)
stars= opinion.find('span' , class_='review-score-count').string
verified_by_purchased=opinion.find('div' , class_='product-review-pz')
#data wystawienia =opinion.find('span' , class_='review-time').find
#data zakupu =opinion.find('span' , class_='review-time').find
usefull=opinion.find('button' , class_='vote-yes').find('span').string
uselless=opinion.find('button' , class_='vote-no').find('span').string
content=opinion.find('p' , class_='product-review-body').string
print(stars)
print(verified_by_purchased)
print(usefull)
print(uselless)
print(content)

#Wydobycie z kodu html fragmentów odpowiadajacym poszczegolnym opiniom

#Wydobycie skladowych pojedynczej opinii

#

