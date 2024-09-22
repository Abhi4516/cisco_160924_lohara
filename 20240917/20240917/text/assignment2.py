



student_names=[]

names_lists=input('Enter the student name (give space): ').split()
set1=set(names_lists)
name_fsets=frozenset(set1)
name_dict={name:len(name) for name in name_fsets}
print(f'original list: {names_lists}')
print(f'no dulicates : {name_fsets}')
print(f'frozen sets: {name_fsets}')
print(f'dict : {name_dict}')  



import json

with open('myfile2.txt','w') as name_db:
    json.dump(name_dict,name_db)
print('dictonary written to json file')    

with open ('myfile2.txt','r') as name_db:
    name_dict2=json.load(name_db)
print(name_dict2)