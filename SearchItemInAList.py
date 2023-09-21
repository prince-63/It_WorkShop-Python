ln = int(input("Enter list length : ")) 
lst = []
ans = 0

# input
for i in range (0, ln) :
    val = int(input("Enter your value : "))
    lst.append(val)

src = int(input('Enter your search value : '))

# searching
for i in range(0, ln) :
    if(lst[i] == src) :
        ans = 1
        break

# check
if(ans == 1) :
    print("Item present.")
else :
    print("Item not present.")