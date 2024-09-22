



intt=[]
n=int(input('Enter the no : '))
for i in range(n):
    name=int(input('Enter the int :  '))
    intt.append(name)

print(intt)


set1=set(intt)
int_fsets=frozenset(set1)
int_dict={int_lists:int_lists*int_lists for int_lists in int_fsets}
print(f'original list: {intt}')
print(f'no dulicates : {int_fsets}')
print(f'frozen sets: {int_fsets}')
print(f'dict : {int_dict}')  





'''import json

with open('myfile2.txt','w') as name_db:
    json.dump(name_dict,name_db)
print('dictonary written to json file')    

with open ('myfile2.txt','r') as name_db:
    name_dict2=json.load(name_db)
print(name_dict2)'''