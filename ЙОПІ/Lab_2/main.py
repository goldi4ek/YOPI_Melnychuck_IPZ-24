import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
data = [0]
res = open("result.txt", "w+")


def connect_txt(data):
    nameoffile = input()
    data = np.genfromtxt(nameoffile, dtype='int')
    data = np.delete(data, 0)
    return data


def diagramlist(i):
    print("\nList diagram")
    print("------------------------")

    res.write("\n\nList diagram")
    res.write("\n------------------------")

    key = 0
    keycount = 0
    while i <= max(data):
        mas = []
        for j in range(len(data)):
            if i < data[j] < i + 10:
                if key == 0:
                    key = data[j]
                mas.append(data[j] % 10)
            elif data[j] == i:
                if key == 0:
                    key = i
                mas.append(0)

        if not mas and keycount < 2:
            key = 0
        else:
            keycount += 1

        print(str(i / 10) + " \t| " + str(mas))

        res.write("\n"+str(i / 10) + " \t| " + str(mas))
        i += 10
    print("Key = " + str(key))

    res.write("\nKey = " + str(key))

def pfunc(pindex):
    index = pindex * (count + 1)-1
    Percentile = data[int(index)] + (index % int(index)) * (data[int(index) + 1] - data[int(index)])
    return Percentile


def standartdeviation():
    sum = 0
    totalSum = 0
    for i in range(len(data)):
        sum += data[i]
    midleX = sum / len(data)

    for i in range(len(data)):
        totalSum += (data[i] - midleX)**2

    result = np.sqrt(totalSum/(len(data)-1))

    res.write("\nStandart deviation = " + str(result))

    return result


def middledeviation():
    sum = 0
    totalSum = 0
    for i in range(len(data)):
        sum += data[i]
    midleX = sum / len(data)
    for i in range(len(data)):
        totalSum += abs(data[i] - midleX)

    result = (totalSum/(len(data)))

    res.write("\nMiddle deviation = " + str(result))

    return result


def lineal():
    sum = 0
    result = []
    for i in data:
        sum += i
    midle = sum / len(data)

    a = np.array([
        [100*1, 1, ],
        [1*midle, 1, ]
        ])
    x = solve(a, np.array([100, 95]))
    print("\na = " + str(x[0]) + "\nb = " + str(x[1]))
    for i in range(len(data)):
        result.append(x[0]*data[i]+x[1])
    print("\nResult marks: " + str(result))

    res.write("\na = " + str(x[0]) + "\nb = " + str(x[1]))
    res.write("\nResult marks: " + str(result))


def boxdiagram():
    plt.boxplot(data)
    plt.grid()
    plt.show()


'''------------- MAIN ------------'''

data = connect_txt(data)
print("Enter data = " + str(data))
data = sorted(data)
print("Sorted data = " + str(data))
count = len(data)

res.write("\nEnter data = " + str(data))
res.write("\nSorted data = " + str(data))

Q1 = pfunc(1/4)
Q3 = pfunc(3/4)
P90 = pfunc(0.9)

print("\nFirst quartile = ", Q1)
print("\nThird quartile = ", Q3)
print("\n90's percentile = ", P90)

res.write("\nFirst quartile = " + str(Q1))
res.write("\nThird quartile = " + str(Q3))
res.write("\n90's percentile = " + str(P90))

minimal = min(data)
maximal = max(data)

print("\nStandart deviation = ", standartdeviation())
print("\nMiddle deviation = ", middledeviation())

lineal()

diagramlist(min(data))
res.close()
boxdiagram()
