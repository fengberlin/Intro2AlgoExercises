# 归并排序

def Merge(l, temp, left, mid, right):
    start = left
    leftEnd = mid - 1
    num = right - left + 1
    while ((left <= leftEnd) and (mid <= right)):
        if l[left] <= l[mid]:
            temp.append(l[left])
            start += 1
            left += 1
        else:
            temp.append(l[mid])
            start += 1
            mid += 1
    while left <= leftEnd:
        temp.append(l[left])
        start += 1
        left += 1
    while mid <= right:
        temp.append(l[mid])
        start += 1
        mid += 1
    for i in range(0, num):
        l[right] = temp[right]
        i += 1
        right -= 1

def MSort(l, temp, left, right):
    if left < right:
        mid = int((right - left) >> 1 + left)
        MSort(l, temp, left, mid)
        MSort(l, temp, mid + 1, right)
        Merge(l, temp, left, mid + 1, right)

def MergeSort(l):
    temp = []
    MSort(l, temp, 0, len(l) - 1) 

if __name__ == '__main__':
    l = [8,2,6,-1,7,1,6,5,9,2,0,3,63,15,24]
    MergeSort(l)
    print(l)

