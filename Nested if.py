Name= input("Enter Your Name")
Age= input("Enter Your Age")
Course= input("Enter Your Course")
if(Age>=18 and Age>=35):
    print("Your age is eligible for course")
    print("Welcome to Junior Data Analyst Course")
    print()
Attendance= int(input("Enter your attendance percentage"))
if(Attendance>=70):
    print("Sucessfully 70% of attendance in 10 days")
    print("You are eligible for rs 12,000 incentive")
    Completion=true
    if(Completion==true):
         print("Sucessfully Completed course")
         print("You are eligible for rs 6,000 incentive")
         placement=("Are you placed any company")
         if(placement==yes):
             print("Congrats for your hardwork")
             print("You are eligible for rs 4,800 incentive")
         else:
                 print("Sorry, Attend more company.Best of luck")
    else:
        print("Course not completed sucessfully")
  else:
      print("Your attendance below 70%, automatically dropout from the course")
else:
    print("Our age criteria not fullfilled. you are not eligible")
    
