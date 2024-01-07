n=int(input("enter the number of rows:"))
for i in range(1,n+1):   #this line create the rows start from 1 and end is n+1
    for j in range(1,i+1): #this line create column start from 1 and end is i+1
        print(j,end="")
    print()
        
