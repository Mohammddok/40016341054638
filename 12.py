Num = int(input("Enter Num :"))
count = 0 

for i in range(2,Num):
    if (Num%i==0):
        count += 1 

if count > 0 :
    print("H")
else:
    print("F")
    
