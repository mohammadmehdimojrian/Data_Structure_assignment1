import random
import time
import copy
def insertion_sort(arr:list) -> list :
    for i in range(1,len(arr)) :
        key = arr[i]
        j=i-1
        while j>= 0 and arr[j] > key :
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

def merge_sort(arr: list) -> list :
    if len(arr) <=1 :
        return arr
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left , right)

def merge(left , right) -> list :
    # print(left , right)
    merged = []
    i=j=0
    while i<len(left) and j < len(right) :
        if left[i] < right[j] :
            merged.append(left[i]) 
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
    
def hybrid_sort(arr: list, k: int = 100) -> list:
    if len(arr) <= k:
        return insertion_sort(arr)
    else:
        mid = len(arr) // 2
        left = hybrid_sort(arr[:mid], k)
        right = hybrid_sort(arr[mid:], k)
        return merge(left, right)
    
if __name__ == '__main__' :
    print('             ////////////////InsertationSort////////////////             ')
    sample_list = [random.randint(1,300) for _ in range(120)]
    sample_list2= copy.copy(sample_list)
    sample_list3 = copy.copy(sample_list)
    print(sample_list)
    start_time_insertion = time.time()
    insertion_sort_result = insertion_sort(sample_list)
    end_time_insertion = time.time() - start_time_insertion
    print(insertion_sort_result)
    print(f'insertation_sort_time : {end_time_insertion}')
    print()
    
    print('             ////////////////MergeSort////////////////               ')
    print(sample_list2)
    start_time_merge = time.time()
    merge_sort_result = merge_sort(sample_list2)
    end_time_merge = time.time() - start_time_merge
    print(merge_sort_result)
    print(f'merge_sort_time : {end_time_merge}')
    print()
    

    print('             ////////////////HybridSort////////////////              ')
    print(sample_list3)
    start_hybrid_time = time.time()
    hybrid_sort_result = hybrid_sort(sample_list3 , 10)
    end_time_hybrid = time.time() - start_hybrid_time
    print(hybrid_sort_result)
    print(f'hybrid_sort_time : {end_time_hybrid}')




