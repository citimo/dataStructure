# KMP算法
# 定义一个函数，用于构建邻居表
def build_neighborhood_table(pattern):
    # 创建一个长度为pattern的列表，元素全为0
    table = [0] * len(pattern)
    # 初始化i和j，i指向pattern的第一个元素，j指向0
    i, j = 1, 0
    # 当i小于pattern的长度时，循环执行以下操作
    while i < len(pattern):
        # 如果pattern中第i个元素和第j个元素相等
        if pattern[i] == pattern[j]:
            # j指向下一个元素，table中第i个元素指向j
            j += 1
            table[i] = j
            # i指向下一个元素
            i += 1
        # 如果pattern中第i个元素和第j个元素不相等
        else:
            # 如果j不等于0，j指向table中第j-1个元素
            if j != 0:
                j = table[j - 1]
            # 如果j等于0，table中第i个元素指向0，i指向下一个元素
            else:
                table[i] = 0
                i += 1
    # 返回table
    return table

# 定义一个函数，用于KMP搜索
def kmp_search(text, pattern):
    # 调用build_neighborhood_table函数，构建邻居表
    neighborhood_table = build_neighborhood_table(pattern)
    # 初始化i和j，i指向text的第一个元素，j指向0
    i, j = 0, 0
    # 当i小于text的长度，j小于pattern的长度时，循环执行以下操作
    while i < len(text) and j < len(pattern):
        # 如果text中第i个元素和pattern中第j个元素相等
        if text[i] == pattern[j]:
            # i和j分别指向下一个元素，table中第i个元素指向j
            i += 1
            j += 1
        # 如果text中第i个元素和pattern中第j个元素不相等
        else:
            # 如果j不等于0，j指向table中第j-1个元素
            if j != 0:
                j = neighborhood_table[j - 1]
            # 如果j等于0，i指向下一个元素
            else:
                i += 1
    # 如果j等于pattern的长度，返回i-j
    if j == len(pattern):
        return i - j
    # 如果j不等于pattern的长度，返回-1
    else:
        return -1

# 定义一个字符串，用于测试KMP搜索
text = "abababab"
# 定义一个模式，用于KMP搜索
pattern = "ababab"
# 调用kmp_search函数，输出结果
print(kmp_search(text, pattern))  # 输出：0
