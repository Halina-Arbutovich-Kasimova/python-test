str = "Не знаю, как там в Лондоне, Я не была. Может, там собака - друг человека. А у нас управдом - друг человека!"
b = len (str)
print ("Количество символов - ",b)
print(str[::-1])
print(str.title())
print(str.lower())
s=str.count("нд")
print("Количество нд в строке - ",s)
m=str.count("ам")
print("Количество ам в строке - ",s)
z=str.count("о")
print("Количество о в строке - ",z)
str2="Я Денис"
x=str2.split(" ")
str2=x[1]+" "+x[0]
print(str2)
print (str*3)
b="р"
print("В строке есть р - ", b in str)
ch = "(Бриллиантовая рука)"
print(str+" "+ch)