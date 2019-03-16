# import this

new_string = "Hello"
print(id(new_string))
new_string = "Shashi"
print(new_string)

num = 123
print(type(num))
print(num)

print(bin(2))

print(oct(2))

cnum = 3 + 4j
print(type(cnum))
print(cnum)

# List example
list1 = [1, 2, 3, 4]
list2 = [1, 'drink', 10, 'sandwiches', 3 + 4j]
list3 = [1, 2, 3, [4, 5, 6], ['Hello', 'Python']]
print(list3)

list1[1] = 45
print(list1)

sublist = list2[2:4]
print(sublist)

numbers = range(10)
print(*numbers)

print(*numbers[::2])

# Set Example
set1 = {1, 1, 3, 4, 4, 7, 8}
print(set1)

list2 = (1, 2, 1, 2, 3, 4, 5)
set2 = set(list2)
print(set2)

print(set1 - set2)  # difference
print(set1 | set2)  # union
print(set1 & set2)  # intersection
print(set1 ^ set2)  # union - intersection

# Dictionaries

student1 = {1: 'Shashi', 2: 'Lalsa', 3: 'Kumar'}
print(student1)

print(student1.get(1))
print(student1[1])
student1[1] = 'Lalsa'
student1[len(student1)] = 'Kumari'
print(student1)
print(student1.keys())
print(student1.values())

d2 = dict({'orange': 5, 'apple': 17})

student1.update(d2)
print(student1)

# Tuples
tp = ([1, 2, 3, 4], ['one', 'two', 'three', 'four'])
l1, l2 = tp
print(l1)
print(l2)


