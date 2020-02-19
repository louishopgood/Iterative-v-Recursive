def find_min_iterative(my_list):
    min = None
    for element in my_list:
        if not min or (element < min):
            min = element
    return min

print(find_min_iterative([42, 17, 2, -1, 67]))
# -1
#rint(find_min_iterative([]))
# None
print(find_min_iterative([13, 72, 19, 5, 86]))
# 5

def find_min_recursive(my_list, min=None):
  if len(my_list) == 0:
    return min
  if min is None or my_list[0] < min:
    min = my_list[0]
    return find_min_recursive(my_list[1:], min)
  return find_min_recursive(my_list[1:], min)

# test cases
print(find_min_recursive([42, 17, 2, -1, 67]) )
print(find_min_recursive([]))
print(find_min_recursive([13, 72, 19, 5, 86]))
