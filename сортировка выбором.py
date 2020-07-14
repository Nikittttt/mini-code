import random
old_list = list(range(1, 92, 3))
random.shuffle(old_list)

def sorter(old_list):
    new_list = []
    for _ in range(len(old_list)):
        mn = 0
        for i in range(1,len(old_list)):
            if old_list[mn]>=old_list[i]:
                mn = i
        new_list.append(old_list.pop(mn))
    return new_list

print(f"Было - {old_list}\n\nСтало - {sorter(old_list)}")
