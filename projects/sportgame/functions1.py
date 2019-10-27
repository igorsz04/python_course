import pymysql
from projects.sportgame import host, user, password, db
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import statistics
import numpy

class SeasonsManager:

    def __init__(self, host, user, password, db):
        """
        class constructor:
        -) connect to DB
        """
        self.conn = pymysql.connect(host=host, user=user, password=password, charset='utf8', db=db)

    def CalendarUpdate (self):
        pass


    def TeamsUpdate (self):
        pass


    def SkillsUpdate (self):
        pass


class RacesManager:

    def __init__(self):
        pass



    def RacesResults (self):
        pass
        #for race in grandprix:


    def Race(self):
        cursor = self.conn.cursor()
        cursor.execute(get_riders_iq_query)
        self.conn.commit()

class RidersManager:
    def __init__(self):
        pass

    def Riders(self):
        pass


mu = 1
sigma = 0.1


conn = pymysql.connect(host=host, user=user, password=password, charset='utf8', db=db)
cursor = conn.cursor()
cursor.execute(get_riders_all_query)
conn.commit()
riders = cursor.fetchall()
riders_in_season = []
for rider in riders:
    rider = list(rider)
    rider.append(float)
    rider.append(int)
    rider.append(float)
    rider.append(float)
    rider[9] = float(rider[9])
    rider[13] = 0
    print("rider: ", rider)
    if rider[4] == 1:
        riders_in_season.append(rider)


print("riders in season: ", riders_in_season)
# print("riders in season: ", riders_in_season[0][1]) = Valentino
cursor.execute(get_rounds_all_query)
conn.commit()
rounds = cursor.fetchall()
season_calendar = []
for round in rounds:
    round = list(round)
    print("round: ", round)
    if round[0] == 1:
        season_calendar.append(round[1])
print(season_calendar)

print("\n\nDRUŻYNY:\n\n")
cursor.execute(get_teams_all_query)
conn.commit()
teams = cursor.fetchall()
teams_in_championship = []
for team in teams:
    team = list(team)
    team.append(float)
    print("team: ", team)
    teams_in_championship.append(team)

print("rozkład : \n", float(stats.norm.rvs(1, 0.04, size=1)))
print(teams_in_championship)
print(type(team))


mu = 1
sigma = 0.1

def takeResult(data):
    return data[14]

for race in season_calendar:
    for team in teams_in_championship:
        team[6] = float(stats.norm.rvs(1, 0.04, size=1))
    for rider in riders_in_season:
        for team in teams_in_championship:
            if rider[3] == team[1]:
                rider[15] = float(team[6])
        rider[12] = float(stats.norm.rvs(mu, sigma, size=1))
        rider[14] = (rider[9]*rider[12]*rider[15])
    riders_in_season.sort(key=takeResult, reverse=True)
    riders_in_season[0][13] = riders_in_season[0][13] + 25
    riders_in_season[1][13] = riders_in_season[1][13] + 20
    riders_in_season[2][13] = riders_in_season[2][13] + 16
    riders_in_season[3][13] = riders_in_season[3][13] + 13
    riders_in_season[4][13] = riders_in_season[4][13] + 11
    riders_in_season[5][13] = riders_in_season[5][13] + 10
    riders_in_season[6][13] = riders_in_season[6][13] + 9
    riders_in_season[7][13] = riders_in_season[7][13] + 8
    riders_in_season[8][13] = riders_in_season[8][13] + 7
    riders_in_season[9][13] = riders_in_season[9][13] + 6
    riders_in_season[10][13] = riders_in_season[10][13] + 5
    riders_in_season[11][13] = riders_in_season[11][13] + 4
    riders_in_season[12][13] = riders_in_season[12][13] + 3
    riders_in_season[13][13] = riders_in_season[13][13] + 2
    riders_in_season[14][13] = riders_in_season[14][13] + 1

    print("wyniki po wyścigu w: ", race)
    for rider in riders_in_season:
        print(rider)


def takeStandings(data):
    return data[13]

print("resultsy: \n")
riders_in_season.sort(key=takeStandings, reverse=True)
for rider in riders_in_season:
    print(rider, "\n")

i = 0
print("\n\n\nWYNIKI PO SEZONIE:\n")
print("| %4s | %12s | %14s | %20s | %6s |" % ("No.", "Name", "Last name", "Team", "Points"))
for rider in riders_in_season:
    i = i+1
    print("| %4i | %12s | %14s | %20s | %6i |" % (i, rider[1], rider[2], rider[3], rider[13]))






##############################
# TRANSFERY
##############################
for team in teams_in_championship:
    print(team[1], team[5])


print("\n\nZawodnik-wiek-skill-wartość: \n")
for rider in riders_in_season:
    if (rider[11]<=25 and rider[9]>=77):
        rider_value = 2500000 - (int(rider[11]) - 25)*500000 + 5000000+(int(rider[9]) - 80)*300000
    elif (rider[9]<66):
        rider_value = 2000000 - (rider[11]-25)*200000
    else:
        rider_value = 2500000 - (int(rider[11]) - 35)*200000 + 4000000+(int(rider[9]) - 80)*400000
    print(rider[1], rider[2], rider[11], rider[9], int(rider_value))


print(teams_in_championship)
riders_preseason_prediction = []
print("riderspreseasonpred: ", riders_preseason_prediction)
i=0
for rider in riders_in_season:
    for team in teams_in_championship:
        if rider[3] == team[1]:
            mean1 = rider[9]*team[4]
            mean1 = int(mean1)
    print(rider[1],rider[2], mean1)
    riders_preseason_prediction.append([rider[1], rider[2], mean1])


def prediction(dat):
    return dat[2]
riders_preseason_prediction.sort(key=prediction, reverse=True)
print("\nprzedsezonowe predykcje: \n")
for rider in riders_preseason_prediction:
    print(rider)




# y = np.random.gamma(2,2,50)
# x = np.linspace(0,50)
# s = np.random.gamma(2, 2, 1000)
# print("y: ", y)
# plt.plot(np.random.gamma(2, 2,100 ))
#









x = np.linspace (0, 1.6, 200)
y1 = stats.gamma.pdf(x, a=2, loc=0.5)
mu = 1
sigma = 0.04
y3 = stats.norm.pdf(x, mu, sigma)
plt.plot(x, y3, "b-")



z = stats.norm.pdf(x, mu, sigma)
c = stats.norm.cdf(x, mu, sigma)
r = stats.norm.rvs(mu, sigma, size=500)

#print("z: ", z)
#print("r: ", r)
print("średnia r: ", sum(r)/500, "\nmediana r: ", statistics.median(r),
      "min r: ", min(r), "max r: ", max(r))


a = numpy.array(r)
plt.hist(a, bins = 4, normed=True)

#plt.show()