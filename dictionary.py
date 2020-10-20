#!/usr/bin/python

people  = {
    "Amber" : 25, "Chris" : 29, "Mike" : 22,"Sarah" : 21
}

entry = (raw_input("Type the name of the person you are looking for or type in 'ALL' if you would like to list entire contents of the dictionary:"))

if entry == 'ALL':
    for key in people.keys():
        print ('Name: {} Age: {}'.format(key, people[key]))


if entry in people:
    print ("{} is {} years old.".format(entry, people[entry]))
else:
    print('Not found')
