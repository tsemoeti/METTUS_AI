Thistuple =("learning","training","stipend")
print(type(Thistuple))

#slice operator

x = [0,1,2,3,4,5,6,7,8]
y = ["Dumelang", "Sanibona","Marriage","Peace"]
s = "Hello"

# slice=[start:stop:step]
print(x[2:0:-2])
print(x[::-1])

#set = unordered unique collection of data
S = {"apple","banana"}
print(type(S))


ss= {4,2,2,5,7}
ss.add(3)
ss.remove(5)
print(ss)

ss2 = {3,4,5,1}
ss3 = ss.union(ss2)
print(ss3)
print(ss.difference(ss2))

ss4 = ss.intersection(ss2)
print(ss4)


x = tuple(m for m in range(100) if m % 6 ==0)
print(x)
