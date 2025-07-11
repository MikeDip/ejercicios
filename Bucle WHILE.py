#  Bucle WHILE


'''
1. Simular un compte enrer.
1. Имитировать обратный отсчет
'''

'''
num = int(input ("Entra el numero"))

for mult in range(num, -1, -1) :
 
    print(mult)
'''


'''
2. Escriure els múltiples de 2 menors o iguals a 100
2. Запишите числа, кратные 2, которые меньше или равны 100.
'''

'''
for num in range(0, 101):

   if num % 2 == 0:
   
       print (num)
 '''



'''
3. Escriure els 10 primers múltiples de 2.
3. Запишите первые 10 чисел, кратных 2.
'''

'''
number = 2

index = 0

while index < 10:
    
    print(number)
    
    number = number + 2
    
    index = index + 1
'''




'''
4. Escriure els n primers múltiples de m
4. Запишите первые n кратных m.
'''

'''
i = 1

n = int(input ("Entra el cantidad de numeros - n"))

m = int(input ("Entra de que dividimos - m"))
            
while i <= n:
    
    print (m * i)
     
    i = i + 1      
'''






'''
6. Sumar els múltiples de 2 menors a 100.
6. Сложите числа, кратные 2, меньше 100.
'''


'''
sum = 0

for num in range(0, 101):

   if num % 2 == 0:
   
       sum = sum + num
       
print (sum)
'''



'''
7. Sumar les potències de 2 menors a 100
7. Сложение степеней числа 2 меньше 100
'''
# ошибка. Не работает

sum = 0          # Может задать 1, т.к. 2^0 = 1?

s = 1          # задаем первое значение 2 в 1-й степени 

while s < 100:
    
    s = s * 2   

sum = sum + s

print (sum)