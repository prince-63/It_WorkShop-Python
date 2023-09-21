ln = int(input("Enter list length : ")) 
lst = []

# input
for i in range (0, ln) :
    val = int(input("Enter your value : "))
    lst.append(val)

# before
print("Before sort list is : ", lst)

# sort 
for i in range(0, ln) :
    for j in range(0, ln - i - 1) :
        if(lst[j] > lst[j + 1]) :
            tmp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = tmp

# After
print("After sort list is : ", lst)

