labs = input("Enter the number of labs completed (up to 6): ")
quiz = input("Enter the number of quizzes completed (up to 6) : ")
ass1 = input("Enter the grade received for Assignment 1: ")
ass2 = input("Enter the grade received for Assignment 2: ")
ass3 = input("Enter the grade received for Assignment 3: ")
ass4 = input("Enter the grade received for Assignment 4: ")
mid1 = input("Enter the grade received for Midterm 1: ")
mid2 = input("Enter the grade received for Midterm 2: ")
final = input("Enter the grade received for the Final Exam: ")
midfinalprep = input("Enter the grade received for the Midterm and Final Preparation: ")
labsgr = ((float(labs)/6) * (20/100)) * 100
quizgr = ((float(quiz)/6) * (15/100)) * 100
ass1gr = float(ass1) * (4/100)
ass2gr = float(ass2) * (4/100)
ass3gr = float(ass3) * (4/100)
ass4gr = float(ass4) * (4/100)
mid1gr = float(mid1) * (12.5/100)
mid2gr = float(mid2) * (12.5/100)
finalgr = float(final) * (18/100)
midfinalprepgr = float(midfinalprep) * (6/100)
finalgrade = labsgr + quizgr + ass1gr + ass2gr + ass3gr + ass4gr + mid1gr + mid2gr + finalgr + midfinalprepgr
finalgraderound = round(finalgrade)
print("Your grade is " + str(finalgraderound))

