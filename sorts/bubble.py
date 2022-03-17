def bubble_sort(array):
    n = len(array)

    for i in range(n-1):

        for j in range(0, n-i-1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

if __name__ == '__main__':    
    array = [12, 6, 13, 5, 11, 1, 7]
    
    print(array)
    bubble_sort(array)
    print(array)