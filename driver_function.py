""""Driver function to run other modules"""
'''
from is_coprime import is_coprime

print(is_coprime(2,12))
'''

from sorting_key import sort_priority

values = [3, 1, 2, 10, 5, 15, 20, 8]
group = [5, 2, 20]
sort_priority(values, group)
print(values)

