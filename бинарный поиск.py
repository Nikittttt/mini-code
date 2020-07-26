import random
from time import time

# список времени для дальнейшей статистики
list_time = []

# класс который и создаёт список, непредвзято выбирает число и сообщает больше или меньше
class randNum:
    def __init__(self):
        self.len_list = 2**25
        print("Начинаю создавать список")
        self.rand_list = list(range(0,self.len_list,3))
        print("Создание окончено")
        self.rand_num = random.choice(self.rand_list)
        print("\nВыбрано число -", self.rand_num)
    def num_sel(self, num):
        if num < self.rand_num:
            return ">"
        elif num > self.rand_num:
            return "<"
        elif num == self.rand_num:
            return "="

# сам бинарный поиск с записью времени и выводом сколько времени работал
for i in range(1, 10**3):
    start = time()
    rand_num = randNum()
    all_list = rand_num.rand_list
    ind = (len(all_list)-1)//2
    ser_ind = ind
    this_num = all_list[ind]
    answer = rand_num.num_sel(this_num)
    count_itr = 1
    while answer != "=":
        if answer == ">":
            all_list = all_list[ind+1::]
            ind = (len(all_list)-1)//2
            ser_ind +=ind
        elif answer == "<":
            all_list = all_list[:ind:]
            ind = (len(all_list)-1)//2
            ser_ind -= ind
        this_num = all_list[ind]
        answer = rand_num.num_sel(this_num)
        count_itr += 1
    end = time()
    print(f"{i}. Я угадал, это было число под индексом {ser_ind}, я угадал это за {count_itr} попыток и за {end-start:.5f} секунд\n\n")
    list_time.append(end-start)

print(f"Среднее време выполнения: {sum(list_time)/len(list_time):.5f} секунд.\n"
      f"Максимально време выполнения: {max(list_time):.5f} секунд.\n"
      f"Минимальное време выполнения: {min(list_time):.5f} секунд.\n"
      f"Проведено {len(list_time)} опытов за {sum(list_time):.5f} секунд.")
