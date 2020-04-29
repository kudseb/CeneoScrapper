# CeneoScraper12
## Etap 1 - pobranie składowych pojedynczej opinii
<<<<<<< HEAD
- opinia               : li.review-box
- identyfikator        : li.review-box["data-entry-id"]
- autor                : div.reviewer-name-line
- rekomendacja         : div.product-review-summary > em
- gwiazdki             : span.review-score-count
- potwierdzona zakupem : div.product-review-pz
- data wystawienia     : span.review-time > time["datatime"] -pierwsyz el listy
- data zakupu          : span.review-time > time["datatime"] -drugi el listy
- przydatna            : button.vote-yes['data-total-vote']
                       : span[id=^votes-yes]
                       : button.vote-yes>span
- nieprzydatna         : button.vote-no['data-total-vote']
                       : span[id=^votes-no]
                       : button.vote-no>span
- treść                : p.product-review-body
- wady                 : div.cons-cell > ul
- zalety: div.pros-cell > ul
## Etap 2 - pobranie składowych wszystkich opinii z poedynczej strony
- zapisanie składowych opinii w złożonej strukturze danych
## Etap 3 - pobranie wszystkich opinii o pojedynczym produkcie
- przechodzenie po stronach z opiniami
- eksport opinii do pliku (.csv. lub .xlsx lub .json)
## Etap 4
- transformacja danych
- refaktoryzacjia kodu
## Etap 5
- zapis danych do obiektu dataframe(ramka danych)
- wykonanie podstawowych oblcizen na danych w ramce danych
- wykonanie prostych wykresów na podstawie danych w ramce danych
## Etap 6 - przygotowanie interfejsu webowego aplikacji (Flask) 
-struktura aplikacji
-     /CeneoScraper  
        /run.py  
        /config.py  
        /app  
            /__init__.py
            /views.py  
            /models.py
            /scrapper.py
            /analyzer.py  
            /static/  
                /main.css
            /templates/  
                /base.html  
        /requirements.txt
        /README.md  
        /./venv
-widoki (Jinja)
-routing