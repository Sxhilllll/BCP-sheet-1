#Q9 WAP to check if a  year is leap year or not
n = int(input("Enter the year"))
if (n % 4== 0 or n % 100== 0):
    print("Year is a leap year")
else:
    print("Year is not a leap year")
    