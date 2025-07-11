'''
1. Funció que pren com a paràmetre 
una llista de números i retorna una altra llista 
ordenada.
1. Функция, которая принимает список чисел в качестве параметра 
и возвращает другой отсортированный список.
'''

'''
def ordena (lista):
    temp = lista.copy()
    temp.sort()    
    return temp
llista = [4,3,2,1,8]
print (llista)
print (ordena(llista))
'''

#=====================================================================


'''
2. Funció que pren com a paràmetre una llista de números 
i retorna la suma dels seus elements
2. Функция, которая принимает список чисел в качестве параметра 
и возвращает сумму его элементов.
'''

'''
def sum(llista):   
    suma = 0    
    for element in llista:    
        suma = suma + element    
    return  suma
llista = [4,3,2,1,8]
print (sum(llista))
'''

#=======================================================================

''' 
3. Funció que pren com a paràmetre una llista de números 
i retorna la suma dels quadrats dels seus elements
3. Функция, которая принимает список чисел в качестве параметра 
и возвращает сумму квадратов его элементов
'''

'''
def sq(llista):
    suma = 0    
    for element in llista:    
        suma = suma + element * element    
    return  suma
llista = [4,3,2,1,8]
print (sq(llista))
'''

#=======================================================================

'''
4. Funció que pren com a paràmetre una llista de números 
i retorna la suma dels cubs dels seus elements.
4. Функция, которая принимает список чисел в качестве параметра 
и возвращает сумму кубов его элементов.
'''

'''
def sq(llista):
    suma = 0    
    for element in llista:    
        suma = suma + element * element * element    
    return  suma
llista = [4,3,2,1,8]
print (sq(llista))
'''

#=======================================================================

'''
5. Funció que pren com a paràmetre una llista de números 
i retorna el seu valor mínim.
5. Функция, которая принимает список чисел в качестве параметра 
и возвращает его минимальное значение.
'''

'''
def mini(llista):
    return  min(llista)
llista = [4,3,2,1,8]
print (mini(llista))
'''

#=======================================================================

'''
6. Funció que pren com a paràmetre una llista de números 
i retorna el seu valor màxim.
6. Функция, которая принимает список чисел в качестве параметра 
и возвращает его максимальное значение.
'''

'''
def maxi(llista):    
    return max(llista)
llista = [4,3,2,1,8]
print (maxi(llista))
'''

#=======================================================================


'''
7. Funció que pren com a paràmetre una llista de números 
i retorna la llista en ordre invertit.
7. Функция, которая принимает список чисел в качестве параметра 
и возвращает список в обратном порядке.
'''


'''
def rev(llista):
    temp = llista.copy()
    temp.reverse()
    return temp
llista = [4, 3, 2, 1, 8]
print (rev(llista))
'''

#=======================================================================

'''
8. Funció que pren com a paràmetre una llista de números 
i retorna una altra llista amb els elements en posició parell.
8. Функция, которая принимает список чисел в качестве параметра 
и возвращает другой список с элементами на четных позициях.
'''

'''
def par_pos(new):    
    resultat = []
    for posicion in range(len(new)):
        if posicion % 2 == 0:
            resultat.append(new[posicion])    
    return resultat
llista = [1,4,7,3,8,7,1]
print(par_pos(llista))
'''

#=======================================================================


'''
9. Funció que pren com a paràmetre una llista de números 
i retorna una altra llista amb
els elements en posició senar.
9. Функция, которая принимает список чисел в качестве параметра 
и возвращает другой список с элементами на нечетных позициях.
'''

'''
def par_pos(new):
    resultat = []    
    for posicion in range(len(new)):        
        if posicion % 2 == 1:            
            resultat.append(new[posicion])            
    return resultat
llista = [1,4,7,3,8,7,1]
print(par_pos(llista))
'''

#=======================================================================

'''
10. Funció que pren com a paràmetre una llista de números 
i retorna una altra llista amb el número de dígits de cada element.
10. Функция, которая принимает список чисел в качестве параметра 
и возвращает другой список с количеством цифр в каждом элементе.
'''

'''
def skolko_cifr_v_spiske(spisok):    
    resultat = []    
    for num in spisok:        
        modul_chisla = abs(num) 
        kak_string = str(modul_chisla)
        resultat.append(str(len(kak_string)))    
    output = ','.join(resultat)    
    return output
spisok = [123, 5, 89, 10000, 42]
print(skolko_cifr_v_spiske(spisok))
'''

