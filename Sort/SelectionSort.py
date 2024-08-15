
# Simple sorting algorithm
# Quadratic runnig time O(n^2)

def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        for j in range(i+1, len(arr)):
            if arr[cur_index] > arr[j]:
                cur_index = j
        arr[cur_index], arr[i] = arr[i], arr[cur_index]


arr = [2,6,5,1,3,4]
selectionSort(arr)
print(arr)