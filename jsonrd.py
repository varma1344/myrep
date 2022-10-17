import json


def getsol(key, dict1):
   list1 = []
   for i in key:
      list1.append(dict1[i])
   return list1


def checkthedata(recs, findredc):
   count = 0
   keys = list(findredc.keys())
   values = list(findredc.values())
   print(keys, values)
   for dic in recs:
      want = getsol(keys, dic)
      if want == values:
         count += 1

   return count


with open("recs.json") as f:
   recs = json.loads(f.read())

findredc = {'fname': 'abc02', 'lname': 'xyz02'}
x=(checkthedata(recs, findredc))
print(x)
if x==2:
   print("pass")
else:
   print("fail")