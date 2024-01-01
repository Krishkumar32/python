#function for update element from list
#insert()
#append()
#extends()


# this is update method
l=[20,30,40,50]
l[0]=10
print(l) 

#this line is method of insert values in index wise
print()
l=[20,30,40,50]
l.insert(1,25)
print(l) 

#in this we direct add the values
print()
l=[20,30,40,50]
l.append(60)
print(l) 

#in this we add the n values in l
print()
l=[20,30,40,50]
n=[40,50]
l.append(n)
print(l)  # output is l=[20,30,40,50,[40,50]]

#in this extend method will add the values in l direct
print()
l=[20,30,40,50]
n=[40,50]
l.extend(n)
print(l) 







