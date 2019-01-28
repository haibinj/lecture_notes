def fib(n):
    result = []
    a,b = 0,1 
    while  a < n :
        result.append(a)
        a, b = b, a+b
    return result

print(fib(2000))

## while is a loop. 
## append() adds a object to the existing object array.

print("\n")

a = 1.3
b = 2 - 0.7

if (a == b):
	print("haha")

a = 10/3
b = 3.333333

if (a == b):
	print("hahaha")
else: print("no")

## floating number could cause some problem.

### more about array--------------

stack = [1,2,3]
stack.append(5)
print(stack)

print(stack.pop())
print(stack.pop())
print(stack)


## pop() can delete a element, this can work as a loop. and it is very efficient compared to other way of loop.

## popleft.


####---------------
results = []
for i in range(10):
	results.append(i**2)

print(results)

results = list(map(lambda i:i**2, range(10)))

print(results)

## lambda is special in python, it is a function define name. a function without a name. it is useful to define a function that only use for once. 



###-------------

results = [i**2 for i in range(10)] 
# this is the same with the last code, it is easy to understand.

## search python document list.

## matrix is an array of array, but it is slow. need to use numeric python.


###-------------
## in array, sequence matters; in set, sequence doesnot matter.
#only unique item are recognized. convinient in data download from internet.
# but in version before 3.5 this is not the case
fruit = {'apple','banana','pear','pineapple','peach','orange','apple'}
print(fruit)

tech = {'apple','blackberry'}
print(fruit - tech)

dict([('sape',4139),('guido',4127),('jack',4212)])

####---------------

















