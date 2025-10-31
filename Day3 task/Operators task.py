a=int(input("Enter your number"))
b=int(input("Enter your number"))
c=int(input("Enter your number"))
print("1. Add Two Numbers:",a+b)
print(" 2. Subtract Two Numbers:", a-b)
print("3. Multiply Two Numbers:", a*b)
print("4. Divide Two Numbers:", a/b)
print(" 5. Find Remainder:", a%b)
print(" 6. Square of a Number:", a**b)
print("7. Cube of a Number:" , a**3)
print("8. Average of Three Numbers:", a+b+c/3)
print()
print("9. Swap Two Variables")
d=int(input("Enter your number1"))
e=int(input("Enter your number2"))
print("Before swap:",d,e)

o=e
e=d
d=o
print("After swap:",d,e)
print()
print("10. Check Datatype")
Age=int(input("Enter your age"))
print(type(Age))
print()
print("11. Add Integer and Float")
f=int(input("Enter your height"))
g=float(input("Enter your weight"))
h= f+g
print(type(h))
print()
print(" 12. Simple Comparison")
num1=int(input("Enter your number"))
num2=int(input("Enter your number"))
print(num1>num2)
print()
print("13. Check Equal or Not")
num3=int(input("Enter your number"))
num4=int(input("Enter your number"))
print(num3==num4)
print()
print("14. Find Total and Average Marks")
num1=int(input("Enter your number"))
num2=int(input("Enter your number"))
num3=int(input("Enter your number"))
num4=int(input("Enter your number"))
num5=int(input("Enter your number"))
print("Total marks:", num1+num2+num3+num4+num5)
print("Total Average:", num1+num2+num3+num4+num5/5)
print()
Hour=int(input("Enter hours"))
print("15. Convert Hours to Minutes:", Hour*60)
print()
print("16. Calculate Simple Interest")
p=int(input("Enter your principle"))
r=int(input("Enter your rate"))
t=int(input("Enter your time"))
print("SI:",(p*r*t)/100)
print()
l=int(input("Enter your Length"))
b=int(input("Enter your bredth"))
print("17. Find Area of a Rectangle:",l*b)
print()
print("18. Check Positive or Negative")
Number=int(input("Enter your number"))
if(Number>0):
    print("positive")
else:
    print("Negative")
print()
print("19. Calculate Total Cost")
COI=int(input("Enter your Cost of item"))
NOI=int(input("Enter your Number of item"))
TOC=COI*NOI
print(TOC)
print()
print("20. Small Calculator")
Num1=int(input("Enter your number"))
Num2=int(input("Enter your number"))
print("Addition:",Num1+Num2)
print("Subtraction:",Num1-Num2)
print("Multiplication:",Num1*Num2)
print("Division:",Num1/Num2)
print("THANK YOU")



























