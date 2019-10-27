import datetime
import urllib


class User:
    def __init__(self, login, password):
        self.login=login
        self.password=password
        self.permissionSelect = True
    def readPost(self):
        if(self.permissionSelect):
            print("Reading...")
    def __str__(self):
        return "login: %s, password: %s, permissions: %s" % (self.login, self.password, ("SELECT " if (self.permissionSelect == True) else ""))

class Moderator(User):
    def __init__(self, login, password):
#        self.login=login
#        self.password=password
#        self.permissionSelect = True

        super().__init__(login, password)
        self.permissionInsert = True
    def writePost(self):
        if(self.permissionInsert):
            print("Writing...")
    def __str__(self):
        return super().__str__() + "INSERT " if self.permissionInsert else ""

class Admin(Moderator):
    def __init__(self,login,password):
        super().__init__(login, password)
        self.permissionDelete = True
        self.permissionUpdate = True
    def updatePost(self):
        print("Updating...")
    def deletePost(self):
        print("Deleting...")
    def __str__(self):
        return super().__str__() + ("DELETE " if self.permissionDelete else "") + ("UPDATE " if self.permissionUpdate else "")


user = User("user1","user11")
print(user)
user.readPost()
moderator = Moderator("mod","moderejter123")
print(moderator)
moderator.readPost()
moderator.writePost()
admin = Admin("adminek","admin1341212")
print(admin)
admin.readPost()
admin.writePost()
admin.updatePost()
admin.deletePost()



########################################
# P71
########################################

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return "Produkt %s kosztuje %s zł" % (self.name, self.price)

class Software(Product):
    def __init__(self, name, price, language, system):
        super().__init__(name, price)
        self.language = language
        self.system = system
    def __str__(self):
        return super().__str__() + " w języku %s i systemie %s" % (self.language, self.system)

class Studies(Software):
    def __init__(self, name, price, language, system, date):
        super().__init__(name,price,language,system)
        self.date = date
    def __str__(self):
        return super().__str__() + " z którego szkolenie jest w dniu %s" % (self.date)

print("")
print("Zadanie P71!!!111")
print("")
product = Product ("produkt1", 4)
print(product)
software = Software("Oprogramowanie",2000, "Java","Windows")
print(software)
studies = Studies("Szkolenie",5000,"JavaScript","Windows",datetime.datetime.today().strftime("%d.%m.%Yr"))
print(studies)



##################
# P72
##################
print("\nzadanie P72!!!!11\n")

class RGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __add__(self, other):
        color = RGB(self.r + other.r, self.g + other.g, self.b + other.b)
        return ""
    def __str__(self):
        return "RGB[%d, %d, %d]" % (self.r, self.g, self.b)

red = RGB(255,0,0)
green = RGB(0,255,0)
blue = RGB(0,0,255)

print(red,green,blue)


help(urllib)
print(dir(urllib))