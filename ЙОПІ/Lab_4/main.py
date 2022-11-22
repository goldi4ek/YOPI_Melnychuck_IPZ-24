
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


def combinations(n, m):
    return factorial(n)/(factorial(m)*factorial(n-m))


def task1(black, brown, red, blue):
    sum = black + brown + red + blue
    return ((red + blue)/(sum)) * 100


def task2():
    return ((combinations(8, 2) + combinations(8, 1))/combinations(10, 2)) * 100


def task3():
    return round((1 - (combinations(8, 3)/combinations(10, 3))) * 100, 2)


def task4(p1, p2, p3, p4):
    return round((1 - p1 - p2 - p3 - p4) * 100,2)


def task5(total, choose, take):
    return round((choose**take/total**take) * 100, 2)


def task6(prob1, prob2):
    return round((prob1 * prob2) * 100,2)


def prob7task(count, prep, totalCount, bestMark):
    return (count/totalCount) * (prep/bestMark) * ((prep - 1) / (bestMark - 1)) * ((prep - 2) / (bestMark - 2))

def task7(CountBest, CountGood, CountMiddle, CountBad, PrepBest, PrepGood, PrepMiddle, PrepBad,TotalCount, BestMark, mark):
    bestProb = prob7task(CountBest, PrepBest, TotalCount, BestMark)
    goodProb = prob7task(CountGood, PrepGood, TotalCount, BestMark)
    middleProb = prob7task(CountMiddle, PrepMiddle, TotalCount, BestMark)
    badProb = prob7task(CountBad, PrepBad, TotalCount, BestMark)

    totalProb = bestProb + goodProb + middleProb + badProb

    match mark:
        case "Best":
            return round((bestProb / totalProb) * 100, 2)
        case "Good":
            return round((goodProb / totalProb) * 100, 2)
        case "Middle":
            return round((middleProb / totalProb) * 100, 2)
        case "Bad":
            return round((badProb / totalProb) * 100, 2)
        case _:
            return "Wrong mark"


def prob(first, second, third, probFrist, probSecond, probThird):
    return round(first * probFrist + second * probSecond + third * probThird, 2)


def task9(first, second, third, probFrist, probSecond, probThird):
        return round(((prob(second,0, 0, probSecond, 0, 0))/(prob(first, second, third, probFrist, probSecond, probThird))) * 100,2)


def task10(first, second, probFrist, probSecond):
    return round(((prob(first,0, 0, probFrist, 0, 0))/(prob(first, second, 0, probFrist, probSecond, 0))) * 100,2)

print("Task 1 - probability: ", str(task1(40, 26, 22, 12)),"%")
print("Task 2 - probability: ", str(task2()),"%")
print("Task 3 - probability: ", str(task3()),"%")
print("Task 4 - probability: ", str(task4(0.15, 0.25, 0.2, 0.1)),"%")
print("Task 5 - probability: ", str(task5(120, 80, 2)),"%")
print("Task 6 - probability: ", str(task6(0.9, 0.8)),"%")
print("Task 7 - probability: ", "Best mark:", str(task7(3,4,2,1,20,16,10,5,10,20,"Best")),"%", "Bad mark:", str(task7(3,4,2,1,20,16,10,5,10,20,"Bad")),"%")
print("Task 8 - probability: ", str(prob(0.4, 0.3, 0.3, 0.9, 0.95, 0.95)*100),"%")
print("Task 9 - probability: ", str(task9(0.4, 0.3, 0.3, 0.8, 0.7, 0.85)),"%")
print("Task 10 - probability: ", str(task10(0.3, 0.7, 0.9, 0.8)),"%")