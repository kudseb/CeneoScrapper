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
- zalety               : div.pros-cell > ul
