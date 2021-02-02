#!/usr/bin/env python

import treelib
import treelib.exceptions

ingredients_to_place = ['a', 'b' ,'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

tree = treelib.Tree()
tree.create_node('root', 'root')
passes = 3

for idx in range(1, passes + 1):
  for i in ingredients_to_place:
    try:
      tree.create_node(i, i, parent='root')
      ingredients_to_place.remove(i)
      print(i)
    except treelib.exceptions.NodeIDAbsentError:
      print("ERROR %s" % i)

  if len(ingredients_to_place) == 0:
      print("All done after pass %i" % idx)
      break

print(len(tree.all_nodes()))
print(len(ingredients_to_place))
print(ingredients_to_place)
