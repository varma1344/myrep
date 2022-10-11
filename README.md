"""
return number of elements that are less than or equal to than given number

"""


def myfunc(lis,num):
    count=0
    for i in lis:
        if i <= num:
           count=count+1
    return count
print(myfunc([1,11,7,8,-1,6],11))
