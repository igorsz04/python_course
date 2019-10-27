A = set([1,2,3,1])
print(A)
print(len(A))
print(2 in A)
print(4 in A)
B = set([3,4,5,6])
print(B)
D = A | B
E = A&B
F = A - B
G = A^B
print(D)
print(E)
print(F)
print(G)

range(5)
print(range(5))
for x in range(5):
    print(x)
print("koniec")
for x in range(1,5):
    print(x)
print("koniec2")
for x in range(1,5,2):
    print(x)
print("koniec3")

for x in range(5,100,10):
    print("%4i%4i%8i" % (x,x**2,x**3))


print("WARCABY")

for i in range (0,4):
        Krotka1 = ("O","Ó")
        Krotka2 = ("Ó","O")
        Krotka1 *= 4
        Krotka2 *= 4
        if (i == 0):
            for m in Krotka1:
                print("M")
        print(Krotka1)
        print(Krotka2)
warcaby = (Krotka1, Krotka2)
print("Warcaby2:")
print(warcaby)
print(warcaby[1][2])

board = [ ['_','_','_'],['_','_','_'],['_','_','_'] ]
print(board)
board[2][1] = 'X'
board[1][2] = 'O'
print(board)