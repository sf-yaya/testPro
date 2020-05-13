class BubbleSort():
    def bubble_sort(self, list1):
        # 排序次数
        for i in range(len(list1) - 1):
            print("这是第{}次排序".format(i))
            # 对比次数
            for j in range(len(list1) - i - 1):

                print("这是第{}对比".format(j))

                # 如果前面一位数大于后一位数，进行位置调换
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]

bs = BubbleSort()
list1 = [11, 9, 8, 10, 4, 50, 28]
bs.bubble_sort(list1)
# print(list1)
