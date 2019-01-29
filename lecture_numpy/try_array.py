import numpy as np

data = np.arange(20).reshape(4,4)

print(data)

#pip3

print(data.shape)
print(data.size)
# here size is a property of the data.
# this is not working, since size here is not a function.
# print(data.size())

# this does not work
# data = np.zeros(4,4)
# this is working
## (4,4) is a object in the function call
data = np.zeros((4,4))
# to generate zero matrix
print (data)

# this works
data = np.arange(20)*3
print(data)

##install numpy
##install pandas
##install scipy