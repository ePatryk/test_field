class Movie():
   
    def __init__(self, title, storyline, hero, trailer):
       
        self.title=title
        self.storyline=storyline
        self.hero=hero
        self.trailer=trailer
        
    def config(self):
        
        print(self.title, self.storyline, self.hero, self.trailer)
        
Matrix = Movie("Matrix", "Action", "Neo", "yt:Matrix")

Matrix.config()


Southpark = Movie("Miasteczko Southpark", "Comedy", "Kenny", "yt:Southpark")


Southpark.config()

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
