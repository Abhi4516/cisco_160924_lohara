
def is_odd(n):
   if n/2 !=0:
      return True
   return False

def is_even(n):
   if n/2 ==0:
      return True
   return False

def is_prime(n):
    for i in range(2, n/2):
         if n%i ==0:
             return False
         
         return True 
             