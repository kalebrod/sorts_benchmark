def merge_sort(array:list) -> list:
    if len(array) < 2:
        return array
    
    result = []
    mid = int(len(array) / 2)
    
    y = merge_sort(array[:mid])
    z = merge_sort(array[mid:])
    
    i = 0
    j = 0
    
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
    
        else:
            result.append(y[i])
            i += 1
    
    result += y[i:]
    result += z[j:]
    
    return result

if __name__ == '__main__':

    array = [12, 6, 13, 5, 11, 1, 7]
    print(array)
    print(merge_sort(array))