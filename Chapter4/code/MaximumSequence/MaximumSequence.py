def Find_Maximum_Subarray_Linear(arr, low, high):
    max_sum = -1e100
    max_left, max_right = -1, -1
    sum = 0
    last_left = 0
    for i in range(low, high):
        sum += arr[i]
        if sum > max_sum:
            max_sum = sum
            max_left =  last_left
            max_right = i
        if sum < 0:
            sum = 0
            last_left = i + 1
    return max_left, max_right, max_sum

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, -3]
    left, right, sum = Find_Maximum_Subarray_Linear(l, 0, len(l))
    print(left, right, sum)