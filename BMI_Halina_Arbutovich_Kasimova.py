height = float (input("Enter the height in cm "))
weight =float( input("Enter the weight in kg "))
BMI =(weight / ((height*0.01))**2)
BMI2 = round(BMI)
print ("Your body mass index = ",BMI2)
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
print (scale1,d2,scale2)
