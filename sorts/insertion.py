def insertion_sort(array:list) -> list:
  
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        
        while j >=0 and key < array[j] :
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = key

    return array

if __name__ == '__main__':
    array = [12, 6, 13, 5, 11, 1, 7]

    print(array)
    insertion_sort(array)
    print(array)
