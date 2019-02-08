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
#for r in results1:
#	print(r)

# to boildown the the elements:
#for r in results1:
#	print(r.text)

#results2 = soup.find('table').children
# for r in results2:
#	print(r)

#results2 = soup.find_all('tr')

#for r in results2:
#	for c in r.children:
#		print(c)

### class include information that may not shown in the form of text.

## in html, change into <span>Jan</span> this can break the code of children, that works through layers of html code.

results3=soup.find_all('td',attrs={'class' : 'user'})
for r in results3: 
	print(r)


results3=soup.find_all('td',attrs={'class' : 'user'})
for r in results3: 
	print(r.text)










