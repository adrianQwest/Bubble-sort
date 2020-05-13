from numpy import random

size_list = 7 #change this number to get a bigger or smaller list
list_to_sort = [random.randint(1, 11) for _ in range(size_list)]
print('starting with:')
print(list_to_sort)
for j in range(size_list-1):
  print()
  print('>>>pass {}'.format(j+1))
  print(list_to_sort)
  for i in range(size_list-j-1):
    a = list_to_sort[i]
    b = list_to_sort[i+1]
    if a > b: #if a is bigger than b swap them over
      list_to_sort[i] = b
      list_to_sort[i+1] = a
      print('elements {2}: swapped {0} > {1}'.format(a,b,(i,i+1)))
    else: print('elements {2}: no swap: {0} <= {1}'.format(a, b,(i,i+1)))
    print(list_to_sort)
  print('biggest {0} now in sorted order: {1}'.format(k:=j+1, list_to_sort[-k:]))
print('all sorted')
print(list_to_sort)
print('the biggest numbers have bubbled to the end one at a time')
