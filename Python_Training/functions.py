# *Args  and **Kwargs
#Args = arguments
#kwargs = key word arguments
#unpack operator, seperates all elements in a collectioon into individual elements
#* is used to unpack tuples
#** used to unpack dictionaries

def func(*args,**kwargs):
    pass

x = [1,4,5,6,7,3,4]
print(x)
print(*x)

def func2(x,y):
    print(x,y)
    pairs =[(1,2),(3,4)]
    for pair in pairs:
        print(*pair)

x = (1,2)
y = (3,4)
func2(x,y)

tuple1 = (1,2,3,4,5)
print(*tuple1)    


def func3(*args, **kwargs):
    print(*args)  
    print(**kwargs)  
func3((1,2,3,4,5),{"Key": 1})

#scope- an area in which parts of the program can access a variable
#global variable- can be accessed throughout the code decelared at the top of the code
    #allows you to change a variable outside of its current scope. Global key is on required for altering the variable value
#local variable- defined inside a function can only be used inside that function
#enclosing variable-
#builtin variables -

x = "Romeo"
def func4(name):
    global x
    x = name
print(x)
func4("changed")
print(x)  





