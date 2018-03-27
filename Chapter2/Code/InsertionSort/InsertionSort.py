# 插入排序
def InsertionSort(l):
    for j in range(1, len(l)):
        key = l[j]
        i = j - 1
        while i >= 0 and l[i] < key:
            l[i + 1] = l[i]
            i = i - 1
        l[i + 1] = key

if __name__ == '__main__':
    l = [5, 2, 4, 6, 1, 3, 1, 5, 3]
    print(l)
    InsertionSort(l)
    print(l)