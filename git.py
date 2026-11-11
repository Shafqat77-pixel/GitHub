#m1
import json
with open("test.json") as ptr:
    data=json.load(ptr)
for name in data["branches"]:
    print(name["name"])
    