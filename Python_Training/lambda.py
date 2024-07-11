#lambda = one line anonyomous function
# syntax = lambda arguments : expression

x = lambda a,b : a + b
print(x(5,3))

t = lambda o: o + 10
print(t(15))

#map and filter

x = [1,6,3,5,6,5,11]

mp = map(lambda i:i+2,x)
print(list(mp))

#FILTER returns neither true or false
mp = filter(lambda i:i%2==0,x)
print(list(mp))