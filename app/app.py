import json
from random import randint
import eel

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

# class BTreeNode:
#     def __init__(self, leaf=False):
#         self.leaf = leaf
#         self.keys = []
#         self.child = []
#
# class BTree:
#     def __init__(self, t):
#         self.root = BTreeNode(True)
#         self.t = t
#
#     # Print the tree
#     def print_tree(self, x, l=0):
#         print("Level ", l, " ", len(x.keys), end=":")
#         for i in x.keys:
#             print(i, end=" ")
#         print()
#         l += 1
#         if len(x.child) > 0:
#             for i in x.child:
#                 self.print_tree(i, l)
#
#     # Search 1
#     def search_by_date(self, k, x=None):
#         if x is not None:
#             i = 0
#             while i < len(x.keys) and k > x.keys[i]['date']:
#                 i += 1
#             if i < len(x.keys) and k == x.keys[i]['date']:
#                 print("find:", x.keys[i], '\n')
#                 return
#             elif x.leaf:
#                 print("find: Not exists!\n")
#                 return None
#             else:
#                 return self.search_by_date(k, x.child[i])
#         else:
#             return self.search_by_date(k, self.root)
#
#     def top_rain_dom(self, k, x=None):
#         arr = []
#         self.top_rain_stor(arr, k, self.root)
#         max = arr[0]
#         for i in range(len(arr)):
#             if(int(max['rain'].replace('%', '')) < int(arr[i]['rain'].replace('%', ''))):
#                 max = arr[i]
#         print("top rain: ", max, '\n')
#
#     # Метод для поиска всех дат из заданого месяца
#     def top_rain_stor(self, arr, k, x):
#         for i in x.keys:
#             if(i['date'].find(k) != - 1):
#                 arr.append(i)
#         if (len(x.child) > 0):
#             for i in x.child:
#                 self.top_rain_stor(arr, k, i)
#     # Search 2
#
#     # Insert the key
#
#     def insert_key(self, k):
#         root = self.root
#         if len(root.keys) == (2 * self.t) - 1:
#             temp = BTreeNode()
#             self.root = temp
#             temp.child.insert(0, root)
#             self.split(temp, 0)
#             self.insert_non_full(temp, k)
#         else:
#             self.insert_non_full(root, k)
#
#     # Insert non full condition
#     def insert_non_full(self, x, k):
#         i = len(x.keys) - 1
#         if x.leaf:
#             x.keys.append(None)
#             while i >= 0 and k['date'] < x.keys[i]['date']:
#                 x.keys[i + 1] = x.keys[i]
#                 i -= 1
#             x.keys[i + 1] = k
#         else:
#             while i >= 0 and k['date'] < x.keys[i]['date']:
#                 i -= 1
#             i += 1
#             if len(x.child[i].keys) == (2 * self.t) - 1:
#                 self.split(x, i)
#                 if k['date'] > x.keys[i]['date']:
#                     i += 1
#             self.insert_non_full(x.child[i], k)
#     # Split
#
#     def split(self, x, i):
#         t = self.t
#         y = x.child[i]
#         z = BTreeNode(y.leaf)
#         x.child.append(z)
#         x.keys.append(y.keys[t - 1])
#         z.keys = y.keys[t: (2 * t) - 1]
#         y.keys = y.keys[0: t - 1]
#         if not y.leaf:
#             z.child = y.child[t: 2 * t]
#             y.child = y.child[0: t - 1]
#     # delete elem from Tree
#
#     def remove(self, x):
#         F = BTree(self.t)
#         arr = []
#         self.createStorage(self.root, arr)
#
#         for i in range(len(arr)):
#             if(x == arr[i]['date']):
#                 arr.remove(arr[i])
#                 for i in range(len(arr)):
#                     F.insert_key(arr[i])
#                 self.root = F.root
#                 return
#         print('element isn\'t found ')
#     # Create an array storing all the elements of the tree
#
#     def createStorage(self, x, arr):
#         for i in x.keys:
#             arr.append(i)
#             # if(not i[1] in arr):
#         if len(x.child) > 0:
#             for i in x.child:
#                 self.createStorage(i, arr)
#
#
#
#
#
# B = BTree(3)
# with open("data.json", "r", encoding='utf-8') as read_file:
#     data = json.load(read_file)
# list_data = data["weather"]
# for i in list_data:
#     B.insert_key(i)
# # Вывод деревка
# B.print_tree(B.root)
# # Поиск по мобилке
# B.search_by_date("22/10/2020")
# # Поиск в заданом месяце(год уточняется во избежание тупиковых ситуаций) дня с самыми большими осадками
# B.top_rain_dom("10/2020")
# # удаление
# B.remove("21/11/2020")
# B.remove("21/11/2020")
# print()
# B.print_tree(B.root)
#
# # B.print_tree(B.root)


eel.init("web")
eel.start("index.html", size=(1000, 900))
