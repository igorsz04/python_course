class Auto:
    # pola obiektowe
#    marka = "Audi"
 #   model = "A4"
  #  cena = 200000.
    def __init__(self, marka, model, cena = 10000):
        self.marka = marka
        self.model = model
        self.cena = cena

    # metody obiektowe
    def getAuto(self):
        print("Marka: %s model: %s cena: %.2f" % (self.marka, self.model, self.cena))
    def setCena(self,nowa_cena):
        self.cena = nowa_cena

# utworzenie obiektu klasy Auto
a1 = Auto("BMW","5",150000)
a1.getAuto()
a1.setCena(180000)
a1.getAuto()
a2 = Auto("Toyota","Avensis")
a2.getAuto()