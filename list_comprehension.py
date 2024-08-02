# # #generating squares of given list

# # numbers = [3,4,5,2,1,6]

# # l= [x**2 for x in numbers ]

# # print(l)


# # # filter out the even numbers from a given list of integers.
# # even = [y for y in numbers if y%2 ==0]
# # print(even)

# # #How can you use a list comprehension to create a list of tuples where each tuple contains
# # #  a number and its square from a given list?

# # square = [(num, num**2) for num in numbers]
# # print(square)

# # #Given a list of strings, write a list comprehension to create a new list with the lengths of each string.

# # s = ['aaa','dddd','rrrrr']
# # new_list = [len(l) for l in s ]

# # print(new_list)

# # #How would you use a list comprehension to flatten a list of lists 
# # # (e.g., [[1, 2, 3], [4, 5, 6]] to [1, 2, 3, 4, 5, 6])?
# # list1 = [[1, 2, 3], [4, 5, 6]]
# # flatten_list = [item for sub_list in list1 for item in sub_list]
# # print(flatten_list)


# #Write a list comprehension to generate a list of all prime numbers up to 100.
# primes = [x for x in range(2, 101) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]

# print(primes)
# # returning positive values with square and negative values remain un changed

# list = [1,2,4,-3,-5,-5]

# M = [x**2 if x>0 else x for x in list]
# print(M)

# #Given two lists, list1 and list2, write a list comprehension to create a list of all possible pairs (tuples) from these lists.

# list1 =[1,2,3,4]

# list2 = ['a','b','c','d']

# l2 = [(x,y) for x in list1 for y in list2]

# print(l2)


#How would you use a nested list comprehension to generate the multiplication table (1 through 10)?

table =[i*j for i in range(1,11) for j in range(1,11)]
for row in table:
    print(f"i * j = {row}")