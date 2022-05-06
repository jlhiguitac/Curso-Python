my_set = {1, 2, 3}
print(my_set)

my_set.add(4)
print(my_set)

my_set.update([1, 2, 5])
print(my_set)

my_set.update((1, 7, 2), {6, 8})
print(my_set)

my_set.add("Holi")
print(my_set)

my_set.update([11, 12])
print(my_set)

my_set.add(9)
print(my_set)

my_set.discard(6)
print(my_set)

my_set.pop()
print(my_set)

my_set.pop()
print(my_set)

my_set2 = {1, 2, 3, 14, 15, "Holi"}
print(my_set2)

my_set3 = my_set | my_set2
print(my_set3)

my_set4 = my_set & my_set2
print(my_set4)

my_set5 = my_set - my_set2
print(my_set5)

my_set6 = my_set2 - my_set
print(my_set6)

my_set7 = my_set ^ my_set2
print(my_set7)





