#basic insertion sort done with python
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while True:
            if array[j-1] < array[j]:
                break
            elif j > 0 and array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]            
                j = j-1
            else:
                break
    return array

#test
list_unsorted = [50, 70, 30, 2, 40, 24, 19, 60]
list_sorted = insertion_sort(list_unsorted)
print(list_sorted)
