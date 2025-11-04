print("print a number between 1 and 100 that are divisible by 6 by not by 9")
for i in range(1, 101):
    if i % 6 == 0 and i % 9 != 0:
        print(i)
print()
print("Sum of all odd number from 1 to 50")
sum=0
for i in range(1, 51):
    if i % 2!=0 :
        sum=sum+i
print("Sum of odd numbers:",sum)
print()
print(" numbers between 1 and 200  divisible by 4 and 6")
count=0
for i in range(1, 201):
    if i % 4==0 and i %6==0:
        count=count+1
print("Count:",count)
print()
print(" print the multiplication table of 1 to 10")
n=int(input("Enter multiplication table"))
for i in range(1,11):
    result=n*i
    print(f"{n} X {i} = {result}")
print()
print("find the factorial of given number")
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num, "is:", fact)
print()

print("Prime numbers between 1 and 50 are:")

for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
print()
print("sum of the digits of a number using arithmetic operations only")
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10    
    sum_digits = sum_digits + digit
    num = num // 10     

print("Sum of digits:", sum_digits)
print()
print("count how many numbers between 1 and 500 are perfect cubes")
count = 0

for i in range(1, 501):
    cube_root = round(i ** (1/3))  
    if cube_root ** 3 == i:          
        count = count + 1

print("Total perfect cubes between 1 and 500:", count)
print()
print("reverse a number using arithmetic only")
num = int(input("Enter a number: "))
count = 0
temp = num
rev = 0

while temp > 0:
    count = count + 1
    temp = temp // 10

for i in range(count):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)
print()
print("print numbers from 1 to 100 but skip those ending with the digit 5")
for i in range(1, 101):
    if i % 10 == 5:   
        continue
    print(i)














