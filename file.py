f = open('demo','w')
f.write('welcome')

f = open('demo','r')
print(f.read())

from pathlib import Path

pathtofile = 'demo'
fun = Path(pathtofile)
if fun.is_file():
    print('true')
else:
    print('false')