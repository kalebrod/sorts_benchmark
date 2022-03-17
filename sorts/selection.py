def selection_sort(array:list) -> list:
    for i in range(len(array)):
        min_idx = i
        
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
                
        array[i], array[min_idx] = array[min_idx], array[i]

    return array

if __name__ == '__main__':
    array = [12, 6, 13, 5, 11, 1, 7]

    print(array)
    selection_sort(array)
    print(array)
  