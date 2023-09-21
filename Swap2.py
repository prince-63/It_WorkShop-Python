a = int(input("Enter a : "))
b = int(input("Enter b : "))

print("before swap a and b : ", a, b)

a = a + b
b = a - b
a = a - b

print("After swap a and b : ", a, b)