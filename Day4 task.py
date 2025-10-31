print("check whether a number is positive, negative, or zero")
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
print("check whether a number is even or odd")
Number1=int(input("Enter your number"))
if(Number1%2==0):
    print(Number1,"EVEN")
else:
    print(Number1,"ODD")
print()
print("check if a person is eligible to vote (age ≥ 18)")
Age=int(input("Enter your Age"))
if(Age>=18):
    print("ELIGIBLE TO VOTE")
else:
    print("NOT ELIGIBLE TO VOTE")
print()
print("check if a student passed or failed based on marks")
Mark=int(input("Enter your Mark"))
if(Mark>=35):
      print("student passed")
else:
    print("student passed")
    print()
print("find the largest of two numbers")

Num1=int(input("Enter your number"))
Num2=int(input("Enter your number"))
if(Num1>Num2):
    print(Num1,"Num1 is largest number")
else:
    print(Num2,"Num2 is largest number")
print()
print("Write a program to display grade (A, B, C, D, Fail) based on marks")
Marks=int(input("Enter your Mark"))
if(Marks>90 and Marks>=100):
         print("A GRADE")
elif(Marks>80 and Marks>=90):
         print("B GRADE")
elif(Marks>70 and Marks>=80):
         print("C GRADE")
elif(Marks>60 and Marks>=70):
        print("D GRADE")
elif(Marks>60):
     print("C GRADE")
else:
    print("FAIL")
    
print()
print("Write a program to print the day name based on a number (1–7)")
Day=int(input("Enter Your Number"))
if(Day==1):
    print("SUNDAY")
elif(Day==2):
     print("MONDAY")
elif(Day==3):
    print("TUESDAY")
elif(Day==4):
    print("WEDNESDAY")
elif(Day==5):
    print("THURSEDAY")
elif(Day==6):
    print("FRIDAY")
elif(Day==7):
    print("SATURDAY")
else:
    print("Enter valid number")
    print()
    
print("Check whether a character is an alphabet, digit, or special character.")

Char = input("Enter your character: ")

if Char.isalpha():
    print(Char, "is an alphabet.")
elif Char.isdigit():
    print(Char, "is a digit.")
else:
    print(Char, "is a special character.")

print()

print("find the largest among three numbers.")
N1=int(input("Enter your number"))
N2=int(input("Enter your number"))
N3=int(input("Enter your number"))
if(N1>N2) and (N1>N3):
    largest=N1
elif(N2>N1) and (N2>N3):
    largest=N2
else:
    largest=N3
print(largest,"is largest number")
print()
print("Display a message based on temperature (e.g., Hot, Warm, Cool, Cold)")

Temp = input("Enter temperature (Hot, Warm, Cool, Cold): ")

if Temp == "Hot":
    print("Temperature is Hot")
elif Temp == "Warm":
    print("Temperature is Warm")
elif Temp == "Cool":
    print("Temperature is Cool")
elif Temp == "Cold":
    print("Temperature is Cold")
else:
    print("Enter a valid temperature (Hot, Warm, Cool, or Cold)")

print("check whether a number is positive and even using nested if")
num=int(input("Enter Your Number"))
if(num>0):
    print("POSITIVE")
    if(num%2==0):
        print("EVEN")
    else:
        print(num,"is not an even number")
else:
    print(num,"is not a postive number")
    print()
print("•  Write a program to simulate a login system that checks username and password using nested if.")

Name = input("Enter your name: ")
PW = input("Enter your password: ")

if Name == "Ram":
    print("Valid Username")
    if PW == Name:
        print("Valid Password, Login successfully")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")

print()

print("To check if a person is eligible for a job:")
age= int(input("Enter your Age"))
Exp= int(input("Enter your Experience"))
if(age>=18 and Exp>2):
    
    print("Eligible for Job")
else:
    print("Not Eligible for Job")
    print()
print("to check if a year is leap year or not using if-else")
year=int(input("Enter Year"))
if(year%4==0):
    print(year,"LEAP YEAR")
else:
    print(year,"Not LEAP YEAR")
print()
print("To check whether a student qualifies for a scholarship:")

M=int(input("Enter your mark"))
A=int(input("Enter your Attendance"))
if(M >= 85) and (A>=90):
    print("Student qualifies for a scholarship")
else:
    print("Student not qualifies for a scholarship")




















    

              























          
          
  
