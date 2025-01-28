# This exercise uses a data structure that stores course information.
# The data structure format is:
#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }
courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }
# def when_offered(courses, course):
#     result = []
#     for season_key in courses:
#         courses_ids = courses[season_key]
#         for key_id in courses_ids:
#             if key_id == course:
#                 result.append(season_key)
    
#     return result
#     # TODO: Fill out the function here.
    
#     # TODO: Return list of semesters here.
#     return None
# print(when_offered(courses, 'cs101'))
# # Correct result: 
# # ['fall2020', 'spring2020']
# print(when_offered(courses, 'bio893'))
# # Correct result: 
# # []

def when_offered(courses, course):
    result = []
    for semestre in courses:
        print(semestre)
        if course in courses[semestre]:
            result.append(semestre)
    return result

resposta = when_offered(courses, "cs101")
print(resposta)

# for item in courses:
#    print(item)


# # create a python dictionary 
# d = {"name": "Geeks", "topic": "dict", "task": "iterate"}

# # loop over dict values
# for val in d.values():
#     print(val)


# # default loooping gives keys
# for keys in d:
#     print(keys)
    
# # looping through keys    
# for keys in d.keys():
#   print(keys)