# _*_coding:utf-8_*_

from cal_time import cal_time

@cal_time
def linear_search(li, val):
    for index, v in enumerate(li):
        if v == val:
            return index
    return None

@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:  # li[val] < val
            left = mid + 1
    return None


if __name__ == '__main__':
    li = list(range(100000000))
    print(linear_search(li, 38900000))
    print(binary_search(li, 38900000))



