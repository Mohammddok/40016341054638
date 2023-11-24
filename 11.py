Num1 = int(input("Enter First Num :"))
Num2 = int(input("Enter Second Num :"))
L1 = []
for i in range(Num1+1,Num2):
    if (i%2 ==0):
        L1.append(i)
print(L1)


