Numa = int(input("Enter Numa : "))
Numb = int(input("Enter Numb : "))
Numc = int(input("Enter Numc : "))

if Numa>Numb and Numa>Numc:
    print("First Num is bigger :%s ! " %(Numa))
elif Numc>Numa and Numb>Numc :
    print("Second Num is bigger : %s! "%(Numb))
elif Numc>Numa and Numc>Numa :
    print("3th Num is bigger : %s! "%(Numc))
else :
    print("c Nums are equal")
