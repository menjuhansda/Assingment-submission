Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #5 inbuilt function of list
>>> #append
>>> lst=[1,2,3,]
>>> print(lst)
[1, 2, 3]
>>> lst.append(4)
>>> print(lst)
[1, 2, 3, 4]
>>> #extend
>>> lst=[1,2,3]
>>> print(lst)
[1, 2, 3]
>>> lst.extend([4,5,6])
>>> print(lst)
[1, 2, 3, 4, 5, 6]
>>> #Insert
>>> lst=[1,2,3]
>>> print(lst)
[1, 2, 3]
>>> lst.insert(5,"Menju hansda")
>>> #List
>>> list1=list()
>>> list1
[]
>>> #length
>>> list1=[10,20,30,40,50]
>>> len(list1)
5
>>> #5 inbuilt function of dictionary
>>> #dictionary.clear
>>> square={1:1,2:4,3:9,4:16,5:25}
>>> print(square)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> square.clear()
>>> print(square)
{}
>>> #dictionary.item
>>> square={1:1,2:4,3:9,4:16,5:25}
>>> print(square)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> print(square.items())
dict_items([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
>>> #dictionary.keys
>>> square={1:1,2:4,3:9,4:16,5:25}
>>> print(square)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> print(square.keys())
dict_keys([1, 2, 3, 4, 5])
>>> #dictionary.values
>>> square={1:1,2:4,3:9,4:16,5:25}
>>> print(square)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> print(square.values())
dict_values([1, 4, 9, 16, 25])
>>> #dictionary.popitem
>>> square={1:1,2:4,3:9,4:16,5:25}
>>> print(square)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> square.popitem()
(5, 25)
>>> print(square)
{1: 1, 2: 4, 3: 9, 4: 16}
>>> 