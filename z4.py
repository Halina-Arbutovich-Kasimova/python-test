a = int(input("Введите число ")) #Z1
b = int(input("Ввести число "))
c = int(input("Ввести число "))
resualt = a>0 and b>0 and c>0 and "Нет нулевых значений !!!"
print(resualt)
resualt2 = a>0 or b>0 or c>0 or "Введены все 0!"   #Z2
print(resualt2)

if a>b+c:            #Z3
    resualt3 = a*b*c
    print(resualt3) 
else:                #Z4
    resualt3 = b+c-a
    print(resualt3) 
    
if a>50 and b>a or c>a: #Z5
    print("Вася")
if a>5 or b==7 and c==7: #Z6
    print("Петя")
    
  






