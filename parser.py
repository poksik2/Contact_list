
dict1 = {'Kot': ['94372', '27535'],'Kit': ['09097'],'Tim': ['11445', '66223'],'Vova': ['32121', '99999']}
dict2 = {'Foma': ['11111'],'Vova': ['12123', '23231'],'Tom': ['75846', '43123', '09098'],'Kot': ['94372', '27538']}
dict3 = {}
dict4 = {}
list1 = []
list2 = []
list3 = []

for key, value in dict1.items():
        if key in dict2:
            dict3[key] = value
for keys, values in dict2.items():
    if keys in dict1:
        dict4[keys] = values

for key , value in dict3.items():
    list1 = list(set(dict3[key]+ dict4[key]))
    dict4[key] = list1
    #print(key,list1)

#print(dict3)
print(dict4)

#list3 = list1 + list2
#list1.extend(list2)
#print(dict3)
