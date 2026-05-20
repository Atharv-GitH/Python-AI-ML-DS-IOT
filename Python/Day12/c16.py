

def add(a,b,c):

    print("in add")

    return a+b+c

add = lambda x,y : x + y

print(add(10,20,30))

print(add(10,20))

'''
op :

print(add(10,20,30))
      ^^^^^^^^^^^^^
TypeError: <lambda>() takes 2 positional arguments but 3 were given
'''
