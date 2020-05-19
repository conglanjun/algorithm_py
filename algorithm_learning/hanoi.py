# _*_coding:utf-8_*_


"""
target is move n plates from a to c with b
step 1:
    move n-1 plates from a to b with c
step 2:
    move 1 plate from a to c
step 3:
    move n-1 plates from b to c with a

"""
count = 0
def hanoi(n, a, b, c):
    global count
    if n > 0:
        hanoi(n-1, a, c, b)
        count += 1
        print("%d moving from %s to %s" % (count, a, c))
        hanoi(n-1, b, a, c)


if __name__ == '__main__':
    hanoi(4, 'A', 'B', 'C')



