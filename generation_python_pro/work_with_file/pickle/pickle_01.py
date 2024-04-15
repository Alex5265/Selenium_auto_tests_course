from copy import deepcopy

data1 = [[1, 2], [3, 4]]
data2 = deepcopy(data1)

print(data1[0] is data2[0])
print(data1[1] is data2[1])


# word = 'everything'
#
# data = f"b'there is {word} here"
#
# print(type(data))



# import pickle
#
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
#
# with open('file.pkl', 'wb') as file:
#     pickle.dump(obj, file)
#
#
# import pickle
#
# with open('file.pkl', 'rb') as file:     # используется файл полученный на предыдущем шаге
#     obj = pickle.load(file)
#     print(obj)
#     print(type(obj))
#
#
# import pickle
#
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# binary_obj = pickle.dumps(obj)
#
# print(binary_obj)
# print(type(binary_obj))
#
#
#
# import pickle
#
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# binary_obj = pickle.dumps(obj)
#
# new_obj = pickle.loads(binary_obj)
#
# print(new_obj)
#
#
# import pickle
#
# obj = {'Python': 1991, 'Java': 1995, 'C#': 2002}
# binary_obj = pickle.dumps(obj)
# new_obj = pickle.loads(binary_obj)
#
# print(obj == new_obj)
# print(obj is new_obj)



