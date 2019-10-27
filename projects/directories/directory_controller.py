import datetime
from os import *
from time import strftime

print("Direct path:",getcwd())
print("Zawartość aktualnego katalogu: ",listdir("."))
print("Zawartość aktualnego katalogu: ",listdir("C:\\Users\\igors\\Documents\\kurs"))

for file in listdir("C:\\Users\\igors\\Documents\\kurs"):
    print(file)


#zmiana katalogu
chdir("C:\\Users\\igors\\Documents")
print(listdir("."))

mkdir("generated from python")
rmdir("generated from python")

print("rozmiary")
for file in listdir("."):
    print("%50s \t %20s MB" % (file, path.getsize(file)/1000000))


print("coś")
# P76
from datetime import datetime
from os import listdir, path, chdir


class FileOperation:
    def __init__(self):
        self.direct_path = input("wprowadź adres bezpośredni (aktualna lokalizacja .)")
        self.direct_path  = self.direct_path.replace("\\","\\\\")
        chdir(self.direct_path)
        self.getDirectoryContent()


    def getDirectoryContent(self):
        print("| %35s | %10s | %25s | %25s |" % ("FILENAME", "SIZE", "CREATED TIME", "MODIFIED TIME"))
        for content in listdir("."):
            print("| %35s | %10.2f | %25s | %25s |"
                  % (content,
                     path.getsize(content)/(10**6),
                     datetime.fromtimestamp(path.getctime(content)).strftime("%d.%m.%Y %H:%M:%S"),
                     datetime.fromtimestamp(path.getmtime(content)).strftime("%d.%m.%Y %H:%M:%S"))
                  )

FileOperation()

#chosen_dir = input("Podaj ścieżkę: ")
#if(chosen_dir =):
#    print("ścieżka nieprawidłowa")
#else:
#    print(listdir(chosen_dir))
#    print(path.getsize(chosen_dir))
#    print(path.)
