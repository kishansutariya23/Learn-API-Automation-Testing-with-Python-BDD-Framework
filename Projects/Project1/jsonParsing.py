import json

# load is used for external file
# loads is used for string


# JSON in string variable
courses = '{"name":"kishansutariya23","languages":["Python","SQL"]}'

# Loads method :- parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])




# for getting first language
print(dict_courses['languages'])
# as above result give list we are storing it in variable
list_languages = dict_courses['languages']
print(type(list_languages))
print(list_languages)
print(list_languages[0])




# for getting second language with less line of code
list_languages = dict_courses['languages'][1]
# or
print(dict_courses['languages'][1])








# open the json file and parse it
# by default it will be read mode
with open('C:\Consistency\Python testing\API testing\Projects\Project1\json_file.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['menu']['popup']['menuitem'][1])


# if order of list/data inside the json change then how to tackle
# so don't go with index instead go with loops and condition
# assert 10=10  --> wont get error and NO o/p if condition is false then we will get error
# for testing the file we use above method
#
    for v in data['menu']['popup']['menuitem']:
        if v['value']=='Open':
            print('Run successful')







# compare 2 json
with open('C:\Consistency\Python testing\API testing\Projects\Project1\json_file2.json') as f2:
    data2 = json.load(f2)
    assert data == data2
    print(data == data2)