#=======================================================================

'''
11. Funció que pren com a paràmetre una llista de cadenes 
i retorna una altra llista amb la longitud de cadascuna de les cadenes que formen la llista.
11. Функция, которая принимает список строк в качестве параметра 
и возвращает другой список с длиной каждой из строк, составляющих список.
'''

'''
def poluchenie_dliny_kazhdoy_stroki(strings):    
    dliny = []    
    for s in strings:        
        dlina = len(s)
        dliny.append(dlina)    
    return dliny
primer = ['manzana', 'pera', 'pan', 'cilantro']
result = poluchenie_dliny_kazhdoy_stroki(primer)
print(result)
'''

#=======================================================================

'''
12. Funció que pren com a paràmetre una llista de cadenes 
i retorna una altra llista amb les mateixes cadenes en minúscules.
12. Функция, которая принимает список строк в качестве параметра 
и возвращает другой список с теми же строками в нижнем регистре.
'''

'''    
def minuscules(llista):    
    resultat = []    
    for cadena in llista:    
        resultat.append(cadena.lower())    
    return resultat
llista = ['Manzana', 'Pera', 'Pan', 'Cilantro']
res = minuscules(llista)
print(res)
'''

#=======================================================================

'''
13. Funció que pren com a paràmetre una llista de cadenes 
i retorna una altra llista amb les mateixes cadenes en majúscules.
13. Функция, которая принимает список строк в качестве параметра 
и возвращает другой список с теми же строками в верхнем регистре.
'''

'''  
def majuscules(llista):    
    resultat = []
    for cadena in llista:    
        resultat.append(cadena.upper())    
    return resultat
llista = ['Manzana', 'Pera', 'Pan', 'Cilantro']
res = majuscules(llista)
print(res)
'''

#=======================================================================

'''
14. Funció que pren com a paràmetre una llista de cadenes 
i retorna una única cadena amb tots els elements concatenats 
(Suma d'strings o cadenes).
14. Функция, которая принимает список строк в качестве параметра 
и возвращает одну строку со всеми объединенными элементами 
(сумма строк или цепочек).
'''

'''
llista = ['Manzana', 'Pera', 'Pan', 'Cilantro', 'Amber']
element = ""
for posicion in range(len(llista)):    
    element = element + llista[posicion]    
print (element)
print (type(element))
'''

#=======================================================================

'''
15. Funció que pren com a paràmetre una llista de cadenes 
i retorna una altra llista amb les mateixes cadenes 
ordenades en ordre alfabètic.
15. Функция, которая принимает список строк в качестве параметра 
и возвращает другой список с теми же строками, 
отсортированными в алфавитном порядке.
'''


'''
llista = ['Manzana', 'Pera', 'Pan', 'Cilantro', 'Amber']
print("LLISTA ORIGINAL:")
for posicion in range(len(llista)):    
    print(posicion+1, "-", llista[posicion])
print("\n")
print("LLISTA EN ORDRE ALFABETIC:")
def ordenar(ll):    
    lista_ordenada = sorted(ll)    
    resultado = []    
    idx = 1
    for element in lista_ordenada:        
        resultado.append(f"{idx} - {element}")        
        idx = idx + 1
    return resultado
for linea in ordenar(llista):
    print(linea)
'''   

#=======================================================================
  
'''
16. Funció que pren com a paràmetre una llista de cadenes 
i retorna una altra llista amb les cadenes 
que es troben en posició parell.
16. Функция, которая принимает список строк в качестве параметра, 
и возвращает другой список со строками, находящимися на четных позициях.
'''

'''
llista = ['Rubi', 'Esmeralda', 'Zafiro', 'Perla', 'Diamant', 'Aquamarina']
print (f"LLISTA ORIGINAL:") 
for posicion in range(len(llista)):  
print (posicion+1,"-", llista[posicion])
print ("\n")
print ("ELEMENTOS EN POSICIONES PARES (primer posicion es 0):")
def parell(var):   
    resultado = []
    for posicion in range(len(llista)):
        if posicion % 2 == 0:            
            resultado.append(llista[posicion])
            print(f"{posicion+1} - {llista[posicion]}")    
    return resultado
parell(llista)
'''

#=======================================================================

