x={'key':2}
print(x['key'])
print(x.values())
#iterating through a dictionary
for key,value in x.items():
    print(key,value)
x['key2']=5
x['key3'] =8
print(x)

#del x['key'] deleting dictionary

#list comprehenesion
x = [[0 for x in range(5)] for x in range(5)]
print(x)

x = [m for m in range(100) if m % 6 ==0]
print(x)


for i in range(25):
    if i % 2 ==0:
        print(i)   


print(2%5)