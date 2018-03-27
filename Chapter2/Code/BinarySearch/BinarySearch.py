# 二分查找

# 非递归
# def BinarySearch(l, key):
#     left = 0
#     right = len(l) - 1
#     while left <= right:
#         mid = int((right - left) >> 1 + left)
#         if l[mid] > key:
#             right = mid -1
#         elif l[mid] < key:
#             left = mid + 1
#         else:
#             return mid
#     return None

# 递归
def BinarySearch(l, left, right, key):
    if left <= right:
        mid = int((right - left) >> 1 + left)    # 不使用(left + right) / 2，因为当left和right很大时会溢出
        if l[mid] == key:
            return mid
        elif l[mid] > key:
            return BinarySearch(l, left, mid - 1, key)
        else:
            return BinarySearch(l, mid + 1, right, key)
    else:
        return None

if __name__ == '__main__':   
    l = [1, 3, 5, 7, 9]
    print(BinarySearch(l, 0, len(l) - 1, -1))