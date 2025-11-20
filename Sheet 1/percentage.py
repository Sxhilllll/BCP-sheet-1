#Input the percentage from the user and assign the grade according to the %age.
percent =int(input("Enter your percentage: "))
if percent>=90 and percent<=100:
 print("Grade = O")
elif percent<90  and percent>=80:
 print("Grade = A+")
elif percent<80  and percent>=70:
 print("Grade = B")
elif percent<70  and percent>=60:
 print("Grade = C")
elif percent<60  and percent>=50:
 print("Grade = D")
elif percent<50  and percent>=40:
 print("Grade = E")