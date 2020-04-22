#import bibliotek
from flask import Flask

#utworzenie obiektu(instancji) klasy Flask reprezentującego aplikację
app=Flask(__name__)

#import widoków/routingów z aplikacji
from app import views