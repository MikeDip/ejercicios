'''
Exercici 1. 
Escriure una classe a Python amb 2 mètodes: get_string() i print_string(). 
get_string() accepta una cadena ingressada per l'usuari 
i print_string() imprimeix la cadena en majúscules
Exercici 1. 
Напишите класс Python с двумя методами: get_string() и print_string(). 
get_string() принимает строку, введённую пользователем, 
а print_string() выводит её в верхнем регистре.
'''    

'''
class MyString:
    def __init__(self):
        self.cadena = ""

    def get_string(self):
        self.cadena = input("Entra la cadena: ")

    def print_string(self):
        print("Su cadena en mayúsculas:", self.cadena.upper())

cadena1 = MyString()
cadena1.get_string()
cadena1.print_string()
'''   
    
#=================================================================================

'''
Exercici 2 
Escriure una classe a Python anomenada Rectangulo 
que contingui una base i una altura, 
i que contingui un mètode que torni l'àrea del rectangle.
Упражнение 2
Напишите класс Python с именем Rectangle, 
содержащий основание и высоту, 
а также метод, возвращающий площадь прямоугольника.
'''

'''
class Rectangle:

    def __init__(self, costat1, costat2):
        self.costat1 = costat1
        self.costat2 = costat2
        
    def area(self):
        return self.costat1 * self.costat2

r1 = Rectangle (3, 4)
print(r1.costat1)
print(r1.costat2)
print(r1.area())
'''
  
#=================================================================================

'''
Exercici 3 
Escriure una classe a Python anomenada Circulo 
que contingui un radi, amb un mètode que torni l'àrea 
i un altre que torni el perímetre del cercle.
Упражнение 3
Напишите класс Python под названием «Окружность», 
непрерывный по радиусу, с методом, который вращает площадь, 
и методом, который площадь и длину окружности.
'''

'''
class Circulo:

    def __init__(self, radi):
        self.radi = radi
        
    def area(self):
        return 3.14 * self.radi ** 2 
    
    def perim(self):
        return 2 * 3.14 * self.radi

  
#    def __str__  (self):
#        return f"Es un objeco circulo con radi {self.radi}, area {self.area()} y perimetro {self.perimetro()}"
     
radi = Circulo (5)
print (radi.area())
print (radi.perim())
'''

#=================================================================================

'''
Exercici 4 
Anem a crear una classe anomenada Persona. Els seus atributs són: nom, edat i DNI. 
Construeix els següents mètodes per la classe: 
 • Un constructor, on les dades poden estar buides.
 • Els setters i getters per a cadascun dels atributs. S'han de validar les entrades de dades.
 • mostrar(): Mostra les dades de la persona.
 • esMayorDeEdad(): Torna un valor lògic indicant si és major d' edat.

Упражнение 4
Создадим класс Person. Его атрибуты: имя, возраст и идентификатор.
Создайте следующие методы для класса:
• Конструктор, где данные могут быть пустыми.
• Set-теры и Get-теры для каждого из атрибутов. 
  Введенные данные должны быть проверены.
• mostrar(): Отображает данные о человеке.
• esMayorDeEdad(): Возвращает логическое значение, указывающее, достиг ли человек совершеннолетия.

Примечания:
Проверка валидности DNI выполняется не через REGEX, а через цикл WHILE
'''

'''
import re

class Persona:
    
    def __init__(self, nom, edat, DNI):
        self.nom = nom          
        self.edat = edat      
        self.DNI = DNI     
    
    def set_nom(self):
        patro = re.compile("^[A-Za-z\ ]+$")  
        temp = ""
        while len(patro.findall(temp)) == 0:
            temp = input("Nom: ")
        self.nom = temp
                
    def set_edat(self):
        patro = re.compile("^[0-9]{1,3}$") 
        self.edat = -1
        while len(patro.findall(temp)) == 0:
            self.edat = input("Edat: ")
        self.edat = int(self.edat)
    
    def esMayorDeEdad(self):     
        if self.edat >= 18:            
            print (f"Es Mayor De Edad")
            return True
        else:
            print (f"No es Mayor De Edad")
            return False 
     
    def set_DNI(self):     
        self.DNI = ""   
        while len(self.DNI) != 9 or not(self.DNI[:-1].isdigit()) or not(self.DNI[-1].isalpha()):
            self.DNI = input ("DNI: ")
            
#            Проверка валидности DNI через REGEX (в данном случае менее точная) 
#   def set_DNI(self):     
#       self.DNI = ""      
#       patro = re.compile("^[A-Za-z0-9]+$")  
#       while len(patro.findall(self.DNI)) == 0:
#           temp = input("DNI: ")
#       self.DNI = temp

    def get_nom(self):
        return self.nom
  
    def get_edat(self):
        return self.edat
    
    def get_DNI(self):
        return self.DNI

p1 = Persona ("Julio Iglesias", 45, "12345678N")

#print (p1)
print (p1.nom)
#print (p1.get_nom())
print (p1.edat)
#print (p1.get_edat())
print (p1.DNI)
#print (p1.get_DNI())
print (p1.esMayorDeEdad())
'''
 
#=================================================================================
 

'''    
Exercici 5 
Desenvolupar un programa que carregui les dades d'un triangle. 
Implementar una classe amb els mètodes per inicialitzar els atributs, 
imprimir el valor del costat amb una mida més gran i el tipus de triangle que és 
(equilàter, isòsceles o escalè).
Упражнение 5
Разработайте программу, загружающую данные треугольника.
Реализуйте класс с методами инициализации атрибутов, 
вывода значения стороны с наибольшим размером и типа треугольника 
(равносторонний, равнобедренный или разносторонний).
'''

'''
class Triangle:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def max_lado(self):
        maxi = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado más largo es: {maxi}")

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            print("El triángulo es isósceles")
        else:
            print("El triángulo es escaleno")

lado1 = int(input("Introduce el lado 1: "))
lado2 = int(input("Introduce el lado 2: "))
lado3 = int(input("Introduce el lado 3: "))

t = Triangle(lado1, lado2, lado3)
t.max_lado()
t.tipo_triangulo()
'''

#=================================================================================
 

'''
Exercici 6 
Escriu una classe de Python, i defineix dos mètodes que tornin l'àrea del quadrat i el perímetre.
Упражнение 6
Напишите класс Python и определите два метода, возвращающие площадь квадрата и его периметр.
'''

class Quadrat:
    def __init__(self, lado):
        self.lado = lado
        
    def analiz(self):
        area = self.lado ** 2 
        print (f"L'àrea del quadrat es: {area}")
        perimetre = 4 * self.lado
        print (f"El perímetre del quadrat es: {perimetre}")

lado = int(input("Introduce el lado del quadrat: "))

q = Quadrat(lado)
q.analiz()



