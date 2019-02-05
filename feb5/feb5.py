

## feb5   scrapping data from internet

## url

## data passing process, can not fail,
## data request process, sometimes fail.

import urllib.request
import ssl
## to test if this is working
print("hello")
## http protocal
response = urllib.request.urlopen("http://www.google.com")

print(response)

page = response.read()
print(page)

### to save to a file

f = open("google.html","w")
f.write(page)
f.close()
#TypeError: write() argument must be str, not bytes
#<!DOCTYPE html>
#<html>
#<head>
#<title></title>
#</head>
#<body>
#Hello world
#</body>
f = open("google.html","wb")
f.write(page)
f.close()


import urllib.request
import ssl
unverified_context = ssl._create_unverified_context()

response = urllib.request.urlopen("http://www.coinmarketcap.com",context=unverified_context)


page= response.read()

print(page)
f = open("coinmarketcap.html","wb")
f.write(page)
f.close()




## beautibul soup package can read the html file

## this program get the information follows "class" = "" .













