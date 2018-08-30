import json
data = [{'a':1, 'b':2}]
d = json.dumps(data)
with open("f.json","w") as f:
    f.write(d)


