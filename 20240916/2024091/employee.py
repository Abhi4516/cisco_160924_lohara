class Employee:
    def __init__(self,name,address,code,a,b):
        self.name=name
        self.address=address
        self.code=code
        self.a=a
        self.b=b

    def add(a,b):
        return a+b
        


    def __str__(self):
        return f'{self.name},{self.address},{self.code},{self.a},{self.b}'

info=Employee('abhi','maharashtra',2345,4,5)
print(Employee.add(2,4))
print(info)        
    

