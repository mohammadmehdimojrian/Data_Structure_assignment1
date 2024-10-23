import random
from time import time
from sorts import hybrid_sort , merge_sort , insertion_sort

n = random.randint(100,15000)
print(f'arry len is {n}')
arrys = [random.randint(1,2*n) for _ in range(n)]

# print('             InsertionSort              ')
insertation_sort_start = time()
insertion_sort_result = insertion_sort(arrys)
end_time_insertion_sort = time() - insertation_sort_start
print(f'Insertion Sort Time : {end_time_insertion_sort}')
print()

# print('             MergeSort              ')
merge_sort_start = time()
merge_sort_result = merge_sort(arrys)
end_time_merge_sort = time() - merge_sort_start
print(f'Merge Sort Time : {end_time_merge_sort}')
print()

# print('             HybridSort              ')
hybrid_sort_start = time()
hybrid_sort_result = hybrid_sort(arrys)
end_time_hybrid_sort = time() - hybrid_sort_start
print(f'Hybrid Sort Time : {end_time_hybrid_sort}')
print()



