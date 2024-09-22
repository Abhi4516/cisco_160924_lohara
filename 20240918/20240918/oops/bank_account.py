class bank:
    def __init__(self,number,name,intital_amount=1000):
        self._number=number
        self._name=name
        self._balance=intital_amount

    def __rep__(self):
         return(f'number: {self._number},name : {self._name}, balance : {self._balance}')
    
    def __str__ (self):
        return self.__rep__()
    
    def deposit(self,amount):
        self._balance +=amount

    def withdraw(self,amount):
        if amount> self._balance:
            print('not enough balance')
    
        self._balance -= amount


rohit_account=bank(18274536277,'Rohit',4000000)           
#print(rohit_account)
rohit_account.deposit(1000000)
rohit_account.withdraw(500000000)
print(rohit_account)