

class SingleTonMeta(type):
    
    instance = None

    def __call__(cls, *args, **kwargs):
        
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        
        return cls.instance

class Demo(metaclass = SingleTonMeta):
    
    def __init__(self):
        print("Constructor")

class DemoChild(Demo):
    
    def __init__(self):
        print("DemoChild Constructor")

obj1 = DemoChild()
obj2 = DemoChild()

print(obj1)
print(obj2)
print(type(Demo))
print(type(DemoChild))

'''
DemoChild Constructor
<__main__.DemoChild object at 0x7e105d56dfd0>
<__main__.DemoChild object at 0x7e105d56dfd0>
<class '__main__.SingleTonMeta'>
<class '__main__.SingleTonMeta'>
'''
