# 简单的模式匹配器
def simpleMatcher(pattern, text):
    starti = 0  # 记录每次尝试的起点
    i = 0  # 文本的下标
    j = 0  # 模式的下标
    match = False
    stop = False
    while not match and not stop:
        if text[i] == pattern[j]:
            i = i + 1
            j = j + 1
        else:
            starti = starti + 1  # 向右移动
            i = starti
            j = 0

        if j == len(pattern):
            match = True
        else:
            if i == len(text):
                stop = True

    if match:
        return i - j
    else:
        return -1
