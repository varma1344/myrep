"""
average of all elements in the list
"""

def avg(list):
    n=len(list)
    if n==0:
        return 0
    total=0
    for i in list:
        total+=i
    return round(total/n,2)

y=(avg([1,11,7,8,-1,6,3]))
print(y)

if y==5.0:
    print('pass')
else:
    print('fail')

z=(avg([1,11,7,28,-1,6,3]))
print(z)

if z==5.0:
    print('pass')
else:
    print('fail')

