

class Demo:

    def __demo__(self):
        print("Constructor")

    def __new__(cls):
        print("Memory Allocation")
        return super().__new__(cls)

obj1 = Demo ()
obj2 = Demo ()

print(obj1)
print(obj2)

'''
Memory Allocation
Memory Allocation
<__main__.Demo object at 0x7dd25a8ffbf0>
<__main__.Demo object at 0x7dd25a8ffd70>
'''
