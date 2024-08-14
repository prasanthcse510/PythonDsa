
def insertion_sort(listArr):
    for i in range(1, len(listArr)):
        j = i
        while listArr[j - 1] > listArr[j] and j > 0:
            listArr[j - 1], listArr[j] = listArr[j], listArr[j - 1]
            j -= 1


# There are two parts, left side is sorted and right side is unsorted
listArr = [2,6,5,1,3,4]
insertion_sort(listArr)
print(listArr)