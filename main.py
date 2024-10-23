import random
from time import time
from sorts import hybrid_sort , merge_sort , insertion_sort
import copy

n = random.randint(2000,17000)
print(f'arry len is {n}')
arrys = [random.randint(1,2*n) for _ in range(n)]
arrys2 = copy.copy(arrys)
arrys3 = copy.copy(arrys)

# print('             InsertionSort              ')
# print(arrys)
insertation_sort_start = time()
insertion_sort_result = insertion_sort(arrys)
end_time_insertion_sort = time() - insertation_sort_start
print(f'Insertion Sort Time : {end_time_insertion_sort}')
print()

# print('             MergeSort              ')
# print(arrys2)
merge_sort_start = time()
merge_sort_result = merge_sort(arrys2)
end_time_merge_sort = time() - merge_sort_start
print(f'Merge Sort Time : {end_time_merge_sort}')
print()

# print('             HybridSort              ')
# print(arrys3)
hybrid_sort_start = time()
hybrid_sort_result = hybrid_sort(arrys3)
end_time_hybrid_sort = time() - hybrid_sort_start
print(f'Hybrid Sort Time : {end_time_hybrid_sort}')
assert merge_sort_result== hybrid_sort_result==insertion_sort_result



