# Developed by: Ryandw11

#data = [[1.37, 1.1], [1.3, 0.2], [0.6,2.8], [3.0,3.2], [1.2, 0.7], [1.4,1.6], [1.2, 1.0], [1.2, 1.1], [0.6,1.5], [1.8, 2.6], [1.2, 1.3], [1.2,1.3], [1.2, 1.0], [0.0, 1.9]]
data = [[1.37, 1.1], [1.3, 0.2], [0.6,2.8], [3.0,3.2], [1.2, 0.7], [1.4,1.6], [1.2, 1.0], [1.2, 1.1], [0.6,1.5], [1.8, 2.6], [1.2, 1.3], [1.2,1.3], [1.2, 1.0], [0.0, 1.9], [0.4, 0.5], [0.7, 0.9], [1.3, 2.0], [1.4, 2.0], [3.0,2.0]]
x=[1.37, 1.3, 0.6, 3.0, 1.2, 1.4, 1.2, 1.2, 0.6, 1.8, 1.2, 1.2, 0.0]
y=[1.1, 0.2, 2.8, 3.2, 0.7, 1.6, 1.0, 1.1, 1.5, 2.6, 1.3, 1.0, 1.9]

groups = []
numofgroups = 2

import numpy
import math
import random
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def setXList():
    x = []
    for i in data:
        x.append(i[0])

#Randomly makeup data
def randomlyMakeData(num):
    global data
    data = []
    for i in range(0, num):
        data.append([random.random(), random.random()])


def setYList():
    y = []
    for  i in data:
        y.append(i[1])


def normalize():
    n = 0
    for i in data:
        data[n][0] = (i[0] - min(x)) / (max(x) - min(x))
        data[n][1] = (i[1] - min(y)) / (max(y) - min(y))
        n+=1

def distance(cord1, cord2):
    return numpy.sqrt(math.pow((cord2[0]-cord1[0]), 2) + math.pow((cord2[1]-cord1[1]), 2))


#Generate a single group center
def generateCenter(groupid):
    gone = 0.0
    gtwo = 0.0
    if len(groups[groupid]) == 0:
        return [random.random(), random.random()]
    for i in groups[groupid]:
        gone += i[0]
        gtwo += i[1]
    return [gone/len(groups[groupid]), gtwo/len(groups[groupid])]

#Get all of the group centers
def generateAllCenters():
    cents = []
    n = 0
    for i in groups:
        cents.append(generateCenter(n))
        n += 1
    return cents


#Multiple group
def groupPointToCenter(centers):
    gr = []
    for c in range(0, numofgroups):
        gr.append([])
    for i in data:
        dis = []
        for c in centers:
            dis.append(distance(c, i))
        dm = min(dis)
        gr[dis.index(dm)].append(i)
    return gr;




def makeClusters(num):
    global groups
    ranCents = []
    for i in range(0, num):
        ranCents.append([random.random(), random.random()])
    c = groupPointToCenter(ranCents)
    groups = c;



#MULTI
randomlyMakeData(40)
a = input("How many clusters do you want?")
print("Generating clusters...")
setXList()
setYList()
normalize()
numofgroups = int(a)
makeClusters(int(a))

for i in range(0, 999):
    g = groupPointToCenter(generateAllCenters())
    groups = g

#adding in colors for plotting
color = ["r", "b", "c", "m", "y", "k", "#ff00ff", "#227c18", "#fea800", "#00fea6", "#fecf00", "#0005ff"]
v = 0
co = 0
for i in groups:
    for x in i:
        plt.plot(x[0], x[1], color=color[co],  marker="o")
    plt.plot(generateCenter(v)[0], generateCenter(v)[1], color=color[co],  marker="*", markersize=12, label=str(len(i)) + " points")
    v+= 1
    co += 1
    if(co >= 11): co = 0
plt.legend()
plt.title("Sorted points into groups. # of groups: " + str(numofgroups))
plt.show()