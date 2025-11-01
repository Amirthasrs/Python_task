Name = input("Enter Your Name: ")
Age = int(input("Enter Your Age: "))
Course = input("Enter Your Course: ")

if Age >= 18 and Age <= 35:
    print("Your age is eligible for the course.")
    print("Welcome to Junior Data Analyst Course!\n")
    
    Attendance = int(input("Enter your attendance percentage: "))
    
    if Attendance >= 70:
        print("Successfully 70% attendance achieved in 10 days.")
        print("You are eligible for ₹12,000 incentive.")
        
        Completion = input("Have you completed the course? (yes/no): ").lower()
        
        if Completion == "yes":
            print("Successfully completed the course.")
            print("You are eligible for ₹6,000 incentive.")
            
            placement = input("Are you placed in any company? (yes/no): ").lower()
            
            if placement == "yes":
                print("Congrats on your hard work!")
                print("You are eligible for ₹4,800 incentive.")
            else:
                print("Sorry, try attending more interviews. Best of luck!")
        else:
            print("Course not completed successfully.")
    else:
        print("Your attendance is below 70%. You are automatically dropped from the course.")
else:
    print("Your age criteria is not fulfilled. You are not eligible for this course.")
