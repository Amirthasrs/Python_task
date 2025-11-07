print("####### String Operators##########")
print("To concatenate given string to end of another string")
Firstname=input("Enter a Firstname :")
Lastname=input("Enter a Lastname :")
Fullname=Firstname+ Lastname
print("My Fullname is:",Fullname)
print()
print("If given string contain specified char values")
Address=input("Enter a Addrss :")
if("pincode" in Address):
    print("Address verified")
else:
    print("Address not verified")
print()
print("Convert into Lower Case")
LC=input("Enter a String :")
lc=LC.lower()
print(lc)
print()
print("Trim Whitespace")
Trim=input("Enter a String :")
T=Trim.strip()
print(T)
print()
print("Reverse string")
Rev=input("Enter a String :")
reverse=Rev[::-1]
print(reverse)
print()
print("")
print()
print()
print("******************TASK4.1********************")
print("Spaces replace with underscore")
S=input("Enter a String :")
S1=S.replace(" ","_")
print(S1)
print()
print("Create a string made of middle three character =Python123")
String="Python123"
C=String[3:6]
print(C)
print()
s="Helloworld"
d=""
for i in s:
    if not i.isdigit():
        d+=i
result=d[0].upper()+ d[1:-1]+ d[-1].upper()
print(result)
print()
print("To get a length of given string")
A=input("Enter a String :")
print("Legth of give string:",len(A))
print()
print(" No of occurance of given string repetition")
Tx="I am new to this office but not new to"
print("No of count in new:",Tx.count("new"))
print()
print("Count the no of words in string")
A=input("Enter a String :")
words=A.split()
print(words)
count=len(words)
print(count)
print()
print("Replace specified character")
S="The quickbrown fox jumps over the lazy dog"
s1=S.replace("d","f")
print(s1)
print()
print("Count vowels in string")
A=input("Enter a String :")
B=['a','e','i','o','u','A','E','I','O','U']
Count=0
for ch in A:
    if ch in B:
        Count=Count+1
print(Count)
print()
print("If string contains Whitespace")
A = input("Enter a String: ")

if " " in A:
    print("Whitespace found")
else:
    print("Whitespace not found")
print()
print("Remove all digits from string")
A = input("Enter a String: ")
B = ""

for ch in A:
    if not ch.isdigit():
        B = B + ch

print("Removing digits:", B)
print()
print("*********TASK************")
print("1. Length of name")
name=input("Enter your name:")
print("Legth of name is:" ,len(name))
print()
print("Convert into Upper Case")
LC=input("Enter a String :")
lc=LC.upper()
print(lc)
print()
print("Convert into Lower Case")
LC=input("Enter a String :")
lc=LC.lower()
print(lc)
print()
print(" No of count of given string a")
A=input("Enter a String :")
print("No of count a:",A.count("a"))
print()
print(" STARTSWITH")
A=input("Enter a String :")
print(A.startswith("Hello"))
print()
print("ENDSWITH")
A=input("Enter a String :")
print(A.endswith(".com"))
print()
print("Find the position of 'python' using find()")
A = input("Enter a String: ")
pos = A.find("python")   
print("'python' found at position:", pos)
print()
print("*************Java replace with python*****************")
S="Java is my first programming"
print("Before replace",S)
S1=S.replace("Java","Python")
print("After replace",S1)
print()
print("STRIP")
S=input("Enter a String :")
S1=S.strip()
print(S1)
print()
print()
print("CAPITALIZATION")
S=input("Enter a String :")
S1=S.capitalize()
print(S1)
print()
print("SPLIT")
S=input("Enter a String :")
S1=S.split()
print(S1)
print()
print("JOIN")
S="Amirtha","Abi"
print("&".join(S))
print()
print()
print("Is numeric")
S = input("Enter a String: ")
print(S.isnumeric())
print("Is alnum")
S = input("Enter a String: ")
print(S.isalnum())
print("Is digit")
S = input("Enter a String: ")
print(S.isdigit())
print("Is lower")
S = input("Enter a String: ")
print(S.islower())
print("Is upper")
S = input("Enter a String: ")
print(S.isupper())
S = input("Enter a String: ")
S1= S.swapcase()
print("After Swapcase",S1)
print("TITLE")
S = input("Enter a String: ")
S1= S.title()
print("After title",S1)
S = input("Enter a String: ")
S1= S.isspace()
print("Results:",S1)
print()
print("Count vowels in string")
A=input("Enter a String :")
B=['a','e','i','o','u','A','E','I','O','U']
Count=0
for ch in A:
    if ch in B:
        Count=Count+1
print(Count)
print()
print("Check Palindrome")
n1 = input("Enter a String: ")

if n1 == n1[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
print("Remove all digits from string")
A = input("Enter a String: ")
B = ""

for ch in A:
    if not ch.isdigit():
        B = B + ch

print("Removing digits:", B)
print()
print("Spaces replace with underscore")
S=input("Enter a String :")
S1=S.replace(" ","_")
print(S1)
print()

print("Remove all string")
A = input("Enter a String: ")
B = ""

for ch in A:
    if  ch.isdigit():
        B = B + ch
print(B)

print()
print("find all string start with capital")
A = input("Enter a String: ")
text = A.split()
B = " "
for ch in text:
    if  ch[0].isupper():
        B=B+ch
print(B)
print()
print()
print("Count how many times each letter occurs")

A = input("Enter a sentence: ")
for ch in set(A):            
    if ch.isalpha():        
        print(ch, "=", A.count(ch))
print()

print("Remove punctual")
A = input("Enter a sentence: ")
S=A.replace("!","") 
print(S)
print()
print("ENDSWITH")
A=input("Enter a String :")
print(A.endswith("@gmail.com"))
print()
print("REVERSE")
A=input("Enter a String :")
B=list(A)
B.reverse()
print(B)
































































