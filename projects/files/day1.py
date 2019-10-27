# one line comment

"""
multiline comments
"""

######################
# data types
######################

# dynamic typing

a = 1
print (type(a))

a = '1'
print (type(a))

a = 1.0
print (type(a))

#P0
imie = "Anna"
adres_zamieszkania = "Nieznana 20"

zmienna_1 = "Ciekawe"
zmienna_2 = "Programowanie"
zmienna_3 = "Jest"
zmienna_4 = "Wciągające"
zmienna_5 = 'I'

print (zmienna_2, zmienna_3, zmienna_1, zmienna_5, zmienna_4)

tmp = zmienna_1
zmienna_1 = zmienna_2
zmienna_2 = tmp

tmp = zmienna_2
zmienna_2 = zmienna_3
zmienna_3 = tmp

tmp = zmienna_4
zmienna_4 = zmienna_5
zmienna_5 = tmp

print (zmienna_1, zmienna_2, zmienna_3, zmienna_4, zmienna_5)


#
a = 1
b = 2

tmp = a
a = b
b = tmp

print (a) #2
print (b) #1

c = 3
d = 4

#pattern matching
c,d = d,c

print (c)
print (d)

a = 10
a = a + 5
a += 5
print (a)

imie = "James"
nazwisko = "Spring"
rok_urodzenia = "21.04.1987"
stanowisko = "dev"
placa = 4500

print (imie, nazwisko, rok_urodzenia, stanowisko, placa)



r = 100
PI = 3.14159265

print (round(PI*(r **2)))
print (round(PI*2*r))

na_km = 8/100
km = 382
print ("liczba paliwa:", km*na_km)


a = 2
b = 2 * a + 2
c = 2 * b + 2


kolorowa_na_min = 2/5
czarnobiala_na_min = 8/2
print ("liczba kartek:", round((kolorowa_na_min+czarnobiala_na_min)*45,0))

a = '1'
b = 10

print (type(int(a)))
print (type(str(b)))


a = 0o11 #system ósemkowy
print (a)


a = 0x100 #system szesnastkowy
print(a)

a = True
b = False

if 1<2:
    print ("ok")

if 1:
    print ("ok2")


print (bool(0))

print ("str" + " " + "text" + str(1))

imie = "Johnny"
nazwisko = "Ktokolwiek"
wiek = 35
stanowisko = "młodszy inżynier procesu"
pensja = 6000

print(10*("Pan "+ imie  + " " + nazwisko + " (wiek: " + str(wiek) + " lat) pracuje na stanowisku: " +stanowisko + " (pensja: " + str(pensja) + " brutto)"))

#P25
wynagrodzenie = 5500
godziny = 168
print("stawka netto:", round(wynagrodzenie/godziny,2))
print("stawka brutto:", round(wynagrodzenie*1.23/godziny,2))


if 1<3 or 1>2:
    print ("ok")

a = bool (0)
b = bool (0)
c = bool (1)

w1 = (not a) and (not b) and (not c)
w2 = (not a) and (not b) and  c
w3 = (not a) and b and  (not c)
w4 = a and (not b) and (not c)

print (w1 or w2 or w3 or w4)

print ("text\ntext\ntext")
print (r"text\ntext\ntext")
print ("text\\ntext\\ntext")


#P36
#napis = input("podaj napis: ")
#print (10*(napis + "\n"))



######################
# poszczegolne litery
######################

text = "string"
print (text[0]) #operator indeksowania

#strings are immutable!
#text[0] = 'b'

text = "hello world"
print (text.capitalize())
print (text.upper())

######################
# Tuple
######################
a = "sample text"
print (a[0])

#for each
for letter in a:
    print (letter)


a = (1,2,3,'a','b','c')
print (type(a))
print (a[5])
print (a)

for elem in a:
    print (elem)


a = (1,2,3,'a','b','c')
print (type(a))

#tuple is immutable!!!
#a[0] = 0



#######################
# List
#######################

a = [1,2,3,'a','b','c']
print (type(a))
print (a[5])

for elem in a:
    print (elem)


#aktualizacja elementu (można na liście, nie mozna na krotce - tuple)
a[0] = 0
print (a)

#append dodaje element na koncu
a.append('d')
print (a)
a.insert(0, -1)    # 0 to indeks, -1 wartość elementu
print (a)

#print (dir(a)) - pokazuje wszystkie funkcje dla tego obiektu

print (len(a))

x        = [1,2,3,4,5,6,7,8,9,10]
new_list = []

for item in x:

    if item > 3:
        new_list.append(item)
print (new_list)

even_list = []

for liczba in x:
    if liczba % 2 == 0:
        even_list.append(liczba)
print (even_list)


# 4 % 2 == 0 -> liczba parzysta


new_list = []
for item in x:
    new_list.append(item*2)
print (new_list)


