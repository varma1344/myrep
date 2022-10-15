def fun(list,num):
    j=0
    for i in list:
        if i==num:
            return j
        j+=1
    return -1


z=(fun([1,11,7,8,-1,6],11))
print(z)

if z==1:
    print('pass')
else:
    print('fail')


y=(fun([1,11,7,8,-1,6],6))
print(y)

if y==5:
    print('pass')
else:
    print('fail')
