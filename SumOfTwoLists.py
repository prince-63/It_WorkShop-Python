# write a program to create a list and print it.

ln = int(input("Enter list length : ")) 
lst1 = []
lst2 = []
sum = []

# input
for i in range (0, ln) :
    val = int(input("Enter your value : "))
    lst1.append(val)

# input
for i in range (0, ln) :
    val = int(input("Enter your value : "))
    lst2.append(val)

# sum
for i in range (0, ln) :
    sum.append(lst1[i] + lst2[i])

# output
print("list 1 is : ", lst1)
print("list 2 is : ", lst2)
print("sum of two lists : ", sum)
