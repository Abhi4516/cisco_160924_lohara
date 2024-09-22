class MyClass:
    class_var = 0
    
    @classmethod
    def class_method(cls):
        return cls.class_var
    
    @staticmethod
    def static_method():
        return "This is a static method."

print(MyClass.class_method())  # Output: 0
print(MyClass.static_method())  


class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        return self.engine.start()

car = Car()
print(car.start()) 
