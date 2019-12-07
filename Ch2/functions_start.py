#
# Example file for working with functions
#

# define a basic function
def function1():
    print("I am a function")


# function that takes arguments
def function2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(number, x=1):
    result = 1
    for i in range(x):
        result = result * number
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# function1()
# print(function1())
# print(function1)

# function2(10, 20)
# print(function2(10, 20))
# print(cube(3))

# print(power(3, 4))
# print(power(x=100, number=100))

print(multi_add(4, 5, 20, 140, 3))
