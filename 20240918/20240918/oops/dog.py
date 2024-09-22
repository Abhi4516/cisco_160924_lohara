nums =[10,20,30,40]
'''
nums_add=(lambda s,num:s+num)
print(nums_add(nums,10))'''


from functools import reduce

list1 = [-1, 3, 7, 99, 0]

print(reduce(max, list1))


new=reduce(lambda num,n:n if n>num else num,nums)

print(new)



