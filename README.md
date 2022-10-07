# myrep

def myfunc(lis,num):
    count=0
    for i in lis:
        if i <= num:
           count=count+1
    return count
print(myfunc([1,11,7,8,-1,6],11))
print(myfunc([1,11,7,8,-1,6],10))
print(myfunc([1,11,7,8,-1,6],-1))
print(myfunc([1,11,7,8,-1,6],-2))
