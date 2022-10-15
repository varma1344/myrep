def is_greater(a,b):
    if a>b:
        return True
    else:
        return False

a=int(input())
b=int(input())

if is_greater(a,b) != True :
    print(a,'is lesser than ',b)
if is_greater(a, b) != False :
    print(a,'is greater than ',b)
