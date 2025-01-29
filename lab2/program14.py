marks1=float(input("Enter marks for subject1 : "))
marks2=float(input("Enter marks for subject2 : "))
marks3=float(input("Enter marks for subject3 : "))
total_avg=(marks1+marks2+marks3)/3

if marks1 <= 39:
    grade1 = 'F'
elif 40 <= marks1 <= 44:
    grade1 = 'P'
elif 45 <= marks1 <= 49:
    grade1 = 'C'
elif 50 <= marks1 <= 54:
    grade1 = 'B'
elif 55 <= marks1 <= 59:
    grade1 = 'B+'
elif 60 <= marks1 <= 69:
    grade1 = 'A'
elif 70 <= marks1 <= 79:
    grade1 = 'A+'
elif 80 <= marks1 <=100:
    grade1='O'

if marks2 <= 39:
    grade2 = 'F'
elif 40 <= marks2 <= 44:
    grade2 = 'P'
elif 45 <= marks2 <= 49:
    grade2 = 'C'
elif 50 <= marks2 <= 54:
    grade2 = 'B'
elif 55 <= marks2 <= 59:
    grade2 = 'B+'
elif 60 <= marks2 <= 69:
    grade2 = 'A'
elif 70 <= marks2 <= 79:
    grade2 = 'A+'
elif 80 <= marks2 <= 100:
    grade2 = 'O'

if marks3 <= 39:
    grade3 = 'F'
elif 40 <= marks3 <= 44:
    grade3 = 'P'
elif 45 <= marks3 <= 49:
    grade3 = 'C'
elif 50 <= marks3 <= 54:
    grade3 = 'B'
elif 55 <= marks3 <= 59:
    grade3 = 'B+'
elif 60 <= marks3 <= 69:
    grade3 = 'A'
elif 70 <= marks3 <= 79:
    grade3 = 'A+'
elif 80 <= marks3 <= 100:
    grade3 = 'O'
print(f"Your total average is {total_avg}")
print(f"Grade of subject 1 : {grade1}")
print(f"Grade of subject 2 : {grade2}")
print(f"Grade of subject 3 : {grade3}")
