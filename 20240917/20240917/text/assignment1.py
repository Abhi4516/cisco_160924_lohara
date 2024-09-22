

list=[]
n=int(input('Enter the no : '))
for i in range(n):
    name=input('Enter the fruit name :  ')
    list.append(name)

print(list)

tuple1=tuple(list)


for j in range(len(list)):
     file1 = open("myfile3.txt", "w")  
     file1.write(f"{list[j]},\n")
     