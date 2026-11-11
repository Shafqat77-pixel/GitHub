#m1
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
# for name in data["branches"]:
#     print(name["name"])


#m2
import json

with open("test.json") as ptr:
 data = json. load(ptr)
new = []
for i in data["branches"]:
 for x in i["teachers"]:
   if x["subject"] == "Python":
    new. append({"branch": i['name' ], "teacher_name": x['name'], "experience": x['experience']})

for i in new:
  print(i)