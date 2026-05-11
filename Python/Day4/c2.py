x = 10
y = 10

print(id(x))        #1000
print(id(y))        #1000

y = 50

print(id(x))        #1000
print(id(y))        #2000
