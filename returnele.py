def fun(list,num):
    count=0
    for i in list:
        if  i%2==1:
            count+=1

    return count


z=(fun([1,11,7,8,-1,6],11))
print(z)

if z==4:
    print('pass')
else:
    print('fail')


y=(fun([1,11,7,8,-1,6],6))
print(y)

if y==4:
    print('pass')
else:
    print('fail')
