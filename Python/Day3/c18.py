x = 100
y = 200

print(id(x))        #1000
print(id(y))        #2000

a = 260
b = 260
x = 260

print(id(x))        #3000
print(id(a))        #3000
print(id(b))        #3000
