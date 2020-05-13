"""
python实战练习2
课后作业1
冒泡排序每一行加注释说明
"""

# 冒泡排序第一种写法
# 定义一个列表
list1 = [11, 9, 8, 10, 4, 50, 28]
# 循环列表的排序次数
# 索引i从0开始，所以for循环的次数等于列表长度减1
for i in range(len(list1) - 1):
    print("这是第{}次排序".format(i))
    # j索引从0开始，列表每排序一次，就对比（列表长度-列表当前循环次数-1）次
    for j in range(len(list1)-i-1):
        print("这是第{}对比".format(j))
        # 如果前面一位数大于后一位数，进行位置调换
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
# 打印排序后的列表
print(list1)


# 冒泡排序第二种写法
# 定义一个列表
list_sort = [2, 3, 1, 6, 5, 8]
# 循环列表排序次数
# 定义i的索引从1开始，所以for循环的长度等于列表长度
for i in range(1, len(list_sort)):
    print("这是第{}次排序".format(i))
    # 循环当前对比次数
    # 索引j从0开始，循环的次数等于列表长度-列表当前循环次数
    for j in range(len(list_sort) - i):
        print("这是第{}次对比".format(j))
        # 如果列表中第一个数大于第二位数时，进行位置对换
        if list_sort[j] > list_sort[j + 1]:
            list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]
# 打印列表排序后的结果
print(list_sort)
