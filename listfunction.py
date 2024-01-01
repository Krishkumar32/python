#function for delete element from list:
#del
#pop()
#remove()
#clear

l=[10,20,30,40]
del l[1]
print(l)
print()

#in this pop method is to remove 2index value
l=[10,20,30,40]
l.pop(2)
print(l)
print()

#this method will show which value is remove
l=[10,20,30,40]
print(l.pop(2))
print(l)
print()

#this method will remove 40 
l=[10,20,30,40]
l.remove(40)
print(l)
print()

#this method clear all values 
l=[10,20,30,40]
l.clear()
print(l)