'''
17. Funció que pren com a paràmetre una llista de cadenes 
i retorna una altra llista amb les cadenes que es troben en posició senar.   
17. Функция, которая принимает список строк в качестве параметра 
и возвращает другой список со строками, которые находятся в нечетных позициях.    
'''    
 
'''
llista = ['Rubi', 'Esmeralda', 'Zafiro', 'Perla', 'Diamant', 'Aquamarina']
print (f"LLISTA ORIGINAL:") 
for posicion in range(len(llista)):  
    print (posicion+1,"-", llista[posicion])
print ("\n")       
print ("ELEMENTOS EN POSICIONES PARES (primer posicion es 0):")
def parell(var):    
    resultado = []
    for posicion in range(len(llista)):       
        if posicion % 2 == 1:            
            resultado.append(llista[posicion])
            print(f"{posicion+1} - {llista[posicion]}")
            return resultado
parell(llista)
'''

#=======================================================================

'''
18. Funció que pren com a paràmetre una llista de cadenes 
i retorna una altra llista amb les mateixes cadenes sense l'últim caràcter
18. Функция, которая принимает список строк в качестве параметра 
и возвращает другой список с теми же строками без последнего символа.

Задается функция с одним параметром (llista). 
Результат равен пустому множеству в квадратных скобках.
Цикл по цепочка в llista
Новая цепочка равно цепочке с параметром [:-1]
результат.функция добавления в новую цепочку в скобках.
Возврат результата

Далее задается исходный набор экзампл в квадратных скобках, 
элементы в одинарных кавычках через запятую. 
Переменная рез равна функции от экзампл.
Печать рез.
'''


'''
# без функции

llista = ['Rubi', 'Esmeralda', 'Zafiro', 'Perla', 'Diamant', 'Aquamarina']
print (f"LLISTA ORIGINAL:") 
for posicion in range(len(llista)):
    print (posicion+1,"-", llista[posicion])
print ("\n")
print ("ELEMENTOS SIN ULTIMA LLETRA:")
for posicion in range(len(llista)):
    print (posicion+1,"-", llista[posicion][:-1])


#c функцией

llista = ['Rubi', 'Esmeralda', 'Zafiro', 'Perla', 'Diamant', 'Aquamarina']
print (f"LLISTA ORIGINAL:") 
for posicion in range(len(llista)):
    print (posicion+1,"-", llista[posicion])
print ("\n")
print ("ELEMENTOS SIN ULTIMA LLETRA:")
def nolast(llista):
    nol = []
    for posicion in range(len(llista)):
        nol.append(llista[posicion][:-1])
    return nol
resultado = nolast(llista)
for posicion in range(len(resultado)):  
    print(posicion+1,"-", resultado[posicion])
'''

#=======================================================================

'''
19. Funció que pren com a paràmetre una llista de cadenes 
i retorna una altra llista amb les mateixes cadenes  
sense el primer caràcter.
19. Функция, которая принимает список строк в качестве параметра 
и возвращает другой список с теми же строками без первого символа.
'''

'''
llista = ['Rubi', 'Esmeralda', 'Zafiro', 'Perla', 'Diamant', 'Aquamarina']
print (f"LLISTA ORIGINAL:") 
for posicion in range(len(llista)):
    print (posicion+1,"-", llista[posicion])
print ("\n")
print ("ELEMENTOS SIN ULTIMA LLETRA:")
def nolast(llista):
    nol = []
    for posicion in range(len(llista)):
        nol.append(llista[posicion][1:])
    return nol
resultado = nolast(llista)
for posicion in range(len(resultado)):  
    print(posicion+1,"-", resultado[posicion])
'''

#=======================================================================

'''
20. Funció que pren com a paràmetre una llista de cadenes 
i retorna una altra llista amb les mateixes cadenes invertides
20. Функция, которая принимает список строк в качестве параметра 
и возвращает другой список с теми же словами, но буквы стоят в обратном порядке.
'''

'''
llista = ['Rubi', 'Esmeralda', 'Zafiro', 'Perla', 'Diamant', 'Aquamarina']
print("LLISTA ORIGINAL:")
print(llista)
print("\nLLISTA AMB LES MATEIXES CADENES INVERTIDES:")
def inv(llista):
    nol = []    
    for paraula in llista:    
        nol.append(paraula[::-1])  # переворот строки    
    return nol
resultado = inv(llista)
for i in range(len(resultado)):    
    print(i + 1, "-", resultado[i])
'''