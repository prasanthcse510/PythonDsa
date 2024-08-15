# divide and conquer algorithm
# Breaks problem into multiple subproblems recursively until they become simple to solve
# solutions are combined to solve original problem
#  O(n * log(n)) running time -> optimal running time for comparison based algorithm

# 1) Split an array in half. 
# 2) Call merge sort on each half to sort them recursively. 
# 3) Merge both sorted halves into one sorted array

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # recursion
        mergeSort(left_arr)
        mergeSort(right_arr)

        # merge
        i = 0   # left_arr index
        j = 0   # right_arr index
        k = 0   # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):    # for missing elements from left array
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):   # for missing elements from right array
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr = [2,6,5,1,7,4,3]
mergeSort(arr)
print(arr)