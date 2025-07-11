'''
Exercicis avançats de tractament de cadenes en Python
Упражнения по продвинутой обработке строк Python
'''


#===================================================================================


'''
1. Mesures de les cadenes (len, max, min):
Escriu un programa que demani a l'usuari diverses paraules separades per espais. 
El programa ha de calcular la paraula més llarga, la més curta i mostrar el caràcter 
amb el valor més alt i més baix ASCII dins de la cadena completa. 
Entrada: 'Python és increïble' 
Sortida esperada: 
La paraula més llarga és: increïble 
La paraula més curta és: és 
El caràcter amb el valor ASCII més alt és: y 
El caràcter amb el valor ASCII més baix és: (espai)

1. Измерения строк (len, max, min): 
Напишите программу, которая запрашивает у пользователя несколько слов, разделенных пробелами. 
Программа должна вычислить самое длинное слово, самое короткое слово и отобразить символ 
с самым высоким и самым низким значением ASCII во всей строке.
Ввод: «Python is amazing»
Ожидаемый вывод:
Самое длинное слово: amazing
Самое короткое слово: is
Символ с самым высоким значением ASCII: y
Символ с самым низким значением ASCII: (пробел)
'''

'''
cadena = input("Entra diverses paraules separades per espais")
print (f"Sus paraulas entradas: {cadena}")

paraulas = cadena.split()

paraula_larga = max(paraulas, key=len)
print("La paraula més llarga és:", paraula_larga)

paraula_corta = min(paraulas, key=len)
print("La paraula més curta és:", paraula_corta)

letra_max = max(cadena)
print("El caràcter amb el valor ASCII més alt és:", letra_max)

letra_min = min(cadena)

if min(cadena)==" ": 
    print ("El caràcter amb el valor ASCII més baix és: Espai") 
else: 
    print("El caràcter amb el valor ASCII més baix és:", letra_min)
'''


#====================================================================================


'''
2. Operacions amb cadenes (+, *, \n):
Escriu un programa que demani a l'usuari una frase i un número. 
El programa ha de concatenar la frase amb una versió repetida 
de la mateixa frase el número de vegades indicat, 
amb cada repetició en una línia nova. 
Entrada: 'Hola, món!', 3 
Sortida esperada: 
Hola, món! 
Hola, món! 
Hola, món!
2. Строковые операции (+, *, \n): 
Напишите программу, которая запрашивает у пользователя фразу и число. 
Программа должна объединить фразу с повторенной версией той же фразы 
указанное количество раз, причем каждое повторение должно быть на новой строке. 
Ввод: 'Привет, мир!', 3 
Ожидаемый вывод: 
Привет, мир! 
Привет, мир! 
Привет, мир!
'''

'''
cadena = input("Entra una frase:")
numero = input("Entra el numero de vezes de sortida:")
for i in range(int(numero)):
    print (cadena)
'''


#====================================================================================


'''
3. Cerca de caràcters (count, index, find):
Escriu un programa que demani una cadena i un caràcter. 
El programa ha de mostrar quantes vegades apareix el caràcter en la cadena, 
la seva primera aparició i la seva última aparició. 
Entrada:'supercalifragilistico', 'i' 
Sortida esperada: El caràcter 'i' apareix 3 vegades. 
La seva primera aparició és a la posició 7. 
La seva última aparició és a la posició 17.

3. Поиск символов (подсчет, индекс, поиск): 
Напишите программу, которая запрашивает строку и символ. 
Программа должна отображать, сколько раз символ появляется в строке, 
его первое появление и последнее появление. 
Ввод: 'supercalifragilistico', 'i' 
Ожидаемый вывод: 
Символ 'i' появляется 3 раза. 
Его первое появление находится в позиции 7. 
Его последнее появление находится в позиции 17.
'''

'''
cadena = input ("Entra una frase:")
caracter = input ("Entra caracter en lo que estas interesante:")

countcar = cadena.count(caracter)
print (f"El caracter '{caracter}' apareix {countcar} vezes.")

indexcar = cadena.index(caracter)
print (f"La primera aparecion de este caracter es a la posicion {indexcar}")
       
rindexcar = cadena.rindex(caracter)       
print (f"La ultima aparecion de este caracter es a la posicion {rindexcar}") 
'''


#====================================================================================


