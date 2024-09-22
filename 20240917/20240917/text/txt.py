with open('myfile2.txt' ,'r') as names :
    names=names.read()
    print(names)

#data={'one':1,'two':2}
file=open('/Users/abbade/Desktop/cisco/cisco_160924_lohara/20240917/text/name.txt','r')
new=file.read()


file1 = open("myfile2.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()

import pickle

'''with open('data.pickle','wb')  as file:
    pickle.dump(data,file)  



with open('data.pickle','rb') as dict:
    files=pickle.load(dict)

print(files)    '''
