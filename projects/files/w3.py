import datetime
from random import sample


class Player:
    def __init__(self, n, ln, h, w):
        self.height = h
        self.weight = w
        self.name = n
        self.lastname = ln


    def calculateBMI(self):
        bmi_calc = self.weight/pow(self.height/100,2)
        return bmi_calc

    def __str__(self):
        return "Imię: %-10s Nazwisko: %-10s BMI: %-15.2f" % (self.name, self.lastname, self.calculateBMI())


player1 = Player(n="Igor",ln="Szczęsny",h=185,w=73)
player2 = Player("Filip","Fiszcz",183,80)
player3 = Player("Piotr","Wójcik",186,110)

print(player1)
print(player2)
print(player3)


#P68
class Lotto:
    def __init__(self):
        self.result=[]

    def starting(self):
        self.result = sample(range(1,50),6)
        print(self.__str__())
    def sorting(self):
        #sortowanie listy
        self.result = sorted(self.result, reverse=True)
        print(self.__str__())
    def __str__(self):
        return "%s data losowania: %s "% (self.result, datetime.datetime.today().strftime("%d.%m.%Yr"))

lotto1 = Lotto()
lotto1.starting()
lotto1.sorting()

#P67 - zróbże w domu
last_insert_index = 0

class Student:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        # odwołanie do globalnej wartości w skrypcie
        global last_insert_index
        last_insert_index += 1
        self.index_no = last_insert_index
        # pusta lista ocen
        self.grades = []
    def calculateAvg(self):
        sum11 = 0
        for grade1 in self.grades:
            sum11 += grade1
        if(len(self.grades) == 0):
            return 0
        return sum11/len(self.grades)
    def __str__(self):
        return "| %06d | %15s | %15s | %25s | %5.2f |" % \
               (self.index_no,self.name,self.lastname,self.grades, self.calculateAvg())

class StudentController:
    def __init__(self):
        self.students = []
    def __str__(self):
        output = ""
        for student in self.students:
            output += student.__str__() + "\n"
        return output
    #metoda dodająca studenta do listy
    def addStudent(self, name, lastname):
        student = Student(name, lastname)
        self.students.append(student)
    def findStudentByIndex(self,index_no):
        for student in self.students:
            if(index_no == student.index_no):
                return student
                print(student)
        return None
    def deleteStudentByIndex(self,index_no):
        deletedStudent = self.findStudentByIndex(index_no)
        if(deletedStudent != None):
            self.students.remove(deletedStudent)
            print("usunięto szkodnika")
        else:
            print("Nie ma takiego studenta")

    def addGradesToStudent(self, index_no, new_grades):
        findStudent = self.findStudentByIndex(index_no)
        if(findStudent != None):
            findStudent.grades.extend(new_grades)
            print("zaktualizowano listę ocen szkodnika")
    def deleteStudentGrades(self, index_no):
        findStudent = self.findStudentByIndex(index_no)
        if(findStudent != None):
            findStudent.grades = []
            print("wyczyszczono liste ocen")

dziekanat = StudentController()
