import math

random_selection_list=(4, 4, 5, 7, 9, 16, 15, 100)

input_selection = input('enter_selction: ')

input_selection_list = input_selection.split()

for index in range(len(input_selection_list)): #преобразуем эементы списка в int
    try:
        input_selection_list[index] = int(input_selection_list[index])
    except ValueError:
        print("not a number") 
print(input_selection_list)

print(input_selection_list)
sum = sum(input_selection_list)
print("sum = " + str(sum))
average = sum/len(input_selection_list)
print("average = " + str(average))
#variance(дисперсия) ниже
proverty_average = 0
proverty_average_2 = 0

for i in input_selection_list:
    proverty_average += i - average#третье свойство средне арифмитического
    proverty_average_2 += (i - average) ** 2

variance = proverty_average_2 / (len(input_selection_list) - 1)##variance(дисперсия)
print(len(input_selection_list))
sigma = math.sqrt(variance) #средне квадратичное отклонение
print("proverty_average = " + str(proverty_average))
print("variance = " + str(variance))
print("sigma = " + str(sigma))

#for i in random_selection()
    