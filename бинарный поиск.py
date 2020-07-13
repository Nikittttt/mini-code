import random
from time import time

list_time = []

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

for _ in range(10**3):
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
            ser_ind -=ind
        this_num = all_list[ind]
        answer = rand_num.num_sel(this_num)
        count_itr += 1
    print(f"Я угадал, это было число под индексом {ser_ind}, я угадал это за {count_itr} попыток и за {time()-start} секунд\n\n")
    list_time.append(time()-start)

print(f"Среднее време выполнения: {sum(list_time)/len(list_time)} секунд")
