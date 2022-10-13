f = open('mydata','a')
f.write('java')

f = open('mydata','r')
print(f.read())

from pathlib import Path

pathtofile = 'mydata'
fun = Path(pathtofile)

if fun.is_file():
    print(f'the file {pathtofile} is exists')
else:
    print(f'the file {pathtofile} does not exists')