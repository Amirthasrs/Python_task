print("*** WHILE LOOP***")
print()
print("print the numbers from 10 down to 1")
i=10
while(i>=1):
    print(i)
    i=i-1
print("Sum of even digit in a number")
num=int(input("Enter a number:"))
sum=0
while num>0:
    digit=num%10
    if digit %2==0:
        sum+=digit
    num//=10
print("Total sum of even numbers:",sum)
print()

print("Count how many digits are in a number")
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10   
    count = count + 1
print("Number of digits:", count)
print()

print("Palindrome")
n1 = int(input("Enter a number: "))
temp = n1
rev = 0
while n1 > 0:
    digit = n1 % 10
    rev = rev * 10 + digit
    n1 = n1 // 10

if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")
print()
print("Find the reverse of a number")
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10        
    rev = rev * 10 + digit   
    num = num // 10         

print("Reversed number:", rev)
print()
print("Print fibonacci series up to 100")
a = 0
b =1
print("Fibonacci series up to 100:")

while a <= 100:
    print(a)
    a = b
    b = a+b
print()
print("Power of number manually")
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1
count = 0

while count < exponent:
    result = result * base
    count = count + 1

print("Result:", result)
print()
print("dividing number by 2 become less than 1 and count how many division")
num=int(input("Enter a number"))
count=0
while num>=1:
    num= num/2
    count= count+1
print("No of division:", count)
print()
print("print the digit of a number from last to first pne per line")
num = int(input("Enter a number: "))

while num > 0:
    digit = num % 10
    print(digit)          
    num = num // 10
print()
print("Sum of the squares of digit")
num = int(input("Enter a number: "))
sum_sq = 0

while num > 0:
    digit = num % 10         
    sum_sq = sum_sq + (digit * digit)  
    num = num // 10           

print("Sum of squares of digits:", sum_sq)

















