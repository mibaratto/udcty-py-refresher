## Examples of iteration with for loops.

# my_list = [0, 1, 2, 3, 4, 5]

## Print each value in my_list. Note you can use the "in" keyword to iterate over a list.
# for item in my_list:
#   print('The value of item is: {}'.format(item))

## Print each index and value pair.
# for i, value in enumerate(my_list):
#     print('The index value is: ' + str(i) + '. The value at i is: ' + str(value))

# a = ["Geeks", "for", "Geeks"]

# Iterating list using enumerate to get both index and element
# for i, name in enumerate(a):
#     print(f"Index {i}: {name}")

# Converting to a list of tuples
# print(list(enumerate(a)))

## Print each number from 0 to 9 using a while loop.
# i = 0
# while(i < 10):
#     print(i)
#     i += 1

## Print each key and dictionary value. Note that you can use the "in" keyword 
## to iterate over dictionary keys.
# my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
# for key in my_dict:
#   print(key + ', ' + my_dict[key])

# print("TEST")

# my_dict = {'a':[00, 1, 2, 3], 'b':[0, 11, 2, 3], 'c':[0, 1, 22, 3], 'd':[0, 1, 2, 33]}
# i = 0
# output = []
# for key in my_dict:
#     output.append(my_dict[key][i])
#     i += 1
# print(output)

# my_list_1 = [4, -6, 7, 2, -4, 10]
# def smallest_positive():
#   for item in my_list_1:
#     return min(my_list_1)
    
# result = smallest_positive()
# print(result)


my_list_1 = []


# def smallest_positive(input):
#   if len(input) == 0:
#      return None
#   minimum = input[0]
#   for item in input:
#       if item < input[0] and item > 0:
#         minimum = item
#   if minimum < 0:
#      return None
#   else:
#     return minimum
   
# result = smallest_positive(my_list_1)
# print(result)


my_dict = {'a':[0, 1, 2, 3], 'b':[0, 1, 2, 3], 'c':[0, 1, 2, 3], 'd':[0, 1, 2, 3]}
i = 0
output = []
for key in my_dict:
    print(key)
    print(my_dict[key])
    output.append(my_dict[key][i])
    i += 1
print(output)






# def smallest_positive(in_list):
#   if len(in_list) == 0:
#     return None
#   else: 
#     smallest = in_list[0]
#     for item in in_list:
#       if item < smallest and item >= 0:
#           smallest = item

#   if smallest < 0:
#     return None
#   else:    
#     return smallest          
            

# print(smallest_positive([-6, -9, -7]))


# This exercise uses a data structure that stores course information.
# The data structure format is:
#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }
# courses = {
#     'spring2020': { 'cs101': {'name': 'Building a Search Engine',
#                            'teacher': 'Dave',
#                            'assistant': 'Peter C.'},
#                  'cs373': {'name': 'Programming a Robotic Car',
#                            'teacher': 'Sebastian',
#                            'assistant': 'Andy'}},
#     'fall2020': { 'cs101': {'name': 'Building a Search Engine',
#                            'teacher': 'Dave',
#                            'assistant': 'Sarah'},
#                  'cs212': {'name': 'The Design of Computer Programs',
#                            'teacher': 'Peter N.',
#                            'assistant': 'Andy',
#                            'prereq': 'cs101'},
#                  'cs253': {'name': 'Web Application Engineering - Building a Blog',
#                            'teacher': 'Steve',
#                            'prereq': 'cs101'},
#                  'cs262': {'name': 'Programming Languages - Building a Web Browser',
#                            'teacher': 'Wes',
#                            'assistant': 'Peter C.',
#                            'prereq': 'cs101'},
#                  'cs373': {'name': 'Programming a Robotic Car',
#                            'teacher': 'Sebastian'},
#                  'cs387': {'name': 'Applied Cryptography',
#                            'teacher': 'Dave'}},
#     'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
#                            'teacher': 'Dorina'},
#                         'cs003': {'name': 'Programming a Robotic Robotics Teacher',
#                            'teacher': 'Jasper'},
#                      }
#     }


# def when_offered(courses, course):
#     result = []
#     for season_key in courses:
#        courses_ids = courses[season_key]
#        for key_id in courses_ids:
#           if key_id == course:
#             result.append(season_key)
    
#     return result



# print(when_offered(courses, 'cs101'))
# # Correct result: 
# # ['fall2020', 'spring2020']
# print(when_offered(courses, 'bio893'))
# # Correct result: 
# # []


#  Class declaration sample
# class Person:
#     def __init__(self, name, age):
#         self.person_name = name
#         self.person_age = age

#     def birthday(self):
#         self.person_age += 1

#     def getName(self):
#         return self.person_name

# bob = Person('Bob', 32)
# print(bob.getName())
# # prints Bob


# bob.birthday()
# print(bob.person_age)
# # prints 33



# Person class 


# *************************PROXIMO PASSO: COMO CRIAR UM DICIONÁRIO