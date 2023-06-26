

dict1 = {'Kot': ['94372', '27535'],'Kit': ['09097'],'Tim': ['11445', '66223'],'Vova': ['32121', '99999']}
#dict2 = {'Foma': ['11111'],'Vova': ['12123', '23231'],'Tom': ['75846', '43123', '09098'],'Kot': ['94372', '27538']}
dict2 = {}
dict3 = {}
dict4 = {}
#list1 = []
#list2 = []
#list3 = []



file_name = 'my_contacts.txt'
with open(file_name, 'r', encoding='utf-8') as file:
    file_string = file.readlines()
    # print(file_string)
    for string in file_string:
        string = string.strip()
        name, number = string.split(': ')
        dict2[name] = number




for key, value in dict1.items():
    if key in dict2:
        dict3[key] = value
# print(self.dict3, 1)
for keys, values in dict2.items():
    if keys in dict1:
        dict4[keys] = values
# print(self.dict4)
for key, value in dict3.items():
    list1 = dict3[key]
    #list1 = list1.strip('[]')
    list2 = dict4[key]
    # list2 = list2.strip('[]')
    list2 = list(list2)

    print(list2)

#for key, value in dict1.items():
        #if key in dict2:
            #dict3[key] = value
#for keys, values in dict2.items():
    #if keys in dict1:
        #dict4[keys] = values

#for key , value in dict3.items():
    #list1 = list(set(dict3[key]+ dict4[key]))
    #dict4[key] = list1
    #print(key,list1)

#print(dict3)
#print(dict4)

#list3 = list1 + list2
#list1.extend(list2)
#print(dict3)
