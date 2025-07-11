'''
Exercici 1: Validació de correus electrònics 
Objectiu: Escriu una expressió regular per validar correus electrònics simples. 
Entrada: hola@test.com,hola@test..com,hola@test.com., josep.puigdemont@company.cat, marta123@xyz.org, persona@. 
Упражнение 1: Проверка электронной почты
Цель: Написать регулярное выражение для проверки простых электронных писем.
'''

'''
import re
cadena = "ds.@test.com,hola@test..com,hola@test.com.,hola@test.com.ar, josep.capsigrany.puigdemont@company.cat, marta123@xyz.org, persona@."
patro = re.compile("[a-z0-9\.]+@[a-z]+(?:\.[a-z]+){1,}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 2: Extracció de números de telèfon amb prefix 
Objectiu: Escriu una expressió regular per extreure 
els números de telèfon espanyols amb prefix "(93)". 
Entrada: (93)2541700, (952)253228, (93)2177017, (958)233517. 
Упражнение 2: Извлечение телефонных номеров с префиксом
Цель: Написать регулярное выражение для извлечения
испанских телефонных номеров с префиксом "(93)".
'''

'''
import re
cadena = "(93)2541700, (952)253228, (93)2177017, (958)233517" 
patro = re.compile("\(93\)[0-9]{7}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 3: Identificació de paraules amb accents 
Objectiu: Extrau totes les paraules que contenen accents en una frase. 
Entrada: Hola, com estàs? Avui és un dia solejat i l'hora és les 10:30 del matí. 
Упражнение 3: Определение ударных слов
Цель: Извлечь все слова, содержащие ударения в предложении.
'''

'''
import re
cadena = "Hola, com estàs? Avui és un dia solejat i l'hora és les 10:30 del matí. " 
patro = re.compile("[a-zA-Z]*[àáèéìíïòóùú]{1}[a-z]*")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 4: Validació de codis postals 
Objectiu: Escriu un regex per validar codis postals de 5 dígits espanyols. 
Entrada: 08001, 08080, 12345, abcd5, 5678. 
Упражнение 4: Проверка почтового индекса
Цель: Написать регулярное выражение для проверки 5-значных испанских почтовых индексов.
'''

'''
import re
cadena = "08001, 08080, 12345, abcd5, 5678" 
patro = re.compile("[0-4]{1}[0-9]{4}|[50-52]{1}[0-9]{3}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 5: Extracció de preus en format decimal 
Objectiu: Escriu un regex per trobar preus amb decimals en una cadena de text. 
Entrada: Els preus dels productes són 10.99€, 20€, 100.50€, i 300.00€. 
Упражнение 5: Извлечение цен в десятичном формате
Цель: Написать регулярное выражение для поиска цен с десятичными знаками в текстовой строке.
'''

'''
import re
cadena = "Els preus dels productes són 10.99€, 20€, 100.50€, i 300.00€. " 
patro = re.compile("[0-9]*\.[0-9]{2}€|[0-9]+€")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 6: Validació de dates en format DD/MM/AAAA 
Objectiu: Escriu un regex per validar dates en format DD/MM/AAAA. 
Entrada: 25/12/2021, 01/01/1999, 31/02/2020, 30/04/2020. 
Упражнение 6: Проверка дат в формате ДД/ММ/ГГГГ
Цель: Написать регулярное выражение для проверки дат в формате ДД/ММ/ГГГГ.
'''

'''
import re
cadena = "25/12/2021, 01/01/1999, 31/02/2020, 30/04/2020" 
patro = re.compile("[0-9]{2}/[0-9]{2}/[0-9]{4}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 7: Detecció de URLs 
Objectiu: Escriu un regex per extreure URLs d'una cadena de text. 
Entrada: Visita https://www.example.com per més informació o http://test.org. També 
pots anar a www.google.com. 
Упражнение 7: Определение URL-адресов
Цель: Написать регулярное выражение для извлечения URL-адресов из текстовой строки.
'''

'''
import re
cadena = "Visita https://www.example.com per més informació o http://test.org. També pots anar a www.google.com"
patro = re.compile("https?://[a-z0-9\_\.-]+\.[a-z0-9]{2,3}|www[a-z0-9\_\.-]+\.[a-z0-9]{2,3}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 8: Validació de números de telèfon mòbils espanyols 
Objectiu: Escriu un regex per validar números de telèfon mòbil que comencin amb 6 o 7 i 
tinguin 9 dígits. 
Entrada: 612345678, 711234567, 812345678. 
Упражнение 8: Проверка испанских номеров мобильных телефонов
Цель: Написать регулярное выражение для проверки номеров мобильных телефонов, начинающихся с 6 или 7 и состоящих из 9 цифр.
'''

'''
import re
cadena = "612345678, 711234567, 812345678"
patro = re.compile("[6|7][0-9]{8}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 9: Extracció de noms propis 
Objectiu: Escriu un regex per extreure noms propis d'una frase (inicien amb majúscula). 
Entrada: Maria va anar a Barcelona amb Josep i Anna. 
Упражнение 9: Извлечение имен собственных
Цель: Написать регулярное выражение для извлечения имен собственных из предложения (они начинаются с заглавной буквы).
'''

'''
import re
cadena = "Maria va anar a Barcelona amb Josep i Anna"
patro = re.compile("[A-ZÀÁÈÉÌÍÏÒÓÙÚ]{1}[a-zàáèéìíïòóùú]+")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 10: Detecció d'adreces IP 
Objectiu: Escriu un regex per validar adreces IP en format IPv4. 
Entrada: 192.168.1.1, 255.255.255.0, 999.999.999.999. 
Упражнение 10: Определение IP-адреса
Цель: Написать регулярное выражение для проверки IP-адресов в формате IPv4.
'''

