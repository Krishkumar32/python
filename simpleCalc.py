# take input from user
num1=int(input("enter the value: \t")) 
# take operator input
opr=input("enter the opr. \t")
# save num1 in result
result=num1
while opr != "=":
    num2=int(input("enter the value: \t"))
    match opr:
        case '+':
            result=result+num2
        case '-':
            result=result-num2
        case '*':
            result=result*num2
        case '/':
            if num2==0:
                print("cannot divide by zero")
                exit(0)
            else:
                result=result/num2
        case _:
            print("enter the correct operator")
    opr=input("enter the opr. \t")
    
print(result)
