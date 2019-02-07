### parsing
## to chech the list of package, type: python3 -m pip list

from bs4 import BeautifulSoup

print("hello")

f = open("sample.html","r")

#to read the text
#print(f.read())

soup = 	BeautifulSoup(f.read(),'html.parser')
# only get the first element: print(soup.td)

results=soup.find('td')

print(results)

results1=soup.find_all('td')

print(results1)

# to operate the elements one by one:
for r in results1:
	print(r)

# to boildown the the elements:
for r in results1:
	print(r.text)




