'''
import re
cadena = "192.168.1.1, 255.255.255.0, 999.999.999.999"
patro = re.compile("[1-9]?[0-9]{0,2}\.[1-9]?[0-9]{0,2}\.[1-9]?[0-9]{0,2}\.[1-9]?[0-9]{0,2}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 11: Validació de contrasenyes 
Objectiu: Escriu un regex per validar contrasenyes que tinguin entre 8 i 16 caràcters, 
almenys una majúscula, una minúscula, i un número. 
Entrada: Contraseña1, pass, PASSWORD123. 
Упражнение 11: Проверка пароля
Цель: написать регулярное выражение для проверки паролей длиной от 8 до 16 символов,
содержащих как минимум одну заглавную букву, одну строчную букву и одну цифру.
'''

'''
import re
cadena = "Contraseña1, pass, PASSWORD123"
patro = re.compile("[A-ZÀÁÈÉÌÍÏÒÓÙÚÑa-z0-9àáèéìíïòóùúñ]{8,16}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 12: Identificació de hashtags 
Objectiu: Escriu un regex per extreure hashtags d'un text. 
Entrada: Avui és un bon dia #sunny #felicitat #dia. 
Упражнение 12: Определение хэштегов
Цель: написать регулярное выражение для извлечения хэштегов из текста.
'''

'''
import re
cadena = "Avui és un bon dia #sunny #felicitat #dia."
patro = re.compile("#[A-Za-z0-9_]+")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 13: Extracció d'enllaços sense protocol 
Objectiu: Escriu un regex per extreure enllaços web 
que no incloguin el protocol (ex: www). 
Entrada: Visita www.example.com per més informació. 
Упражнение 13: Извлечение ссылок без протокола
Цель: написать регулярное выражение для извлечения веб-ссылок, 
которые не включают протокол (например: www).
'''

'''
import re
cadena = "Visita www.example.com per més informació"
patro = re.compile("www\.[a-z0-9]+\.[a-z0-9]{2,3}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 14: Validació de targetes de crèdit 
Objectiu: Escriu un regex per validar números de targetes de crèdit amb 16 dígits. 
Entrada: 1234 5678 9012 3456, 1111 2222 3333 4444. 
Упражнение 14: Проверка кредитной карты
Цель: написать регулярное выражение для проверки 16-значных номеров кредитных карт.
'''

'''
import re
cadena = "234 5678 9012 3456, 1111 2222 3333 4444"
patro = re.compile("[1-9]{4}\s[0-9]{4}\s[0-9]{4}\s[0-9]{4}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 15: Extracció de coordenades geogràfiques 
Objectiu: Escriu un regex per extreure coordenades en format de graus decimals. 
Entrada: 41.40338, 2.17403. 
Упражнение 15: Извлечение географических координат
Цель: Написать регулярное выражение для извлечения координат в формате десятичных градусов.
'''

'''
import re
cadena = "41.40338, 2.17403"
patro = re.compile("[1-9]+[0-9]?\.[0-9]{1,5}")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 16: Validació de noms d'usuari 
Objectiu: Escriu un regex per validar noms d'usuari que només continguin caràcters 
alfanumèrics i guions baixos. 
Entrada: usuari_123, usuari-abc, usuari.abc. 
Упражнение 16: Проверка имен пользователей
Цель: Написать регулярное выражение для проверки имен пользователей, содержащих только буквенно-цифровые символы и подчеркивания.
'''

'''
import re
cadena = "usuari_123, usuari-abc, usuari.abc"
patro = re.compile("[a-z0-9_\.]+")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 17: Extracció de paraules que contenen números 
Objectiu: Escriu un regex per extreure paraules que continguin números. 
Entrada: He comprat 3pomes i 5plàtans. 
Упражнение 17: Извлечение слов, содержащих числа
Цель: написать регулярное выражение для извлечения слов, содержащих числа.
'''

'''
import re
cadena = "He comprat 3pomes i 5plàtans"
patro = re.compile("[1-9]+[a-zàáèéìíïòóùúñ]+")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 18: Detecció de codis HTML 
Objectiu: Escriu un regex per extreure etiquetes HTML d'un text. 
Entrada: <div>Hola</div>, <p>Paràgraf</p>. 
Упражнение 18: Обнаружение HTML-кодов
Цель: написать регулярное выражение для извлечения HTML-тегов из текста.
'''

'''
import re
cadena = "<div>Hola</div>, <p>Paràgraf</p>"
patro = re.compile("<[^>]+>[àáèéìíïòóùúñi\w]+<[^>]+>")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 19: Validació d'horaris 
Objectiu: Escriu un regex per validar horaris en format HH:MM (de 24 hores). 
Entrada: 14:30, 02:59, 25:00. 
Упражнение 19: Проверка времени
Цель: Написать регулярное выражение для проверки времени в формате ЧЧ:ММ (24-часовой).
'''

'''
import re
cadena = "14:30, 02:59, 25:00"
patro = re.compile("[0-1][0-9][:][0-5][0-9]")
print(patro.findall(cadena))
'''

#==========================================================

'''
Exercici 20: Identificació de cadenes entre cometes 
Objectiu: Escriu un regex per extreure cadenes entre cometes dobles d'un text. 
Entrada: "Hola", "Bon dia", 'Això no val'.
Упражнение 20: Определение строк в кавычках
Цель: Написать регулярное выражение для извлечения строк в двойных кавычках из текста.
'''

'''
import re
cadena = '"Hola", "Bon dia", \'Això no val\''
patro = re.compile("\"[A-ZÀÁÈÉÌÍÏÒÓÙÚ]{1}[\sa-zàáèéìíïòóùú]+\"")
print(patro.findall(cadena))
'''