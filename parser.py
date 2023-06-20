
dict1 = {'Kot': ['94372', '27535'],'Kit': ['09097'],'Tim': ['11445', '66223']}
dict2 = {'Foma': ['11111'],'Vova': ['12123', '23231'],'Tom': ['75846', '43123', '09098'],'Kot': ['94372', '27538']}
dict3 = {}
list1 =[]
list2 = []

for name, num in dict1.items():
    if name in dict2.keys() and dict1.keys():
        list1 = num
        print(list)
for name, num in dict2.items():
    if name in dict1.keys() and dict2.keys():
        list2 = (num)
        print(type(list2))

list1 = list1+list2
print(list(set(list1)))
