import math
import numpy as np
import matplotlib.pyplot as plt

nameoffile = input()
data = np.genfromtxt(nameoffile, dtype='float')

myfile = open("output1.txt", mode='w', encoding='latin_1')
print(data)

uniqueEl_array=[]

uniqueElCount = 0
datasort = sorted(data)
for ele in datasort:
    if(ele not in uniqueEl_array):
        uniqueElCount += 1
        uniqueEl_array.append(ele)

print(uniqueEl_array)

name = [0 for i in range(uniqueElCount)]
freq = [1 for i in range(uniqueElCount)]
helpUniqEl = 0
helpUniqEl2 = -1
for i in range(len(datasort)):
    for j in range(uniqueElCount):
        if (datasort[i] == name[j]):
            freq[helpUniqEl2] += 1
            break
        if (j == uniqueElCount - 1):
            name[helpUniqEl] = datasort[i]
            helpUniqEl += 1
            helpUniqEl2 += 1
count = [(name[i],freq[i]) for i in range(len(freq))]
print()



print("  Name  | Count | ReactCount ")
print("--------+-------+------------")
myfile.write("\n      Name  | Count | ReactCount ")
myfile.write("\n    --------+-------+------------")

reactCount = 0
for i in range(len(count)):
    reactCount += count[i][1]
    myfile.write("\n     " + str(count[i][0]) + "\t|   " + str(count[i][1]) + "   |\t" + str(reactCount))
    if (int(count[i][0]) < 10):
        print("\t" + str(count[i][0]) + "\t|   " + str(count[i][1])+"   |\t"+ str(reactCount))
    else:
        print("\t" + str(count[i][0]) + "\t|   " + str(count[i][1])+"   |\t"+ str(reactCount))

for i in range(int(len(freq))):
    if (freq[i] == max(freq)):
       maxfilm = ('Film: ' + str(name[i]) + ' Freq: ' + str(freq[i]))
print('moda : ' + maxfilm)
myfile.write('\nmoda : ' + maxfilm)
sortedData = sorted(data)
print('mediana: ' + str(sortedData[int(len(sortedData) / 2)]))
myfile.write('\nmediana: ' + str(sortedData[int(len(sortedData) / 2)]))



sumX = 0
for i in range(int(len(freq))):
    sumX += int(name[i]) * freq[i]

sumX = sumX/int(len(data))

varX = 0
for i in range(int(len(data))):
    varX += (int(data[i])-sumX)**2

varX = varX/(len(data)-1)

print("Dispersion = " + str(round(varX,4)))
print("Standard deviation = "+str(round(math.sqrt(varX),4)))
myfile.write("\nDispersion = " + str(round(varX,4)))
myfile.write("\nStandard deviation = "+str(round(math.sqrt(varX),4)))
myfile.close()


print(sorted(data))
plt.hist(sorted(data), bins = 20, align = 'mid', facecolor = 'DARKBLUE' )
plt.show()


