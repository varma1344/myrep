def func(list,num):
    count=0
    for i in list:
        if i<=num:
            count+=1
    return count

y=(func([1,11,7,8,-1,6],10))
print(y)

if y==6:
    print('pass')
else:
    print('fail')

z=(func([1,11,7,8,-1,6],11))
print(z)

if z==6:
    print('pass')
else:
    print('fail')