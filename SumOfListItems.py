# write a program to create a list and print it.

ln = int(input("Enter list length : ")) 
lst = []
sum = 0

# input
for i in range (0, ln) :
    val = int(input("Enter your value : "))
    lst.append(val)
    sum = sum + val

# output
print("list is : ", lst)
print("sum of all list items : ", sum)
