print("helloworld")

x = 10

if x < 0:
    print("X is smaller than 0.:")

else: 
	print("X is not smaller than 0.")



    x = 10

    if x < 0:
        print("X is smaller than 0.:")
    elif x > 10:
        print("X is bigger than 10.")
    else: 
       print("X is between 0 and 10.")

## don't use short form of a variable, use complete word are easy to look up variables later.

y = 10

if y < 0:
    print("Y is small")
elif y >= 10:
    print("Y is big.")
else: 
	print("error")

## always write "else:", else include all other case, can be used to check if there is error before. This is defencive programming.

## to allow inputting a number and enteracting with the program,  put a input function. input(), 
Y = int(input("enter value of Y"))

if y < 0:
    print("Y is small")
elif y >= 10:
    print("Y is big.")
else: 
	print("error")


## to write a loop

animals = [ "cat", "dog", "turtle", "bird"]

print(animals)

for x in animals:
	print(x)
	print(len(x))


# numbers = [1,2,3,4,5,6,7,8,9,10]

# for i in numbers:

#    print(i**2) 

number = range(1,11)
## but range start from zero.
print number

for i in number:
    print(i**2) 

# def complicated_function()
#    pass
## pass 


number2 = range(10)
for i in number2 :
    print((i+1)**2)


## this is not working, although it works in R
# number3= range(10)+1



### loop


def fib(n):
    result = []
    a,b = 0,1 
    while  a < n :
        result.append(a)
        a, b = b, a+b
    return result

print(fib(2000))

