#comprehension list = składanie listy
print ([elem * 2 for elem in x])

print (x[0]) #1
print (x[6]) #7
#print (a[len(x)-1])
print (x[-1])

print (x[0:6:1])   # <0,6)
print (x[0:6:2])   # <0,6) co 2 element


print (x[0:6])   #krok domyslny to 1
print (x[-1:-5])
print (x[-1:-5:-1])    # < )





########################
# set (zbiory)
########################

a = "sample text"
b = [1,2,3,1,1,2]
c = (1,2,1,2,1)

a_set = set(a)
b_set = set(b)
c_set = set(c)

print (a_set)
print (b_set)
print (c_set)


#
a = 177
a_set = set(str(a))
print (a_set)
print (len(a_set))

for item in a_set:
    print (item)

a = "sample text"
a_set = set(a)
print ('m' in a_set)


a_set.add('80')
print (a_set)

a_set.remove('80')
print (a_set)


a = [1,2,3]
del a[1]  # 2 to index elementu
print (a)



###########################
# Dictionary
###########################

numbers = {
    'a':1,
    'b':2,
    'c':3
}

print (numbers['a'])
print (numbers['b'])
print (numbers['c'])

print (numbers.keys())
print (numbers.values())
print (numbers.items())

dictionary = dict()
print (type(dictionary))

print ([1,2,3] * 3)
print ([1,2,3])


#######################


#P34

combo = [[],[]]
combo[0].append(1)
combo[0].append(2)
combo[0].append(3)
combo[1].append("Adam")
combo[1].append("Ewa")

print (combo)

print("haha")


#P35
drugie_imie = combo[1][1]


#P36
art_spoz = []
art_spoz.append("chleb")
art_spoz.append("chikker")
art_spoz.append("cheeseburger")
art_spoz.append("cola")
art_spoz.append("kebab")

print (art_spoz)
lst = (art_spoz[0:5:4])


result = ""
for elem in lst:
    result = result + elem
print (result)
print("coś")
print (" ".join(lst))



a = (1,2,3)
print (a*3)


#P38
a = ('1','2','1977')
print ("data waznosci artykulu to " + a[0] + "-" + a[1]+ "-" + a[2])
print("coś")
combo = (('1','2','1977'),('4','2','1977'),('6','2','1977'))
print ("data waznosci artykulu to " + combo[0][0] + "-" + combo[0][1]+ "-" + combo[0][2])

###########################

a = "sample text"

a_set = set(a)
print (set(a))
print("cos")
letters = dict()
for letter in a:
    if letter in letters.keys():
        letters[letter] += 1
    else:
        letters[letter] = 1
print (letters)


###tabliczka mnozenia 10x10
print("tabliczka mnożenia")

a=[1,2,3,4,5,6,7,8,9,10]
tablica2=[1,2,3,4,5,6,7,8,9,10]
for x in tablica2:
    for y in a:
        print (x*y, end="\t")
    print ("\n")

print ("koniec tabliczki")

#####################
print ("start")
even_list = []
for x in tablica2:
    for y in a:
        if x*y % 2 == 0:
            #print (x*y, end="\t")
            even_list.append(x*y)

print (len(even_list))
print (len(set(even_list)))

print ("end")

####################

a=['car','toyota','cokolwiek','whatever']
n=[]
for i in a:
    n.append(len(i))
print (n)

ac = [len(i) for i in a]
print (a)

b = [1,2,3,4,5]
result = 1
for i in b:
    result = result * i
print (result)


result = "sample text"
print (result[::-1])
print (result[::])

####################################
#OBCZAJ TO ZROB
a = "sample text"

a_set = set(a)
print (set(a))
b = list(a_set)
print (type(b))
print (b)
litery = []
print("litery = {")
#for item in b:
#    print("'"+b[item]+"':"+b[item].count(b[item]))

#CLEAN CODE - CZYSTY KOD - ROBERT C MARTIN

print ("}")





#P37
dlugosc = float(input("podaj dlugosc: "))
wysokosc = float(input("podaj wysokosc: "))
print("pole wynosi: ", dlugosc*wysokosc*0.5)




#P11
chleb = 1.99
mleko = 2.5
cuksy = 12.99

chleb_i=int(input("podaj sztuki chleba: "))
mleko_i=float(input("podaj litry mleka: "))
cuksy_i=float(input("podaj kilogramy cuksów: "))

print("zamowienie rowne ", chleb*chleb_i + mleko*mleko_i + cuksy*cuksy_i)






#kwota netto
kwota_brutto = int(input("podaj kwotę brutto: "))
podaj_VAT = int(input("podaj stawkę VAT: "))
print (round(kwota_brutto/(1+podaj_VAT/100),2))



a = int(input("podaj liczbe a:"))
b = int(input("podaj liczbe b:"))

print (2*a+2*b)

