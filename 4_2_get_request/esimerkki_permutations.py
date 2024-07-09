import itertools

list1 = [1, 5, 8]
list2 = [2, 9, 25]
permut = itertools.permutations(list1, len(list2))
unique_combinations = []
for comb in permut:
    zipped = zip(comb, list2)
    unique_combinations.append(list(zipped))
print(unique_combinations)

