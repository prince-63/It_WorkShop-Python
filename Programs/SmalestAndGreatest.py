import sys

smalest = sys.maxsize
gretest = 0

for i in range(5) :
    num = int(input("Enter a num : "))
    if(gretest < num) :
        gretest = num

    if(smalest > num) :
        smalest = num


print("smallest number is : ", smalest)
print("gretest number is : ", gretest)