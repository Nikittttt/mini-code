import time
import random
from random import randint
 
lists = list(range(1,1_000_002))
random.shuffle(lists)
 
def fast_sort(list_to_sort):
    if len(list_to_sort)<=1:
        return list_to_sort
    else:
        rand_num = list_to_sort.pop(randint(0, len(list_to_sort)-1))
        list_low = []
        list_high = []
        for i in list_to_sort:
            if i <= rand_num:
                list_low.append(i)
            else:
                list_high.append(i)
        return fast_sort(list_low)+[rand_num]+fast_sort(list_high)
 
start = time.time()
sorted_list = fast_sort(lists)
stop = time.time()
print(stop-start,'секунд ушло на сортировку')
