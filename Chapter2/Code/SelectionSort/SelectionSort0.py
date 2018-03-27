# 选择排序算法
# 稳定性: 不稳定 
# 时间复杂度: О(n^2)
# 最优时间复杂度: О(n^2)
# 平均时间复杂度: О(n^2)
# 空间复杂度: О(n) total

def MaxIndex(l, length):
    maxIndex = 0
    for i in range(1, length):
        if l[i] > l[maxIndex]:
            maxIndex = i
    return maxIndex

def SelectionSort(l):
    length = len(l)
    for i in range(len(l) - 1):
        index = MaxIndex(l, length)
        if (index != length - 1):
            temp = l[length - 1]
            l[length - 1] = l[index]
            l[index] = temp
        length = length - 1

if __name__ == '__main__':
    l = [5, 2, 6, 0, 9, -8]
    print(MaxIndex(l, len(l)))
    print(l)
    SelectionSort(l)
    print(l)