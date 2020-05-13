"""
作业4
使用列表推导式写下面这个算法题
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
"""

# 列表推导式一
list1 = [-4,20,0,6,10]
list2 = [list1[i] ** 2 for i in range(len(list1))]
# 对列表进行排序
list2.sort()
# 打印排序后的列表值
print(list2)

# 列表推导式二
list3 = [5,-3,2,3,11]
list4 = [list3[j]**2 for j in range(len(list3))]
# # 对列表进行排序
list4.sort()
# 打印排序后的列表值
print(list4)




# list1 = [-4,-1,0,3,10]
# list2=[]
# for i in range(len(list1)):
#          list2.append(list1[i]**2)
#          list2.sort()
#
#
# print(list2)



