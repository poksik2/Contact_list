import json

dict1 = {'Kot': ['94372', '27535'],'Kit': ['09097'],'Tim': ['11445', '66223'],'Vova': ['32121', '99999']}
#dict2 = {'Foma': ['11111'],'Vova': ['12123', '23231'],'Tom': ['75846', '43123', '09098'],'Kot': ['94372', '27538']}
#dict2 = {}
dict3 = {}
dict4 = {}
dict5 = {}
#list1 = []
list2 = []
list3 = []



file_name = 'my_contacts.txt'

with open(file_name, 'r', encoding='utf-8') as file:
    file_list = file.readlines()
    i = 0
    while i != len(file_list):
        dict2 = (file_list[i])
        #print(dict2)
        i +=1
        dict2 = dict2.strip()
        #print(dict2)
        dict2 = dict2.split(': ')
        #print(dict2)
        list2 = dict2[1]
        #print(list2)
        list2 = list2.split(', ')
        dict3[dict2[0]] = list2
    #print((dict3))



