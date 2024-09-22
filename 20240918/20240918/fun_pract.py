
'''lam=(lambda x:x*x)
print(lam(4))

def fun(first:int=1,second:int=0):
    return first-second

print(fun())
print(fun(10,5))



def fun1(*args):
    return args
print(fun1(10,1,2,3)) '''





'''def change_name(names,index,name):
    names[index]=name

names=['abhi','abhijeet']  

change_name(names,0,'abhijeet')
print(names) 


def args(a,b,*args):
    sum=a+b
    if (len(args)>0):
       for num in args:
         sum +=num

    return sum
print(args(10,20,30)) 



def args(a,b,**args):
    sum=a+b
    if (len(args)>0):
       for i in args:
            sum += args[i]

    return sum
print(args(10,20,sec=34,sec2=45)) 



def fact(n):
    if n<1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))     

import math
def prime(n):
    a=int(math.sqrt(n))
    for i in range(2,a+1):
        if n % i ==0:
            return False
        else:
            return True
        
print(prime(625))     '''   



nums=[10,20,30,40,50,60]
sum=0
for i in nums:
     sum += i
avg=sum/len(nums)
print(avg)     

