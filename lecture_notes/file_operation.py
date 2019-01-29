
# f = open("data.txt")

#print(f)

## run this file does not print. 

#print(f.read())

#print(f.read(3))

## the good thing of python is that it can control the reading stream of a file.




#f = open("data.txt",'w')

#print(f)


## over-writing a file. 'w' open with write 
with open("data2.txt",'w',encoding = 'utf-8' ) as f:
	f.write("hello data2\n")
	f.write("this is a test\n")
	f.write("this is a test of appending")


with open("data3.txt",'w',encoding = 'utf-8' ) as f:
	f.write("hello data2\n")
	f.write("this is a test\n")
	f.write("this is a test of appending")

import csv 

with open('dataset.csv') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',')
	for r in csv_reader:
		print(r)


print(csv_reader)




















