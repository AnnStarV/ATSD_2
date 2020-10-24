# import json
# from random import randint
#
# class Node:
#     def __init__(self, value = None, next = None):
#         self.value = value
#         self.next = next
#
#     def __str__(self):
#         return str(self.value)
#
# class LinkedList:
#     def __init__(self):
#         self.first = None
#         self.last = None
#         self.length = 0
#
#     def add(self, x):
#         self.length += 1
#         if self.first == None:
#             # self.first и self.last будут указывать на одну область памяти
#             self.last = self.first = Node(x, None)
#         else:
#             self.last.next = self.last = Node(x, None)
#
#     def __str__(self):
#         if self.first != None:
#             current = self.first
#             out = 'LinkedList [\n' + str(current.value) + '\n'
#             while current.next != None:
#                 current = current.next
#                 out += str(current.value) + '\n'
#
#             return out + ']'
#
#
#     def find_element(self, findsurname):
#         if self.first != None:
#             current = self.first
#             if current.value["surname"] == findsurname:
#                 print(current.value["post"])
#                 return
#             while current.next != None:
#                 current = current.next
#                 if current.value["surname"] == findsurname:
#                     print(current.value["post"])
#                     return
#             return
#
# class HashTable(object):
#     def __init__(self):
#         self.table = [None] * 10
#         self.size = 0
#         self.goldconst = 0.618033
#
#     def get_value(self, key, size):
#         return int(size * ((key * self.goldconst) % 1))
#
#     def insert(self, key, val):
#         elem = LinkedList()
#         self.size += 1
#
#         key = self.get_value(key, self.size)
#         if self.table[key] is None:
#             self.table[key] = elem
#             elem.add(val)
#         else:
#             self.table[key].add(val)
#
#
#     def delete(self, key):
#         val = self.get_value(key, self.size)
#         if self.table[val] != None:
#             if type(self.table[val]) == list:
#                 i = self.table[val].index(key)
#                 self.table[val][i] = None
#             else:
#                 self.table[val] = None
#         else:
#             KeyError()
#
#     def __str__(self):
#            for i in self.table:
#                print(i)
#
#
#     def find(self, findsurname):
#         for i in range(len(self.table)):
#             if (self.table[i]!=None):
#                 self.table[i].find_element(findsurname)
#
#
# with open("data.json", "r", encoding='utf-8') as read_file:
#     data = json.load(read_file)
#
# list_data = data["workers"]
# lenght = len(list_data)
#
# N = HashTable()
#
# while lenght > 0:
#     lenght -= 1
#     key = randint(10, 100)
#     N.insert(key, list_data[lenght])
#
# N.insert(92, {'patronymic': 'Alexeeevich', 'post': 'менеджер', 'name': 'Натан', 'surname': 'Журавлёв'})
# N.delete(92)
# N.__str__()
# N.find("Панфилов")
