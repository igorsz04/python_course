import matplotlib.pyplot as plt
import numpy as np

# plt.figure(1, figsize=(10,5))
# plt.plot([1,2,3,4],[1,4,9,16])
# plt.title('Plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.figure(2,figsize=(15,5))
# plt.plot([1,2,3,4],[1,4,9,16],'bo')

#
# x = np.arange(1,5)
# y = x**3
# plt.figure(3, figsize=(10,10))
# plt.plot([1,2,3,4],[1,4,9,16], 'go', x, y, 'rx')
#
#
# plt.figure(4)
# plt.subplot(1,2,1)
# plt.plot([1,2,3,4],[1,4,9,16])
# plt.title('first plot')
#
# plt.subplot(1,2,2)
# plt.plot(x,y,'rx')
# plt.title('second plot')
# plt.suptitle('suptitle')
#
# plt.figure(5)
# divisions = ['A','B','C','D','E']
# divisions_average = [70, 82, 73, 65, 68]
# variance = [4,6,7,8,10]
#
# plt.bar(divisions, divisions_average, yerr=variance, color='blue')
#
#
# plt.figure(6)
# plt.barh(divisions, divisions_average, xerr=variance, color='blue')
#
# plt.figure(7)
# next_divisions_average = [69, 70, 75, 69, 72]
#
# index = np.arange(5)
# width = 0.3
# plt.bar(index, divisions_average, width, color='red', label='divisions')
# plt.bar(index+ width, next_divisions_average, width, color='black', label='next divisions')
# plt.title('Divisions')
#
# plt.xlabel('First division')
# plt.ylabel('Next division')
# plt.legend()


#
# plt.figure(8)
# firms = ['Google','Amazon','PWN','ABC','SpaceX']
# market_share = [30,30,10,10,20]
# explode = [0.1, 0, 0, 0, 0]
# plt.pie(market_share,explode=explode, labels=firms, shadow=True, startangle=45)
# plt.axis('equal')
# plt.legend(title='Firms')


#rozkład normalny
plt.figure(9)
x = np.random.randn(1000)
plt.hist(x,10)

plt.figure(10)
y = np.random.randn(1000)
plt.scatter(x,y)



plt.show()