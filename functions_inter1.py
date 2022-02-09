x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#2
def iterateDictionary(students):
    for i in range(0, len(students)):
        print("first_name" + " - " + students[i]['first_name'] + " last_name" + " - " + students[i]['last_name'])
print(iterateDictionary(students))

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
    # first_name - Michael, last_name - Jordan
    # first_name - John, last_name - Rosales
    # first_name - Mark, last_name - Guillen
    # first_name - KB, last_name - Tonel

#3
def iterateDictionary2(key_name, some_list):
    for element in some_list:
        print(element[key_name])
iterateDictionary2("first_name", students)

def iterateDictionary2(key_name, some_list):
    for element in some_list:
        print(element[key_name])
iterateDictionary2("last_name", students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


#4
def printInfo(some_dict):
    for element in some_dict:
        print(len(some_dict[element]), element)
        for value in range(len(dojo[element])):
            print(some_dict[element][value])
printInfo(dojo)