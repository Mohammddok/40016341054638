Num1 = int(input("Enter First Num :"))
Max = Num1 
Min = Num1 
count = 1 

while count<100:
    Num2 = int(input("Enter Num2 : "))
    if Num2 > Max :
        Max = Num2
    elif Num2<Min :
        Min = Num2 
    count +=1 
print("Max is %s"%(Max))
print("Min is %s"%(Min))
