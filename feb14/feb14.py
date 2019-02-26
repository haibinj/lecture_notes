import os 
from bs4 import BeautifulSoup

if not os.path.exists("parsed_results")
	os.mkdir("parsed_results")

f= open("html_files/coinmarketcap.html","r")

#class is not unique
#ID is unique, in this case <table id=
soup = BeautifulSoup(f.read(),'html.parser')
f.close()

#print(soup)
currencies_table = soup.find("table",{"id":"currencies"})
currencies_tbody = currencies_table.find("tbody")

currencies_row = currencies_tbody.find("tr",{"id":"id-bitcoin"})

print(currencies_row)