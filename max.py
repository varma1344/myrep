#return max element in a given list

def fun(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max

y=(fun([1,11,7,8,-1,6]))
print(y)

if y==11:
    print('pass')
else:
    print('fail')

z=(fun([1,11,7,28,-1,6]))
print(z)

if z==28:
    print('pass')
else:
    print('fail')