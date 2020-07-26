from time import time
from random import randint, shuffle

# создаём и перемешиваем список
lists = list(range(1,2**25))
shuffle(lists)
 
# алгоритм быстрой сортировки
def fast_sort(list_to_sort):
    # случай когда не надо ничего сортировать
    if len(list_to_sort) <= 1:
        return list_to_sort
    # случай сортировки
    else:
        # выбираем случайное число из списка(можно заменить на первое число или центральное)
        rand_num = list_to_sort.pop(randint(0, len(list_to_sort)-1))
        # разбиваем список на числа которые меньше и больше выбранного числа
        list_low = []
        list_high = []
        for i in list_to_sort:
            if i <= rand_num:
                list_low.append(i)
            else:
                list_high.append(i)
        # возвращаем соединённые списки(рекурсивно вызывая сортировку чисел которые меньше и больше)
        return fast_sort(list_low)+[rand_num]+fast_sort(list_high)

# сколько времени ушло на сортировку
start = time()
sorted_list = fast_sort(lists)
stop = time()
print(f'{stop-start:.5f} секунд ушло на сортировку')
