subject1=int(input("Enter the marks of subject 1: "))
subject2=int(input("Enter the marks of subject 2: "))
subject3=int(input("Enter the marks of subject 3: "))   
total=subject1+subject2+subject3
percentage=(total/300)*100
print("Total marks:",total)
print("Percentage:",percentage)
if percentage>=90:
    print("Grade: A")
elif percentage>=80:
    print("Grade: B")               
elif percentage>=70:
    print("Grade: C")
elif percentage>=60:
    print("Grade: D")
elif percentage>=40:
    print("Grade: E")
else:
    print("Grade: F")
# Program to calculate total marks, percentage and grade based on marks in three subjects.