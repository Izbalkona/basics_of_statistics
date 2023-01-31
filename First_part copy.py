import math



# находим среднее значение
def find_average(x):
    return sum(x) / len(x)


# находим размах
def find_range(x):
    x_copy = sorted(x)
    return abs(x_copy[-1] - x_copy[0])

# находим медиану
def find_median(x):
    if len(x) % 2 == 0:
        return (x[len(x) // 2] + x[len(x) // 2 -1]) / 2
    else:
        return x[len(x) // 2]


# находим дисперсию в генеральной совокупности
def find_general_variance(x, x_average):
    variance = 0
    for i in x:
        variance += (i - x_average) ** 2
    return variance / len(x)


# находим дисперсию в выборке
def find_subgeneral_variance(x, x_average):
    variance = 0
    for i in x:
        variance += (i - x_average) ** 2
    return variance / (len(x) - 1)


# возвращаем квадрат из числа
def get_sqrt(x):
    return x ** 0.5

x = input('enter_selction: ')

x = x.split()

for index in range(len(x)): #преобразуем эементы списка в int
    try:
        x[index] = int(x[index])
    except ValueError:
        print("not a number") 
print(get_sqrt(find_subgeneral_variance(x, find_average(x))))

print(x)

