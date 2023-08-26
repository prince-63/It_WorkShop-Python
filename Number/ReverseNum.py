num = int(input("Enter a num : "))

reverse = 0

print("Number is a : ", num)

while(num > 0) :
    #r = reminder 
    r = num % 10
    reverse = reverse * 10 + r
    num = int(num / 10)

print("reverse number is : ", reverse)