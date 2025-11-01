print("1. Create 5 variables of different data types (int, float, str, bool, list. Use print() and type() to display each variable and its type")
a=int(input("Enter your Number"))
print(f"Integer value is:{a}")
print(type(a))
b=float(input("Enter your decimal Number"))
print(f" Decimal value is:{b}")
print(type(b))
c=str(input("Enter your Name"))
print(f" String value is:{c}")
print(type(c))
d=bool(input("Are you student (Y/N):"))
print(f" Boolen value is:{d}")
print(type(d)) 
e=list(input("List of students:"))
print(f" List value is:{e}")
print(type(e))
print()

print("2.Print a sentence using variables:Example output — “My name is John and my age is 15.”(But the name and age must come from variables.")
name= "John"
age=15
print(f"My name is {name} and my age is {age}.")
print()
print("3.Take two numbers as variables and print their sum, difference, product, and quotient.")
Num1=int(input("Enter your Number"))
Num2=int(input("Enter your Number"))
print("Sum is", Num1+Num2)
print("difference is", Num1-Num2)
print("product is", Num1*Num2)
print("quotient is", Num1/Num2)
print()
print("4.Print the result of combining string and integer properly using f-string (avoid type error).")
name=str(input("Enter your Name"))
age=int(input("Enter your Age"))
print(f"My name is {name} and my age is {age}.")
print()
print()
print("Operators (Arithmetic, Relational, Logical, Assignment)")
print("6.	Use arithmetic operators to find: o	Square of a number o	Cube of another number o	Average of three numbers")
A=int(input("Enter your Number"))
B=int(input("Enter your Number"))
C=int(input("Enter your Number"))
print("Square of a number is:", A*A)
print("Cube of another number is:", B*B*B)
print("Average of three numbers is:", A+B+C%3)
print()
print("7.Compare two variables a and b using all relational operators (>, <, ==, !=, >=, <= Print True or False for each case.")
a1=int(input("Enter your Number"))
b1=int(input("Enter your Number"))
print("a1>b1:",a1>b1)
print("a1<b1:",a1<b1)
print("a1==b1:",a1==b1)
print("a1!=b1:",a1!=b1)
print("a1>=b1:",a1>=b1)
print("a1<=b1:",a1<=b1)
print()
print("8.	Use logical operators (and, or, not) to check: o	If a number is positive and even o	If a number is negative or zero")
ab1=int(input("Enter your Number"))
bc1=int(input("Enter your Number"))
if(ab1>0) and (ab1%2):
    print(ab1,"number is positive and even")
elif(bc1<0) or (bc1==0):
    print(bc1,"number is negative or zero")
else:
    print("Enter valid number")
    print()
print("9. To swap two variables without using a third variable (use arithmetic or assignment operators).")
M=10
N=20
print("assignment operators")
print("Before swapping:",M,N)
M,N=N,M
print("After swapping:",M,N)
print()
print("arithmetic operators")
print("Before swapping:",M,N)
M=M+N
N=M-N
M=M-N
print("After swapping:",M,N)
print()
print("10.	Take two numbers and check: o	Which one is greater o	Whether both are equal (Use conditional and comparison operators)")
n1=int(input("Enter your Number"))
n2=int(input("Enter your Number"))
if(n1>n2):
      print(n1,"is greater")
elif(n2>n1):
    print(n2,"is greater")
elif(n1==n2):
    print(n1,n2, "is equal")
else:
    print("Enter Valid number")
print()
print("11.Write a program that checks whether a given number is even or odd.")
number=int(input("Enter your Number"))
if(number%2==0):
    print(number, "IS EVEN NUMBER")
else:
    print(number, "IS ODD NUMBER")
print()
print("12.Write a program to find whether a number is positive, negative, or zero (use elif).")
Number=int(input("Enter your number"))
if(Number>0):
    print("Positive")
elif(Number<0):
        print("Negative")
elif(Number==0):
        print("Zero")
else:
    print("Number not valid")
print()
print("Write a program to display grade (A, B, C, D, Fail) based on marks")
Marks=int(input("Enter your Mark"))
if(Marks>=90):
         print("A GRADE")
elif(Marks>75 and Marks>=89):
         print("B GRADE")
elif(Marks>50 and Marks>=74):
         print("C GRADE")
elif(Marks>50):
    print("FAIL")
else:
    print("Not Valid Mark")
    print()
print("to check if a year is leap year or not using if-else")
year=int(input("Enter Year"))
if(year%4==0):
    if(year!=100 and year%400==0):
        print(year,"LEAP YEAR")
    else:
        print(year,"Not LEAP YEAR")
else:
    print(year,"Not LEAP YEAR")
print()
print("15.Write a program to check whether a person is eligible to vote (age ≥ 18).If not eligible, print how many years left to become eligible")
Age=int(input("Enter your Age"))
years_left = 18 - Age
if(Age>=18):
    print("ELIGIBLE TO VOTE")
else:
    print(f"You need to wait {years_left} to become eligible.")
print()
print()
print("16.Write a program that takes three numbers and prints which one is the largest.")
Num1=int(input("Enter your number"))
Num2=int(input("Enter your number"))
if(Num1>Num2):
    print(Num1,"Num1 is largest number")
else:
    print(Num2,"Num2 is largest number")
print()
print("17.	Using nested if, check: o	If a number is positive 	Check if it’s even or odd o	Else print it’s negative or zero")

Z=int(input("Enter Your Number"))
if(Z>0):
    if(Z%2==0):
        print("POSITIVE AND EVEN NUMBER")
    else:
      print("ODD NUMBER")
else:
    print("it’s negative or zero")
print()
print("o	“Child” if age < 13 o	“Teen” if age between 13–19 o	“Adult” if age between 20–59 o	“Senior Citizen” if age ≥ 60")
Age1=int(input("Enter Your Age:"))
if(Age1<13):
      print(Age1,"Child")
else:
    if(Age1<=19):
      print(Age1,"TEEN")
    else:
      if(Age1<=59):
        print(Age1,"ADULT")
      else:
        if(Age1>=60):
            print("SENIOR CITIZEN")
        else:
            print("Age is not valid")
print()
print("19.	Write a program that checks whether a character is a vowel or consonant. (Input a single alphabet letter and use if-elif-else.)")
Ch=input("Enter a Character")
li=['a','e','i','o','u','A','E','I','O','U']
if Ch in li:
      print(Ch," is VOWEL")
elif Ch.isalpha():
    print(Ch,"is CONSONANT")
else:
    print(Ch, "is not vowel and consonant")
print()
print("o	If all marks ≥ 40 → print “Pass” o	If any one subject < 40 → print “Fail” o	If average ≥ 90 → print “Outstanding” (use nested if)")
M1=int(input("Enter your Mark"))
M2=int(input("Enter your Mark"))
M3=int(input("Enter your Mark"))
Average=M1+M2+M3/3
if(M1>=40 and M2>=40 and M3>=40):
      print("PASS")
      if(Average>=90):
          print("OUTSTANDING")
else:
    print("FAIL")
        



























      
    





































      
























 
 
 
