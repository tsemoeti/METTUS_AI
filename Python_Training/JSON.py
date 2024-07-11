#JSOM, uses strings, numbers, objects and arrays
#importing Json module with it's libraries
import json

json_obj = '{"Name":"David", "Class": "Grade 1K", "Age":6}' #JSOn String
python_obj = json.loads(json_obj) #Parse json string to load and become a python dictionary
print("\nJason Data")
print(python_obj)
print("\nName:", python_obj["Name"])
print("Class:", python_obj["Class"])
print("Age:", python_obj["Age"])


python_object = {"Name":"David", "Class": "Grade 1K", "Age":6} #initialize python dictionary
json_object = json.dumps(python_object) #parse the python_obect and use the dump method to create a JSon object
print(type(json_object))
print(json_object)


#Python objects into strings

Json_dict = json.dumps({"Name":"David", "Class": "Grade 1K", "Age":6})
Json_list =json.dumps(["green", "orange", "Pink"])
Json_string = json.dumps("Money")
Json_number1 = json.dumps(78)
Json_number2 = json.dumps(387)
Json_true = json.dumps(True)
Json_False = json.dumps(False)
Json_None = json.dumps(None)



print("Json Dictionary:" , Json_dict)
print("Json List: ", Json_list)
print("Json String: ", Json_string)
print("Json number_1: ", Json_number1)
print("Json number_2: ", type(Json_number2))
print("Json True:" , Json_true)
print("Json false:" , Json_False)
print("Json None:" , Json_None)

#Write code to convert json encoded data into python objects

Json_dict1 = json.loads('{"Name":"David", "Class": "Grade 1K", "Age":6}')
Json_list1 =json.loads('["green", "orange", "Pink"]')
Json_string1 = json.loads('["Money"]')
Json_number2 = json.loads('[78]')
Json_number3 = json.loads('[387]')

print("Python Dictionary:" , Json_dict1)
print("Python List: ", Json_list1)
print("Python String: ", Json_string1)
print("Python number_1: ", Json_number2)
print("Python number_2: ", Json_number3)

#instance, is a json document this is being validated and described

def encode_complex(object):
    if isinstance(object,complex):
        return object.real, object.imag
    raise TypeError(repr(object) + "is not JSon serialized")

complex_object = json.dumps(2 + 3j, default = encode_complex)
print(complex_object)





