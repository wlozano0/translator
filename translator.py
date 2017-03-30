#!/usr/bin/python

FILE = 0
FUNCTION = 1
TOKEN = 2
TRANSLATE = 3

f = open('translator.csv')
db = f.readlines()
f.close()
db2 = []
for i in range(0, len(db)):
    db2.append(db[i].strip().split(','))

name = 'test.c'
f = open(name, 'r')
txt = f.readlines()
f.close()

function = ''
for i in range(0, len(txt)):
    if txt[i].startswith('//FUNCTION'):
        i += 1
        function = txt[i].split(' ')[1]
        pos = function.find('(')
        if pos != -1:
            function = function[0:pos]

        print 'Processing function ' + function
        
    for l in db2:
        if l[FILE] == name and (l[FUNCTION] == function or l[FUNCTION] == '*'):
            txt[i] = txt[i].replace(l[TOKEN], l[TRANSLATE])

name2 = name.split('.')[0] + '2.c'    
f = open(name2, 'w')
for i in range(0, len(txt)):
    f.write(txt[i])
f.close()
