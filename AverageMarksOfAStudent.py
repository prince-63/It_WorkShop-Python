std = ['first', 'second', 'third'] # students
sub = ['english', 'hindi', 'science'] 
roll = ['1', '2', '3'] 

# marks of a each student -- subject wise
eng = [10, 10, 10] 
ind = [9, 9, 9] 
sci = [8, 8, 8] 

print('Subject : ', sub)
print('Student : ', std)

src = int(input("Enter a roll of a student to find a details : "))
for i in range(0, len(std)) :
    if(i + 1 == src) :
        total_marks = eng[i] + ind[i] + sci[i]
        percentage = (total_marks / 30) * 100
        print('Name : ', std[i])
        print('Roll : ', roll[i])
        print('English : ', eng[i])
        print('Hindi : ', ind[i])
        print('Science : ', sci[i])
        print('Total marks : ', total_marks)
        print('Percentage : ', percentage)