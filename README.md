"""
return number of position if ti find otherwise return -1

"""


def sel(list,num):
    j=0
    for i in list:
        if i==num:
            return j
        j+=1
    return -1
print(sel([1,11,7,8,-1,6],11))

