import requests 
#импортируем библиотеку requests, которая позволяет делать HTTP запросы к веб-страницам.
from bs4 import BeautifulSoup
#импортируем класс BeautifulSoup из библиотеки bs4, которая позволяет парсить HTML и XML документы.
url = 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'
parse_books_info(url)
