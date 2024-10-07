#Data Storage, Strings and Printing

#Create a Variables that store the names of your groupmates
student1 = "Jenny B. Gazmen"
student2 = "Joshua Cortez"
student3 = "Florheim Wizard V. Mariano "

#Create Variables that contains their age in whole number
age1 = str(23)
age2 = str(22)
age3 = str(22)
#Create variables that contains their weekly allowance in decimal form

allowance1 = float(2000)
allowance2 = float(1500)
allowance3 = float(1800)

# Print all results formated as follows: use concat
print(student1, student2, student3, age1, age2, age3, allowance1, allowance2, allowance3)

#Teamname: Member 1: StudentName, his age is "age", allowance per week is "allowance"
teamName = "JQuery"
print("TEAM NAME:",teamName)
print("Member 1:", student1, "her age is", age1, "and her allowance per week is", allowance1)
print("Member 2:", student2, "his age is", age2, "and his allowance per week is", allowance2)
print("Member 3:", student3, "his age is", age3, "and his allowance per week is", allowance3)

#Create variables to store the length of the names of the members and print the formatted as follow:
#Print member 1-3 consists of length chracters
nameLen1 = len(student1)
nameLen2 = len(student2)
nameLen3 = len(student3)

#Print the length of the members
print("Member 1 consist of",nameLen1 , "characters")
print("Member 2 consist of", nameLen2, "characters")
print("Member 3 consist of", nameLen3, "characters")