'''
4. Majúscules i minúscules (upper, lower, capitalize):
Escriu un programa que demani una frase a l'usuari. 
El programa ha de mostrar la frase en tres versions: 
totes les paraules en majúscula, en minúscules, 
i amb només la primera lletra en majúscula. 
Entrada: 'el gat menja peix' 
Sortida esperada: 
Frase amb majúscules: EL GAT MENJA PEIX 
Frase en minúscules: el gat menja peix 
Frase capitalitzada: El gat menja peix 
La frase estava originalment en minúscules.

4. Заглавные и строчные буквы (заглавные, строчные, заглавные): 
Напишите программу, которая запрашивает у пользователя предложение. 
Программа должна отображать предложение в трех вариантах: 
все слова заглавными, строчными и только с первой буквой заглавной. 
Ввод: «кот ест рыбу» 
Ожидаемый вывод: 
Предложение заглавными буквами: КОТ ЕСТ РЫБУ 
Предложение строчными буквами: кот ест рыбу 
Предложение с заглавными буквами: Кот ест рыбу 
Первоначально предложение было написано строчными буквами
'''

'''
frase = input ("Entra una frase con minusculas:")
print (f"Frase amb majúscules: {frase.upper()}.")
print (f"Frase en minúscules: {frase.lower()}.")
print (f"Frase capitalitzada: {frase.capitalize()}.") 
'''


#====================================================================================


'''
5. Concatenació de cadenes (''.join()):
Escriu un programa que demani a l'usuari una llista de paraules separades 
per comes i un símbol escollit per l'usuari per unir-les. 
Entrada: 'poma,plàtan,taronja', '@' 
Sortida esperada: poma@plàtan@taronja

5. Конкатенация строк (''.join()): 
Напишите программу, которая запрашивает у пользователя список слов, 
разделенных запятыми, и символ, выбранный пользователем для их объединения. 
Ввод: 'apple,banana,orange', '@' 
Ожидаемый вывод: apple@banana@orange
'''

'''
paraulas = input("Entra una llista de paraules separades per comes:")
simbol = input("Entra un símbol escollit:")

words = paraulas.split(',')
resultat = simbol.join(words)

print(resultat)
'''


#====================================================================================



'''
6. Divisió de cadenes (split, partition):
Escriu un programa que demani a l'usuari una frase llarga i una paraula de divisió.
El programa ha de dividir la frase utilitzant 'partition' 
i després mostrar la llista de paraules utilitzant 'split'. 
Entrada: 'A mi m'agrada la pizza, i també la pasta', 'pizza' 
Sortida esperada: 
Partició de la frase: ('A mi m'agrada la ', 'pizza', ', i també la pasta') 
Llista de paraules: ['A', 'mi', "m'agrada", 'la', 'pizza,', 'i', 'també', 'la', 'pasta']]

6. Разделение строк (split, partition): 
Напишите программу, которая запрашивает у пользователя длинное предложение 
и разделяющее слово. 
Программа должна разделить предложение с помощью 'partition', 
а затем отобразить список слов с помощью 'split'. 
Ввод: 'I like pizza, and also pasta', 'pizza' 
Ожидаемый вывод: 
Раздел предложения: ('I like ', 'pizza', ', and also pasta') 
Список слов: ['A', 'me', "like", 'la', 'pizza,', 'i', 'also', 'la', 'pasta']
'''

'''
frase = input ("Entra una frase")
div = input ("Entra un caracter para dividir")

parti = frase.partition(div)
print (parti)

separado = frase.split()
print (separado)
'''


#====================================================================================


'''
7. Ordenació de cadenes (sorted):
Escriu un programa que demani a l'usuari una frase 
i mostri els caràcters ordenats de manera ascendent i descendent. 
Entrada:'zebra' 
Sortida esperada:
Caràcters ordenats (ascendent): aebrz 
Caràcters ordenats (descendent): zrbca

7. Сортировка строк (сортировка):
Напишите программу, которая запрашивает у пользователя фразу
и отображает символы, отсортированные по возрастанию и убыванию.
Ввод:'zebra'
Ожидаемый вывод:
Сортированные символы (по возрастанию): aebrz
Сортированные символы (по убыванию): zrbca
'''

'''
frase = input ("Entra una frase")

print (f"Caràcters ordenats (ascendent):", sorted(frase)) 
print (f"Caràcters ordenats (descendent):", sorted((frase), reverse=True)) 
'''



#====================================================================================



