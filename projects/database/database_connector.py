import pymysql

class DatabaseConnector:
    def __init__(self):
        self.loginToDbServer("localhost","python_user","123","python_db")
        menu = input("(S) - select\n(I) - insert\n(D) - delete\n(U) - update")
        if(menu.upper()=="S"):
            self.selectFromUsers()
        elif(menu.upper()=="I"):
            self.insertIntoUsers(input("imię"), input("nazwisko"), input("data urodzenia"), input("pensja"),
                                 input("płeć"))

        elif(menu.upper()=="D"):
            self.deletefromUsers(input("id: "))

        elif(menu.upper()=="U"):
            self.updateUsers(input("id: "), input("nowe salary: "))


        decision = input("Potwierdź dane (T/N): ")
        if(decision.upper() == "T"):
            #przeniesienie danych z bufora pamieci do DB
            self.connect.commit()
        else:
            #wycofanie wprowadzonych danych
            self.connect.rollback()
        self.selectFromUsers()
    def loginToDbServer(self, host, user_login, user_password, db_name):
        """

        :param host:
        :param user_login:
        :param user_password:
        :param db_name:
        :return:
        """
        try:
            #globalny obiekt polaczenia

            self.connect = pymysql.connect(host,user_login,user_password,db_name)
            self.coursor = self.connect.cursor()
            print("Ustanowiono połączenie z bazą danych")
        except:
            print("Błąd połączenia z bazą danych")
    def selectFromUsers(self):
        sql_query = "SELECT * from users"
        #metoda wykonująca zapytanie
        self.coursor.execute(sql_query)
        print("| %3s | %10s | %12s | %12s | %12s | %6s |" % ("ID", "IMIĘ", "NAZWISKO", "URODZINY", "PENSJA", "GENDER"))
        #zwrócenie tabelki wynikowej
        for user in self.coursor.fetchall():
            print("| %3d | %10s | %12s | %12s | %10.2fzł | %6s |" % (user[0], user[1], user[2],user[3],user[4],user[5]))
    def insertIntoUsers(self, name, lastname, birthdate, salary, gender):
        self.coursor.execute("INSERT INTO users VALUES (default, %s, %s, %s, %s, %s)",
                             (name,lastname,birthdate,salary,gender))

    def deletefromUsers(self, id):
        self.coursor.execute("DELETE FROM users WHERE id = %s",(id))

    def updateUsers(self,salary, id):
        self.coursor.execute("UPDATE users SET salary = %s WHERE id = %s ", (id, salary))



DatabaseConnector()