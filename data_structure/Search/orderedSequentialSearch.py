# 有序列表的顺序搜索
def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    
    return found

if __name__ == '__main__':
    print(orderedSequentialSearch([1, 2, 3, 4], 3))