'''
8. Modificació de cadenes (replace, strip, lstrip, rstrip):
Escriu un programa que demani una frase amb espais al principi i al final, 
i un caràcter o paraula a substituir. 
Utilitza 'strip', 'replace', 'lstrip' i 'rstrip' per modificar la cadena 
i mostrar les versions.
Entrada: ' Hola, Python és genial! ', 'Python' 
Sortida esperada: 
Frase sense espais: 'Hola, Python és genial!' 
Frase sense espais inicials: 'Hola, Python és genial! ' 
Frase sense espais finals: ' Hola, Python és genial!' 
Frase modificada: 'Hola, [substituït] és genial!' 

8. Изменение строки (replace, strip, lstrip, rstrip):
Напишите программу, которая запрашивает строку с начальными и конечными пробелами, 
а также символ или слово для замены.
Используйте 'strip', 'replace', 'lstrip' и 'rstrip' для изменения строки
и отображения версий.
Ввод: ' Привет, Python великолепен! ', 'Python'
Ожидаемый вывод:
Предложение без пробелов: ' Привет, Python великолепен! '
Предложение без начальных пробелов: ' Привет, Python великолепен! '
Предложение без конечных пробелов: ' Привет, Python великолепен! '
Измененное предложение: ' Привет, [заменено] великолепен! '
'''


'''
cadena = input ("Entra una frase con espasios en el principio y en el final")
sim1 = input ("Entra un simbol palabra que quieres reemplazar")
sim2 = input ("Entra un simbol palabra de que quieres reemplazar")

resultat3 = cadena.strip(" ")
print (f"Frase sense espais:", resultat3)

resultat1 = cadena.lstrip(" ")
print (f"Frase sense espais inicials:", resultat1)

resultat2 = resultat1.rstrip(" ")
print (f"Frase sense espais finals:", resultat2)

resultat4 = cadena.replace (sim1, sim2)
print (f"Frase sense espais finals:", resultat4)
'''



#====================================================================================




'''
9. Comparació de cadenes (<, >, ==, !=):
Escriu un programa que demani dues cadenes a l'usuari 
i compari quina és més gran segons l'ordre alfabètic. 
Mostra si són iguals o diferents. 
Entrada: 'gat', 'gos' 
Sortida esperada: 
La cadena 'gos' és major que 'gat'.

9. Сравнение строк (<, >, ==, !=):
Напишите программу, которая запрашивает у пользователя две строки и сравнивает, 
какая из них больше в алфавитном порядке.
Покажите, равны они или различны.
Ввод: 'cat', 'dog'
Ожидаемый вывод:
Строка 'dog' больше, чем 'cat'.
'''


'''
cad1 = input ("Entra la primera cadena")
cad2 = input ("Entra la segunda cadena")

if cad1 > cad2:
   print (f"{cad1}  és major que  {cad2}")
    
else:
   print (f"{cad2}  és major que  {cad1}")
'''




#====================================================================================


'''
10. Comprovacions True/False (isdigit, isalpha, islower, startswith,endswith):
Escriu un programa que demani una cadena a l'usuari i comprovi 
si només conté dígits, lletres, espais, 
i si comença o acaba amb un caràcter específic. 
Entrada: 'Python123' 
Sortida esperada: 
La cadena només conté dígits: False 
La cadena només conté lletres: False 
La cadena només conté espais: False 
La cadena comença amb 'P': True 
La cadena acaba amb '3': True

10. Проверки True/False (isdigit, isalpha, islower, startswith, endswith):
Напишите программу, которая запрашивает у пользователя строку и проверяет, 
содержит ли она только цифры, буквы, пробелы, и начинается 
или заканчивается ли она определенным символом.
Вход: 'Python123'
Ожидаемый вывод:
Строка содержит только цифры: False
Строка содержит только буквы: False
Строка содержит только пробелы: False
Строка начинается с 'P': True
Строка заканчивается на '3': True
'''

'''
cadena = input ("Entra cadena")

res1 = cadena.isdigit()
print (f"La cadena només conté dígits:", res1)

res2 = cadena.isalpha() 
print (f"La cadena només conté lletres:", res2)

res3 = cadena.isspace()
print (f"La cadena només conté espais:", res3)

res4 = cadena.startswith('P')
print (f"La cadena comença amb 'P':", res4)

res5 = cadena.endswith('3')
print (f"La cadena acaba amb '3':", res5)
'''