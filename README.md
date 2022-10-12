"""
function which return max element in a given list

"""

def myfunc(lis):
    max=lis[0]
    for i in lis:
        if i>max:
           max=i

    return max
print(myfunc([1,11,7,8,-1,6]))
