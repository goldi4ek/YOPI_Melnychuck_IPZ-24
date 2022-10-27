import math

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

res = open("result.txt", "w+")


def connect_txt():
    inputdata = []
    # nameoffile = input()
    input = open('input_10.txt')
    input.seek(1)
    for line in input:
        inputdata.append(input.read(3))
        input.read(1)
        inputdata.append(input.read(2))
    print(inputdata)
    for i in range(int(len(inputdata))):
        inputdata[i] = inputdata[i].replace(',', '.')

    data = [[0 for i in range(2)] for j in range(int(len(inputdata) / 2))]
    index0 = 0
    index1 = 0
    for i in range(int(len(inputdata))):
        if i % 2 == 0:
            data[index0][0] = float(inputdata[i])
            index0 +=1
        elif i % 2 != 0:
            data[index1][1] = int(inputdata[i])
            index1 += 1
    return data


def dataX(data):
    inputdatadata = []
    for i in range(len(data)):
        inputdatadata.append(data[i][0])
    return inputdatadata


def dataY(data):
    inputdatadata = []
    for i in range(len(data)):
        inputdatadata.append(data[i][1])
    return inputdatadata


def diffusiondiagram(data):

    infoX = dataX(data)
    infoY = dataY(data)

    plt.scatter(infoX, infoY, c='coral', marker="o")
    plt.grid()
    plt.show()


def middleXY(data):
    global middlex, middley
    middlex = 0.0
    middley = 0.0

    for i in range(len(data)):
        middlex += data[i][0]
        middley += data[i][1]

    middlex = middlex / len(data)
    middley = middley / len(data)


def covariance(data):
    covariance = 0.0
    print("\nMean x = " + str(middlex))
    print("Mean y = " + str(middley))

    res.write("\nMean x = " + str(middlex))
    res.write("\nMean y = " + str(middley))

    for i in range(len(data)):
        covariance += (data[i][0] - middlex)*(data[i][1] - middley)

    return covariance/(len(data))


def regretionline(data):
    dobXY = 0.0
    sumX = 0
    sumY = 0
    sumdobXX = 0

    for i in range(len(data)):
        dobXY += data[i][0]*data[i][1]
        sumX += data[i][0]
        sumY += data[i][1]
        sumdobXX += data[i][0]**2

    b = (len(data) * dobXY - (sumX * sumY)) / ((len(data) * sumdobXX) - sumX**2)

    x, y = sp.symbols("X, Y")

    line = sp.Eq(y - middley, b * (x - middlex))

    lineX = sp.solve(line, y)
    lineY = sp.solve(line, x)

    print("\nY = " + str(lineX))
    print("X = " + str(lineY))

    res.write("\n\nY = " + str(lineX))
    res.write("\nX = " + str(lineY))


def correliation (data):
    chis = 0.0
    sumXX = 0.0
    sumYY = 0.0
    for i in range(len(data)):
        chis += (data[i][0] - middlex)*(data[i][1] - middley)
        sumXX += (data[i][0] - middlex)**2
        sumYY += (data[i][1] - middley)**2

    return chis/(math.sqrt(sumXX*sumYY))


def gravitycenter (data):
    chis = 0
    znam = 0
    for i in range(len(data)):
        chis += data[i][0]*data[i][1]
        znam += data[i][0]
    return chis/znam


def trand(data):
    if data[0][1] > data[len(data)-1][1]:
        print("Negative trand")
    elif data[0][1] < data[len(data)-1][1]:
        print("Positive trand")
    else:
        print("no trand")


data = connect_txt()
trand(data)
data = sorted(data)
print(data)

res.write("\nEnterdata:\n" + str(data))

diffusiondiagram(data)

middleXY(data)

covariance = covariance(data)
gravitycenter = gravitycenter(data)
print("\nGravitycenter = "+ str(gravitycenter))
print("\nCovariance = " + str(covariance))

res.write("\n\nGravitycenter = "+ str(gravitycenter))
res.write("\n\nCovariance = " + str(covariance))


regretionline(data)
print("\nCorrelation = " + str(correliation(data)))

res.write("\n\nCorrelation = " + str(correliation(data)))


