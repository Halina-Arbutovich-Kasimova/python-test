height = float(input("Enter the height in cm "))
weight = float(input("Enter the weight in kg "))
floor = str(input("Enter the floor w or m "))
age = float(input("Enter the age "))
BMI =(weight / ((height*0.01))**2)
BMI2 = round(BMI)
print("Your body mass index = ",BMI2)
scale1 = 16
scale2 = 40
result=scale2-scale1-1
result2 = BMI2 - scale1-1
a = result2
l = ["=",]
n = result
d = l*n
d[a]='/'
d2=' '.join(d)
print("less than ",scale1,d2,scale2, " over 40")
if floor == "w" and age<=20 and BMI2 <=19:
    print("Underweight!Need urgent expert advice")
elif floor == "w" and age>20 and BMI2 <=19:
    print("Underweight!Need urgent expert advice")
elif floor == "w" and age<=20 and BMI2 > 19 and BMI2<=25:
    print("Norm!Keep up the good work ")
elif floor == "w" and age>20 and BMI2 >19 and BMI2<=25:
    print("Norm!Keep up the good work")
elif floor == "w" and age<=20 and BMI2 >=30:
     print("Dangerous! excess weight!Control your diet and exercise")
elif floor == "w" and age>20 and BMI2 >=30:
     print("Dangerous! excess weight!Control your diet and exercise")
elif floor == "m" and age<=21 and BMI2 <=19:
    print("Underweight!Need urgent expert advice")
elif floor == "m" and age>21 and BMI2 <=19:
    print("Underweight!Need urgent expert advice")
elif floor == "m" and age<=21 and BMI2 <=25:
    print("Norm!Keep up the good work")
elif floor == "m" and age>21 and BMI2 <=25:
    print("Norm!Keep up the good work")
elif floor == "m" and age<=21 and BMI2 >=30:
     print("Dangerous! Excess weight!Control your diet and exercise")
elif floor == "m" and age>21 and BMI2 >=30:
     print("Dangerous! Excess weight!Control your diet and exercise")
else:
    print("Check the correctness of the entered data! Take the test again")
