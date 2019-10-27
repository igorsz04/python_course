from random import choices, randint
from time import localtime

from math import sqrt

returnedValue = localtime()
print(returnedValue)

productsNames = ["A","B","C"]
productsPrice = [1.99,2.33,5.00]

#metoda prezentująca zawartosc sekwencji
def printSequence(sequence):
    for element in sequence:
        print(element, end=" ")
    print()

printSequence(productsNames)
printSequence(productsPrice)
printSequence([1,3,4,5,6,7,8,9,5,3])

"""
1. Szukanie min i max [1,23]
2. 1 -> 0, 23 -> 1
3. (23-1) = 22 | 4 -> 3/22
"""
data = [1,23,4,2,4,1,4]
print("zadanko")

def findMinimum(data):
    return min(data)

def findMaximum(data):
    return max(data)

def findExtrema(data):
    return min(data),max(data)


def normalizeDataset(data, lowBorder=0, topBorder=1):
    normalizedData = []
    a = abs(lowBorder - topBorder) / abs(findExtrema(data)[0] - findExtrema(data)[1])
    b = topBorder - (a*findExtrema(data)[1])
    for elem in data:
        normalizedData.append(a*elem+b)
    return normalizedData

data = [1,23,4,2,4,1,4]     #do znormalizowania od 0 do 1

print(normalizeDataset(data))

def printDataset(data):
    for elem in data:
        print("%6.3f" % elem, end=" ")
    print()

printDataset(data)



#dowolna liczba argumentów
def gradesAvg(*grades):
    sum = 0
    for grade in grades:
        sum+=grade
    return sum/len(grades)

print("uczen 1:", gradesAvg(2,3,1,4,5,6),gradesAvg(4,5),gradesAvg(4,4,4,4))



#p57
def silnia(n):
    siln = 1
    i=1
    if (n==0):
        return 1
    for i in range(1,n+1):
        siln = siln*i
    return siln

print(silnia(18))


#rekurencyjnie
def silnia2(n):
    siln = n
    if(n==1):
        return 1
    return n * silnia2(n-1)

print(silnia2(18))



#P58
def fibo(n):
    i1 = 0
    i2 = 1
    suma = 2
    for i in range(1,n):
        m=i2
        i2+=i1
        i1 = m
        suma=suma+i1+i2
    i=i1+i2
    return i, suma


print(fibo(8))

def fibonacciSeries(n):
    fib=[]
    sum=0
    for index, value in enumerate(range(0,n+1)):
        if(index == 0):
            fib.append(0)
        elif(index == 1):
            fib.append(1)
        else:
            fib.append(fib[index - 1] + fib[index - 2])
        sum += fib [index]

    return fib, fib[n], sum

print (fibonacciSeries(15))

content = "Ciąg został omówiony w roku 1202 przez Leonarda z Pizy, zwanego Fibonaccim, " \
"w dziele Liber abaci jako rozwiązanie zadania o rozmnażaniu się królików. " \
"Nazwę ciąg Fibonacciego spopularyzował w XIX w. Edouard Lucas"

"""
1. Podziel zdanie na wyrazy
2. Losuj wyrazy i przypisz je do wygenerowanego zdania

"""

#def random_sentence(content):
 #   return content.split(" ")
  #  print(content.split(" "))
   # generatedSentence = choices(content.split(" "),5)

#random_sentence(content)


def splitSentenceBySeparator(content, separator):
    return content.split(separator)
def createSentenceByListOfWords(listOfWords):
    sentence = ""
    for word in listOfWords:
        sentence += word + " "
    return sentence + "."
def generateSentence(content, n = 5):
    words = splitSentenceBySeparator(content, " ")
    generatedSentence = choices(words, k = n)
    return createSentenceByListOfWords(generatedSentence)

print(generateSentence(content))


#P60

def distance(a1,a2,b1,b2):
    a_wsp = [a1,a2]
    b_wsp = [b1,b2]
    odleglosc = sqrt(pow(b1-a1,2)+pow(b2-a2,2))
    return odleglosc

print(distance(0,0,3,4))


#P61 - ciąg geometryczny
def geometricSeries(a1,q,n):
    an=a1*pow(q,n-1)
    suma = 0
    for i in range (1,n+1):
        suma = suma+(a1*pow(q,i-1))
    return an, suma

print (geometricSeries(2,3,5))


#P63 - <span style="color: color_name; font-size: value; “>content</span>
def getHTMLspanCode(color, fontSize, content, repetition = 1):
    html = '<span style="color: %s; font-size: %s; “>%s</span>\n' % (color, fontSize, content)
    html = html * repetition
    return html


print(getHTMLspanCode("black",12,"HUEHUE",3))


#^ zadanie: dodaj argument określający ile duplikatów znacznika ma byc wygenerowanych ^

posts = ["Post1","Post2","Post3","Post4"]

def generateHtmlSpanCode(posts, color = "black", fontSize = 12):
    html_content = ""
    for post in posts:
        html_content += '<h1 style="color: %s; font-size: %s;">%s</h1>\n' % (color, fontSize, post)
    return html_content

# print(generateHtmlSpanCode(posts, "red", 16))
print(generateHtmlSpanCode(posts))

def generateHtmlSpanCodeWithBackground(posts, color = "black", fontSize = 12):
    html_content = ""
    backgrounColor = "black"
    for post in posts:
        html_content += '<h1 style="color: %s; font-size: %s; background-color: %s">%s</h1>\n' % \
                        (color, fontSize, backgrounColor, post)
        if(backgrounColor == "black"):
            backgrounColor = "white"
        else:
            backgrounColor = "black"
    return html_content

print(generateHtmlSpanCodeWithBackground(posts, color = "red"))

# color = "black"
def generateDifferentColors(color1 = "black", color2 = "white"):
    global color
    if(color == color1):
        color = color2
    else:
        color = color1
    return color

color = "black"
print(generateDifferentColors("red","yellow"))
print(generateDifferentColors("red","yellow"))
print(generateDifferentColors())


#P65
def RandomValues(minsup,maxsup,ilosc): #samemu
    suma=0
    liczby=[]
    for i in range(1,ilosc):
        nnn = randint(-1000,1000)
        if nnn<minsup or nnn>maxsup:
            nnn=0
        else:
            suma=suma+nnn
        liczby.append(nnn)
    return suma, liczby

print(RandomValues(-900,900,30))


def generateSignal(n): #z gita
    signal = []
    for i in range(0, n):
        signal.append(randint(-1000, 1000))
    return signal
def sumRandomValuesWithSuport(minSupp, maxSupp, n): #z gita
    signal = generateSignal(n)
    processedSignal = []
    sum = 0
    sumProcessed = 0
    for i,v in enumerate(signal):
        sum += v
        if(v < minSupp or v > maxSupp):
            processedSignal.append(0)
        else:
            processedSignal.append(v)
            sumProcessed += v
    return signal, sum, sum/len(signal), processedSignal,sumProcessed, sumProcessed/len(processedSignal)

x = sumRandomValuesWithSuport(-900,900,100000)
print(x[0],x[1],x[2])
print(x[3],x[4],x[5])
print(x[2],x[5])