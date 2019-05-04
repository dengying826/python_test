# 冒泡排序
list1 = [4, 13, 5, 8, 6, 10, 11, 2, 3, 7, 12, 14, 1]
for i in range(len(list1) - 1):
    for j in range(len(list1) - i - 1):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
        print('%d %d' % (i, j) + str(list1))
print(list1)
