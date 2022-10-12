
"""
Returns all elements that are odd


"""


def myfunc(lis):
    list=[]
    for i in lis:
        if i%2==1:
           list.append(i)

    return list
print(myfunc([1,11,7,8,-1,6]))
