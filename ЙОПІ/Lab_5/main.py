import math
from scipy import integrate


def combinations(m, n):
    return (math.factorial(n))/(math.factorial(m) * math.factorial(n-m))


def bernoulli(m, n, prob):
    return (combinations(m, n) * math.pow(prob, m) * math.pow(1 - prob, n - m))


def gausFunction(m, n, prob):
    return ((m-n*prob)/(math.sqrt(n*prob*(1-prob))))


def tableForGaus(x):
    return (1/math.sqrt((2*math.pi)))*math.exp(-x**2/2)

def f(x):
    return math.exp(-x**2/2)


def tableForLaplass(x):
    integral = integrate.quad(f, 0, x)[0]
    return (1/math.sqrt((2*math.pi))) * integral


def moavreLaplace(m, n, prob):
    return (1 / math.sqrt(n * prob * (1-prob)) * tableForGaus(gausFunction(m, n, prob)))


def integralLaplase(m1, m2, n, prob):
    return tableForLaplass(gausFunction(m2, n, prob)) - (tableForLaplass(gausFunction(m1, n, prob)))


def mostProbablyNumber(n, prob):
    q = 1 - prob
    m1 = (n * prob) - q
    m2 = (n * prob) + prob
    b = (m2 - m1) / 2
    return round(m1+b)


print("Task 1 - probability: ", str(round(bernoulli(3, 5, 0.2) * 100, 2)) + "%")

print("\nTask 2: \na) (4 times):  \nProbability:", str(bernoulli(4, 5, 0.8) * 100) + "%")
print("b) (more or equal than 4 times):""  \nProbability:", str((1 - bernoulli(1, 5, 0.8) - bernoulli(2, 5, 0.8) - bernoulli(3, 5, 0.8)) * 100) + "%")

print("\nTask 3 - probability: ", str(round(moavreLaplace(80, 400, 0.2) * 100, 2)) + "%")

print("\nTask 4 - probability: ", str(round(moavreLaplace(5, 100000, 0.0001) * 100, 2)) + "%")

print("\nTask 5 - probability: ", str(round(integralLaplase(228, 252, 600, 0.4) * 100, 2)) + "%")

print("\nTask 6 - the most probably number: ", mostProbablyNumber(100, 0.4))

print("\nTask 7 - probability: ", str(round(integralLaplase(0, 170, 4000, 0.04) * 100)) + "%")

print("\nTask 8 - probability: ", str(round(moavreLaplace(5000, 10000, 0.5) * 100, 3)) + "%")

print("\nTask 9 - probability: ", str(round(moavreLaplace(5, 1000, 0.002) * 100, 3)) + "%")

print("\nTask 10 - the most probably number: ", mostProbablyNumber(150, 0.03))