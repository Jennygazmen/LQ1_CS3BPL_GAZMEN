#Perform and print the ff. math opts for all the age and allowances:

student1 = "Jenny B. Gazmen"
student2 = "Joshua Cortez"
student3 = "Florheim Wizard V. Mariano "

#Create Variables that contains their age in whole number
age1 = 23
age2 = 22
age3 = 22

#Create variables that contains their weekly allowance in decimal form
allowance1 = float(2000)
allowance2 = float(1500)
allowance3 = float(1800)

nameLen1 = len(student1)
nameLen2 = len(student2)
nameLen3 = len(student3)

print("Member 1 consist of",nameLen1 , "characters")
print("Member 2 consist of", nameLen2, "characters")
print("Member 3 consist of", nameLen3, "characters")

#add the age of member 1 - 3
result1 = age1 + age2 + age3
print("The sum of their age is", result1)

#subtract the age of all members
result2 = age1 - age2 - age3
print("The difference of their age is", result2)   

#multiply the age of all the members
result3 = age1 * allowance1
result4 = age2 * allowance2
result5 = age3 * allowance2
print(result3)
print(result4)
print(result5)


#perform and print, compare
compareAge1 = age1 - age2
compareAge2 = age2 - age3
print(compareAge1)
print(compareAge2)

#length mem1 -mem2: mem2 to mem3

lengthmem1 = nameLen1 - nameLen2
lengthmem2 = nameLen2 - nameLen3
print(lengthmem1)
print(lengthmem2)

