def getsol(key,dict1):
    list1=[]
    for i in key:
        list1.append(dict1[i])
    return list1

def checkthedata(recs,findredc):
    count=0
    keys=list(findredc.keys())
    values=list(findredc.values())
    print(keys,values)
    for dic in recs:
        want=getsol(keys,dic)
        if want==values:
            count+=1
    return count
recs = [{"fname": "abc01", "lname": "xyz02", "age": "32",
              "address": "111 xyz rd, abc city, MD, 21774"},
          {"fname": "abc02", "lname": "xyz02", "age": "32",
              "address": "112 xyz rd, abc city, MD, 21774"},
          {"fname": "abc02", "lname": "xyz02", "age": "43",
              "address": "113 xyz rd, abc city, MD, 21774"},
          {"fname": "abc03", "lname": "xyz02", "age": "22",
              "address": "114 xyz rd, abc city, MD, 21774"}
         ]
findredc = {"fname": "abc01", "lname": "xyz02"}
print(checkthedata(recs,findredc))
