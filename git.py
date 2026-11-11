#m1
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
# for name in data["branches"]:
#     print(name["name"])


#m2
# import json

# with open("test.json") as ptr:
#  data = json. load(ptr)
# new = []
# for i in data["branches"]:
#  for x in i["teachers"]:
#    if x["subject"] == "Python":
#     new. append({"branch": i['name' ], "teacher_name": x['name'], "experience": x['experience']})

# for i in new:
#   print(i)






#m3
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for son in data["branches"]:
#         new.append(son["students"])
# print(f"Branches da {len(new)}-ta Student bor \nBular")
# for i in new:
#     print(i)




#m4
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for pay in data["branches"]:
#         for i in pay["students"]:
#             new.append(i)
# print(max(new,key=lambda x:x["payment"]))




#m5
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for pay in data["branches"]:
#         for i in pay["students"]:
#             new.append(i["payment"])
# print(f"Barcha oquvchilarni jami paymenti: {sum(new)}")




#m6
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
#     for tajriba in data["branches"]:
#         for i in tajriba["teachers"]:
#             if i["experience"]>5:
#                 print(i)




# #m7
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
#     print("Python yo'nalishi mavjud filiallar:")

# for branch in data["branches"]:
#     python_bormi = False  
#     for i in branch["students"]:
#         if i["course"]=="Python":
#             python_bormi=True
#             break
#     if not python_bormi:
#         for t in branch["teachers"]:
#             if t["subject"]=="Python":
#                 python_bormi=True
#                 break

#     if python_bormi:
#         print(branch["name"]) 






#uyish1
# nums=[2,2, 1, 1, 1, 2, 2]
# new={}
# for i in nums:
#     if i in new:
#         new[i]+=1
#     else:
#         new[i]=1
# a=max(new.values())
# for key,value in new.items():
#     if a==value:
#         print(key)