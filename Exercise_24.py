# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном списке урожайности грядки.

# Пример: 
# 4 -> 1 2 3 4
# 9

def Bush_and_berries_number () -> list:
    bushes_number = int(input('Input the number of bushes of berries: '))
    while bushes_number < 3:
        bushes_number = int(input('There must be at least 3 bushes. Try again: '))
    berries_on_a_bush = []
    for i in range(bushes_number):
        berries_number = int(input(f'How many berries are there on a bush {i+1}? Input a number: '))
        while berries_number < 0:
            berries_number = int(input(f'There must be at least 0 berries. Input again: '))
        berries_on_a_bush.append(berries_number)
    return berries_on_a_bush

def Counting_summs (list) -> list:
    summ = 0
    summ_list = []
    for i in range(len(list)):
        summ = list[i-2] + list [i-1] + list[i]
        summ_list.append(summ)
    return summ_list

def Counting_max_berries (list_2) -> int:
    list_2 = sorted(set(list_2))
    print(f"Max number of berries to collect: {list_2[-1]}")

possible_summs_of_berries = Counting_summs(Bush_and_berries_number())
Counting_max_berries(possible_summs_of_berries)