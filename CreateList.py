# write a program to create a list and print it.

ln = int(input("Enter list length : ")) 
lst = []

# input
for i in range (0, ln) :
    val = int(input("Enter your value : "))
    lst.append(val)

# output
print("list is : ", lst)
