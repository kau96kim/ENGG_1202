from sortballs import *
frontier = [{'path': ['PULL'], 'state': (1, 0, 5, 4, 3, 2)}, 
{'path': ['FLIP', 'PULL'], 'state': (2, 0, 3, 4, 5, 1)}, 
{'path': ['FLIP', 'FLIP'], 'state': (0, 1, 5, 4, 3, 2)}]
print("Before getNext:")
for f in frontier:
  print(f)
item = getNext(frontier)
print("getNext: ", item)
print("After getNext:")
for f in frontier:
  print(f)