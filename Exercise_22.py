# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в 
# порядке возрастания все те числа, которые встречаются 
# в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов 
# первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def Create_list (number) -> list:
    user_list = []
    for i in range(number):
        user_list.append(int(input(f'Input number №{i+1}:')))
    return user_list

def Create_common_set (list1, list2) -> set:
    common_list = []
    for i in range(len(list1)):
        if list1[i] in list2:
                common_list.append(list1[i])

    common_list = set(common_list)
    return common_list

user_list1 = Create_list(int(input('Input how many elements will be in your list: ')))
user_list2 = Create_list(int(input('Input how many elements will be in your list: ')))
user_common_set = Create_common_set(user_list1, user_list2)
print(sorted(user_common_set))

# использована функция sorted, поскольку во множестве показывались 
# по возрастанию сперва положительные элементы, потом по убыванию отрицательные





