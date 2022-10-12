def myfuc(lst,num):
    j=0
    for i in lst:
        if i==num:
            return j
        j+=1
    return -1
print(myfuc([1,11,7,8,-1,6],11))

