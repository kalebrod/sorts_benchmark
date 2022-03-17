def partition(array:list,low:int,high:int) -> int:
    i = ( low - 1 )
    x = array[high]
 
    for j in range(low , high):
        if   array[j] <= x:
 
            i = i+1
            array[i],array[j] = array[j],array[i]
 
    array[i+1],array[high] = array[high],array[i+1]
    
    return (i+1)
 

def quick_sort(array:list,low:int,high:int) -> list:
 
    #  auxiliary stack
    size = high - low + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
 
        # sorted array
        p = partition( array, low, high )

        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

if __name__ == '__main__':
    array = [12, 6, 13, 5, 11, 1, 7]
    
    print(array)
    quick_sort(array, 0, len(array)-1)
    print(array)