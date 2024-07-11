set1 = {1,5,6,7,9}
for i in set1:
    print(i)

set2 = {1,}    
set2.add(9)
set2.add(7)
print(set2)

set2.remove(1)
print(set2)

set3 = {1,3,8,9}
intersection = set1.intersection(set3)
print(intersection)

union = set1.union(set3)
print(union)

difference = set1.difference(set3)
print(difference)