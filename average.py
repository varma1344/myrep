def fun(a,b,c):
    x=a+b+c
    avg=x/3
    return avg

y = (fun(4,5,6))
print(round(y,2))

if y == 5.0:
     print('pass')
else:
     print('fail')

z = (fun(7,3,12))
print(round(z,3))

if z == 9.0:
    print('pass')
else:
    print('fail')




