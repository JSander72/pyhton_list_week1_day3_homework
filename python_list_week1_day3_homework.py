grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)

print(grades) 

#--------------------------#

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
total = sum(grades)
print("The sum of all the grades is : ", total)
average = total / len(grades)
print(average)

#--------------------------#

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temperatures = temperatures[7:14]  
print(second_week_temperatures)

#--------------------------#

above_100 = temperatures[23:]
print(above_100)

#--------------------------#

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print("Temperture from the 5th to the 10th: ", temperatures[4:10])
