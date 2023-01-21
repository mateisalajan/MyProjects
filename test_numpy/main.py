import numpy as numpy

lst = numpy.array([4, 3, 2])

lst2 = lst[lst > numpy.percentile(lst, 30)]
print(lst2)

# lst = [2, 7, 3, 9, 1, 5]
# dict_nou = {}
# i = 0
# for x in lst:
#     dict_nou[i] = x
#     i += 1
# lst2 = sorted(dict_nou.keys(), reverse=True)
# print(lst2)

