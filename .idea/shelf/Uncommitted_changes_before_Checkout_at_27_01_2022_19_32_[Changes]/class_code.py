def decorator(func):
    def wrapper():
        print ("===============")
        
        func()
        
        print ("===============")
    return wrapper

def foo():
    print ("jestem udekorowany")
    
foo = decorator(foo)

foo()
