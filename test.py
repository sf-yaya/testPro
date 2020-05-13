list_sort = [2, 3, 1, 6, 5, 8]
# 排序次数
for i in range(1, len(list_sort)):
    # 对比次数
    for j in range(len(list_sort) - i):
        if list_sort[j] > list_sort[j + 1]:
            list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]
print(list_sort)
