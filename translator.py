#!/usr/bin/python

FILE = 0
FUNCTION = 1
TOKEN = 2
TRANSLATE = 3

keyWords = ['if', 'while', 'for']

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
    l = txt[i].strip()
    if l.strip() == '':
        continue
    if l.split(' ')[0] not in keyWords and l[-1] != ';' and l[-1] == ')' or l[-1] == '{':
        pos1 = l.rfind('(')
        pos2 = l[0:pos1].rfind(' ') + 1
        function = l[pos2:pos1]

        print 'Processing function *' + function + '*'
        
    for l in db2:
        if l[FILE] == name and (l[FUNCTION] == function or l[FUNCTION] == '*'):
            txt[i] = txt[i].replace(l[TOKEN], l[TRANSLATE])

name2 = name.split('.')[0] + '2.c'    
f = open(name2, 'w')
for i in range(0, len(txt)):
    f.write(txt[i])
f.close()
