#Raising and exception
#e:g raise Exception("bad")
# eg: raise FileExistsError('Contact us webpage'

#try block
def using_exception():
    try:
        x = 7/0
    except Exception as e:
        print(e)    # e prints what the error is


def using_value_error():
    while True:
        try:
            my_input = int(input("Please enter a number: "))
        except ValueError:
            print("Invalid input please enter a number")  
        if my_input == 0:
            print("END GAME")
            break
        else:
            print(my_input)

def using_the_error():
    try:
        print(9/0)
    except ZeroDivisionError:
            print("Have you ever divided by zero before")   


def division(x,y):
    try:
        res = x/y
    except ZeroDivisionError:
        print("Error: divided by zero")  
    else:
        print(f"Your answer is: {res}") 
    finally:
        print("Finally block is always executed")    
              
#using_exception()
using_value_error()
#using_the_error()
#division(3,0)
#division(15,5)