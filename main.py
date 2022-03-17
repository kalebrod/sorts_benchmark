import json
from time import time
from random import sample

from sorts import bubble, quick, insertion, selection, merge

methods = {
    'bubble':bubble.bubble_sort,
    'quick':quick.quick_sort,
    'insertion':insertion.insertion_sort,
    'selection':selection.selection_sort,
    'merge': merge.merge_sort
}

def run_method(method:str, array:list)->float:
    print(method,end=' ')
    start = time()
    
    if method == 'quick':
        methods[method](array,0,len(array)-1)
    else:    
        methods[method](array)
    
    end = time() - start
    print(end)
    
    return end

number_pool = range(1000000)

v1 = sample(number_pool,1000)
v2 = sample(number_pool,10000)
v3 = sample(number_pool,100000)

v1_up = sorted(v1.copy())
v2_up = sorted(v2.copy())
v3_up = sorted(v3.copy())

v1_down = sorted(v1.copy(),reverse=True)
v2_down = sorted(v2.copy(),reverse=True)
v3_down = sorted(v3.copy(),reverse=True)

times = {}
times['random'] = {}
times['ascending'] = {}
times['descending'] = {}

# Random array

# For 1.000 elements
print('Running 1.000')

times['random']['bubble'] = [run_method('bubble',v1.copy())]
times['random']['quick'] = [run_method('quick',v1.copy())]
times['random']['insertion'] = [run_method('insertion',v1.copy())]
times['random']['selection'] = [run_method('selection',v1.copy())]
times['random']['merge'] = [run_method('merge',v1.copy())]

# For 10.000 elements
print('Running 10.000')

times['random']['bubble'].append(run_method('bubble',v2.copy()))
times['random']['quick'].append(run_method('quick',v2.copy()))
times['random']['insertion'].append(run_method('insertion',v2.copy()))
times['random']['selection'].append(run_method('selection',v2.copy()))
times['random']['merge'].append(run_method('merge',v2.copy()))

# For 100.000 elements
print('Running 100.000')

times['random']['bubble'].append(run_method('bubble',v3.copy()))
times['random']['quick'].append(run_method('quick',v3.copy()))
times['random']['insertion'].append(run_method('insertion',v3.copy()))
times['random']['selection'].append(run_method('selection',v3.copy()))
times['random']['merge'].append(run_method('merge',v3.copy()))

# Array sorted in ascending order

# For 1.000 elements
print('Running 1.000')

times['ascending']['bubble'] = [run_method('bubble',v1_up.copy())]
times['ascending']['quick'] = [run_method('quick',v1_up.copy())]
times['ascending']['insertion'] = [run_method('insertion',v1_up.copy())]
times['ascending']['selection'] = [run_method('selection',v1_up.copy())]
times['ascending']['merge'] = [run_method('merge',v1_up.copy())]

# For 10.000 elements
print('Running 10.000')

times['ascending']['bubble'].append(run_method('bubble',v2_up.copy()))
times['ascending']['quick'].append(run_method('quick',v2_up.copy()))
times['ascending']['insertion'].append(run_method('insertion',v2_up.copy()))
times['ascending']['selection'].append(run_method('selection',v2_up.copy()))
times['ascending']['merge'].append(run_method('merge',v2_up.copy()))

# For 100.000 elements
print('Running 100.000')

times['ascending']['bubble'].append(run_method('bubble',v3_up.copy()))
times['ascending']['quick'].append(run_method('quick',v3_up.copy()))
times['ascending']['insertion'].append(run_method('insertion',v3_up.copy()))
times['ascending']['selection'].append(run_method('selection',v3_up.copy()))
times['ascending']['merge'].append(run_method('merge',v3_up.copy()))

# Array sorted in descending order

# For 1.000 elements
print('Running 1.000')

times['descending']['bubble'] = [run_method('bubble',v1_down.copy())]
times['descending']['quick'] = [run_method('quick',v1_down.copy())]
times['descending']['insertion'] = [run_method('insertion',v1_down.copy())]
times['descending']['selection'] = [run_method('selection',v1_down.copy())]
times['descending']['merge'] = [run_method('merge',v1_down.copy())]

# For 10.000 elements
print('Running 10.000')

times['descending']['bubble'].append(run_method('bubble',v2_down.copy()))
times['descending']['quick'].append(run_method('quick',v2_down.copy()))
times['descending']['insertion'].append(run_method('insertion',v2_down.copy()))
times['descending']['selection'].append(run_method('selection',v2_down.copy()))
times['descending']['merge'].append(run_method('merge',v2_down.copy()))

# For 100.000 elements
print('Running 100.000')

times['descending']['bubble'].append(run_method('bubble',v3_down.copy()))
times['descending']['quick'].append(run_method('quick',v3_down.copy()))
times['descending']['insertion'].append(run_method('insertion',v3_down.copy()))
times['descending']['selection'].append(run_method('selection',v3_down.copy()))
times['descending']['merge'].append(run_method('merge',v3_down.copy()))

times['arrays'] = {
    'v1':v1,
    'v2':v2,
    'v3':v3
}

with open("times.json","w") as file:
    json.dump(times,file,indent=5)
