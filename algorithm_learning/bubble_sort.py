# _*_coding:utf-8_*_

import random
from cal_time import cal_time

@cal_time
def bubble_sort1(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        # print(li)
        if not exchange:
            return

@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


if __name__ == '__main__':
    li = list(range(10000))
    random.shuffle(li)
    bubble_sort1(li)


