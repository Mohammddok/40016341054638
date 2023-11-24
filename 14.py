Num1 = int(input("Enter First Num :"))
Num2 = int(input("Enter Second Num :"))
L1 = []
count = 0

if Num1 > Num2 :
    Num1 = Num1+Num2
    Num2 = Num1-Num2
    Num1 = Num1-Num2

    
b = 0
for i in range(1, num+1):
    if (num % i == 0):
        b += i 

if (b ==num*2) :
    print("Yes")
else:
    print("No")
