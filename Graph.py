import matplotlib.pyplot as plt
import numpy as np

def read(fileName):
    f = open(fileName)
    caloriesPerDay = {}
    for line in f:
        data = line.split(":")
        day = int(data[0])
        calories = float(data[1])
        if day not in caloriesPerDay.keys():
            caloriesPerDay[day] = 0
        caloriesPerDay[day] += calories
    return(caloriesPerDay)

def graph(d):
    days = []
    calories = []
    for k,v in d.items():
        days.append(k)
        calories.append(v)
    newDays = [days[x] - days[0] + 1 for x in range(len(days))]
    plt.scatter(newDays, calories)
    plt.title("Calories per Day")
    plt.plot(newDays, calories)
    plt.xlim([0, len(days) + 1])
    plt.ylim([0, max(calories) + 100])
    plt.xticks(np.arange(0, len(days) + 1, 1))
    plt.yticks(np.arange(0, max(calories) + 100, 100))
    plt.show()


