L1 = []

for x in range(0,10):
    L1.append(int(input("Enter Num :")))

print(L1)
def sort(get_list):
    for i in range(1, len(get_list)):
        if(get_list[i]<get_list[i-1]):
            j = i 
            while L1[j] < get_list[j-1] and j>0:
                get_list[j],get_list[j-1] = get_list[j-1], get_list[j]
                j = j-1
    return get_list

print(sort(L1))
