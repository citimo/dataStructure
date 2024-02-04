# 冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# 使用元组解包进行交换
def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

# 短路冒泡排序
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum = passnum - 1

if __name__ == '__main__':
    mylist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(mylist)
    print(mylist)
    mylist_1 = [17, 20, 26, 44, 31]
    shortBubbleSort(mylist_1)
    print(mylist_1)
