# 选择排序
# def SelectionSort(l):
#     for i in range(0, len(l) - 1):
#         minIndex = i
#         for j in range(i + 1, len(l)):    
#             if l[j] < l[minIndex]:
#                 minIndex = j
#         if (minIndex != i):
#             temp = l[minIndex]
#             l[minIndex] = l[i]
#             l[i] = temp

def SelectionSort(l):
    length = len(l)
    i = len(l) - 1
    while i > 0:
        maxIndex = 0
        for j in range(1, length):
            if l[j] > l[maxIndex]:
                maxIndex = j
        if (maxIndex != i):
            temp = l[maxIndex]
            l[maxIndex] = l[i]
            l[i] = temp
        length = length - 1
        i = i - 1

if __name__ == '__main__':
    l = [5, 0, 12, 66, -15, 3, 9, -1, 100, 0, 1, 3, 2, 1, 6, 5, 4, 3, 2, 1]
    print(l)
    SelectionSort(l)
    print(l)