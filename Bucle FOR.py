#  Bucle FOR


'''
20. Fes un programa que mostri la taula de multiplicar d'un nú́mero introduït per
teclat per l'usuari. Aquí tens un exemple de com s'ha de comportar el
programa:
20. Напишите программу, которая отображает таблицу умножения числа, введенного пользователем. 
Вот пример того, как должна себя вести программа: Назовите мне число: 5
Dóna'm un número: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''

'''
num = int(input ("Entra el numero"))

for mult in range(1, 11) :
 
    print(f"{num} x {mult} = {num * mult}")
'''








'''
22. Fes un programa que mostri, en línees independients, tots els números parells
compresos entre 0 i 200 (ambdós inclosos)
22. Напишите программу, которая выводит на экран в отдельных строках 
все четные числа от 0 до 200 (включительно).
'''

'''
for index in range(2, 202):

    if index % 2 == 0:
    
        print (index)
'''



'''
23. Escriu un programa que mostri els números parells positius entre 2 i un número
qualsevol que introdueixi l'usuari per teclat.
23. Напишите программу, которая отображает положительные четные числа от 2 до любого числа, 
введенного пользователем с клавиатуры.
'''


'''
num = int(input ("Entra el numero mas de 2"))


if num > 2:
    
    print (f"Els números parells positius entre 2 i su número ({num}) son:")

    for i in range (2, num+1):
  
        if i % 2 == 0:
            
            print (i)
else:
    
    print (f"Su numero ({num}) no es correcto.")
'''





'''
30. Fer un programa que llegeixi un nombre sencer positiu 
i escrigui la suma de les seves xifres.
30. Составьте программу, которая считывает положительное целое число 
и записывает сумму его цифр.
'''





'''
num = input ("Entra un nombre sencer positiu: ")

if int(num) > 0:
    
    suma = 0
    
    for xifra in num:
    
        suma = suma + int(xifra)
    
    print ("La suma de les xifres del numero", num, "és", suma)

else:

    print("El valor (", num, ") no és un enter positiu.")
           
'''   