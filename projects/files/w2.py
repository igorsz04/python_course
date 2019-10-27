#typy wartości
print(type("abc"),type("a"),type('a'))


#####################
# #struktury danych
#####################

global_temp = []
#dodawanie wartości

global_temp.append(24.5)
global_temp.append(22.3)
global_temp.append(24.1)
global_temp.append("Err")
global_temp.append(False)
global_temp.append('E')
print("Actual values: " + str(global_temp))

#wybieranie wartości z listy
i=3
print("Wskazanie czujnika "+str(i+1)+": "+str(global_temp[i]) + " st. C")

#wypisz co drugą wartość z listy
print(global_temp[::2])

#usuwanie wartości
global_temp.remove(False)
print(global_temp)
print(global_temp[4])

#usuwanie po indeksie
index = len(global_temp)-1
global_temp.pop(index)
print(global_temp)

#lista wielowymiarowa
board = [ ['_','_','_'],['_','_','_'],['_','_','_'] ]
print(board)
board[2][1] = 'X'
board[1][2] = 'O'
print(board)

#v1
for row in board:
    print(row)

#v2
for row in board:
    for i in row:
        print(i,end=' ')
    print()

#słowniki
global_temp_current = {"C1" : 24.5, "C2": 23.4, "C3" : 22.5}
print(global_temp_current)
#dodawanie klucza i wartosci do słownika
global_temp_current["C4"] = 21.1
global_temp_current["C5"] = 21.1
print(global_temp_current)

#zbiór kluczy i lista wartości
print(global_temp_current.keys())
print(global_temp_current.values())

#iterowanie po słownikach w pętli
for key in global_temp_current.keys():
    print("sensor " + key + ": " + str(global_temp_current[key]) + " st.C")

#słownik z wartościami w postaci listy
global_temp_current1 = {"C1" : ["model XYZ", "Warszawa", 24.5, "+/-0.5%"],
                       "C2" : ["model ABC", "Kraków", 22.5, "+/-0.1%"]}
print(global_temp_current1)
print(global_temp_current1["C1"][2], global_temp_current1["C1"][1])

for key in global_temp_current1.keys():
    print (key, end=' ')
    for i in global_temp_current1[key]:
        print(i, end=' ')
    print()

#jakieś zadanie rekrutacyjne - czy dwie liczby są lustrzane (palidromy)
liczba = "1221"
#liczba = input("wprowadz liczbę: ")
liczba_rev = list(liczba)
liczba_rev.reverse()
print(list(liczba)==liczba_rev)
print(liczba_rev)


#uzytkownik wprowadza liczby i algorytm zwraca tylko wartosci unikatowe
#[1,1,2,2,3,4] -> [1,2,3,4]
lista = [1,1,2,3,4,4,4]
uniquelista = set(lista)
print(uniquelista)

uniquelista.add(7)
print(uniquelista)
uniquelista.discard(7)
print(uniquelista)

print(1 in uniquelista)
print(6 in uniquelista)
print(set([1,2]) <= uniquelista)
print("subset", set([1,2]).issubset(uniquelista))
print("superset", set([1,2]).issuperset(uniquelista))

#różnica symetryczna
#wypisz wszystkie elementy występujące w każdej z list ale niebędące elementami wspólnymi
a = [1,2,3,4,5,6]
b = [3,4,5,6,7,8,9]

a1 = set(a)
b1 = set(b)
print(a1^b1)
print(a1.symmetric_difference(b1))


#wyrazenie trojargumentowe
#c = int(input("podaj liczbę: "))
#print("parzysta") if c%2==0 else print("nieparzysta")
#print("nieparzysta") if c%2 else print("parzysta")

#p48
#try:
#    print("nieparzysta") if int(input("podaj liczbe: ")) else print("parzysta")
#except:
#    print("to nie liczba!!!111")


#p49
login = input("podaj login: ")
haslo = input("podaj haslo: ")

#login, haslo, uprawnienia, aktywacja
users = [ ["mk","mk123","ROLE_ADMIN",True,0],
          ["kk", "kk123", "ROLE_USER", True,0],
          ["ll", "ll123", "ROLE_USER", True,0]]

#logowanie na podstawie listy uzytkownikow
islogged = False
for i in users:
    if (login==i[0] and haslo==i[1]):
        islogged = True
        if (i[2] == "ROLE_ADMIN"):
            print("panel administratora")
            break
        else:
            print("panel uzytkownika")
            break
print("" if islogged else "blad logowania")




#do 3 prob logowania
islogged = False
while(islogged == False):
    print(users)
    login = input("podaj logina: ")
    for i in users:
        #sprawdza czy jest taki user
        if (login==i[0] and i[3]==True):
            haslo = input ("podaj haslo: ")
            if (haslo == i[1]):
                if(i[2] == "ROLE_ADMIN"):
                    print("panel administratora")
                    break
                else:
                    print("panel uzytkownika")
                    break
            else:
                print("bledne haslo")
                i[4] +=1
                if(i[4]==3):
                    i[3] = False
        elif(login==i[0] and i[3]==False):
            print("konto zablokowane")
            break
        else:
            print("bledny login")
            break






