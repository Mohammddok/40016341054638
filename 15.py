Num1 = int(input("Enter First Num :"))
Num2 = int(input("Enter Second Num :"))
L1 = []


if Num1 > Num2 :
    Num1 = Num1+Num2
    Num2 = Num1-Num2
    Num1 = Num1-Num2

for i in range (Num1, Num2+1):
    count = 0
    for j in range(1,i+1):
        if (i%j ==0):
            count += j  
    if (count== 2*i):
        print("True")
        
    else:
        print("False")
print(L1)        
