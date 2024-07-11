from array import*

array_num = array('i',[2,2,3,5,6])

for i in array_num:
    print(i)


array_num.append(7)
print(array_num)

print(array_num.itemsize)

#write a code import an array module and display the name space

for name in array.__dict__:
    print(name)

class Student:
    def __init__(self, student_name, student_number):
        self.student_name = student_name
        self.student_number = student_number

    
    def __str__(self):
        return f"{self.student_name} ({self.student_number})"    

S1 = Student("Wendy", 18677)     
print(S1.__dict__)  
print(S1.student_name)
print(S1)
        
class Car:
    def __init__(self, model, type, color, petrol_type):
        self.model = model
        self.type = type
        self.color = color
        self.petrol_type = petrol_type

    def __str__(self) :
        return f"The car model is a {self.model}.\nThe car type is {self.type}.\nThe car color is {self.color}.\nThe car petrol type is {self.petrol_type}.   "

Car1 = Car("Ford Ranger", "Double Cab", "Matt Black", "Diesel")   
print(Car1)    

