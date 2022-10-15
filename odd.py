"""
Returns all elements that are odd

"""

def fun(list):
    lis=[]

    for i in list:
        if  i%2==1:
            lis.append(i)

    return lis


z=(fun([1,11,7,8,-1,6]))
print(z)

if z == [1, 11, 7, -1]:
    print('pass')
else:
    print('fail')


y=(fun([6,8,2,]))
print(y)

if y == []:
    print('pass')
else:
    print('fail')
