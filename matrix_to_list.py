'''Matrix to list conversion using list comprehension.'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list1 = [x for i in matrix for x in i]
print(list1)
