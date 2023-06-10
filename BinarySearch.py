#Binary Search Algorithm
def define_array():
    array = []
    array_length = int(input("Defina o tamanho do array: "))
    
    for i in range(array_length):
        array_values = int(input("Digite os valores do array: "))
        array.append(array_values)
    
    return array

def quick_sort(array, start=0, end=None):
    if(end is None):
        end = len(array) - 1
    
    if(start < end):
        pivot = partition(array, start, end)
        quick_sort(array, start, pivot-1)
        quick_sort(array, pivot+1, end)
    
    return array

#QuickSort Partition
def partition(array, start, end):
    pivot = array[end]
    s = start
    for i in range(start, end):
        if(array[i] <= pivot):
            array[i], array[s] = array[s], array[i]
            s = s + 1
    
    array[s], array[end] = array[end], array[s]
    return s

#Search
def recursive_binary_search(array, value):

    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == value:
            return mid
        
        elif array[mid] > value:
            right = mid - 1

        else: # A[meio] < item
            left = mid + 1
    return -1

def search():
    array = quick_sort(define_array())
    value = int(input("Digite um valor para a pesquisa: "))
    print((recursive_binary_search(array, value)))

search()
