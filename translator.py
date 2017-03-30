#!/usr/bin/python
import sys
import os

FILE = 0
FUNCTION = 1
TOKEN = 2
TRANSLATE = 3

keyWords = ['if', 'while', 'for']

basePath = './'
if len(sys.argv) < 2:
    print 'Error, need paramter 1 source folder'
    sys.exit()

basePath = sys.argv[1]

if basePath[-1] != '/':
    basePath += '/'

print 'Base Path:', basePath

f = open('translator.csv')
db = f.readlines()
f.close()
db2 = []
for i in range(0, len(db)):
    db2.append(db[i].strip().split(','))

for root, dirs, files in os.walk(basePath):
    #print 'ROOT:', root, 'DIR:', dirs, 'FILE:', files
    for fname in  files:
        if not fname.endswith('.h') and not fname.endswith('.c'):
            continue

        print 'Processing file *' + root + fname + '*'
        f = open(root + fname, 'r')
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
                if l[FILE] == fname and (l[FUNCTION] == function or l[FUNCTION] == '*'):
                    txt[i] = txt[i].replace(l[TOKEN], l[TRANSLATE])

        newRoot = root.replace(basePath, basePath[0:-1] + '2/')
        try:
            os.mkdir(newRoot)
        except:
            pass
        f = open(newRoot + fname, 'w')
        for i in range(0, len(txt)):
            f.write(txt[i])
        f.close()
