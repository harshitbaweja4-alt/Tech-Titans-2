# Student Marks Analyzer
# Write a program that accepts the marks obtained by a student in five subjects.
# The program should determine the highest marks, lowest marks, and average marks obtained by the student, and display all three results.

# Variables to Store Highest, Lowest and Average Marks
highestMarks = 100
lowestMarks = 0


# Taking Marks for Five Subjects as Input
# Taking Marks for Five Subjects as Input
subject1 = int(input("Enter Marks for Subject 1: "))
subject2 = int(input("Enter Marks for Subject 2: "))
subject3 = int(input("Enter Marks for Subject 3: "))
subject4 = int(input("Enter Marks for Subject 4: "))
subject5 = int(input("Enter Marks for Subject 5: "))

# Initialize Highest and Lowest with the first subject's marks
highestMarks = subject1
lowestMarks = subject1

# Finding the Highest Marks
if subject2 > highestMarks:
    highestMarks = subject2
if subject3 > highestMarks:
    highestMarks = subject3
if subject4 > highestMarks:
    highestMarks = subject4
if subject5 > highestMarks:
    highestMarks = subject5

# Finding the Lowest Marks
if subject2 < lowestMarks:
    lowestMarks = subject2
if subject3 < lowestMarks:
    lowestMarks = subject3
if subject4 < lowestMarks:
    lowestMarks = subject4
if subject5 < lowestMarks:
    lowestMarks = subject5

# Calculating the Average Marks (added parentheses)
avg = (subject1 + subject2 + subject3 + subject4 + subject5) / 5

# Displaying the Results
print(f"Highest: {highestMarks}")
print(f"Lowest: {lowestMarks}")
print(f"Average: {avg}")