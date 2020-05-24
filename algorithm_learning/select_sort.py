# _*_coding:utf-8_*_


def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def select_sort(li):
    for i in range(len(li) - 1):
        min_local = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_local]:
                min_local = j
        if min_local != i:
            li[i], li[min_local] = li[min_local], li[i]


li = [3, 2, 4, 1, 5, 6, 7, 8, 9]
select_sort(li)
print(li)
