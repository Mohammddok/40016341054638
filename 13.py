Num1 = int(input("Enter First Num :"))
Num2 = int(input("Enter Second Num :"))
L1 = []
count = 0

if Num1 > Num2 :
    Num1 = Num1+Num2
    Num2 = Num1-Num2
    Num1 = Num1-Num2

for numb in range(Num1+1, Num2):
    for j in range(2,numb):
        if (numb%j==0):
            count += 1 
            break
        if count != 0 :
            L1.append(numb)
            break
print(L1)
