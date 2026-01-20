import json
d={}
with open('brazi.json', 'r') as f:
    craciun = json.load(f)
    for brad in craciun:
        if brad["c"] in d:
             d[brad["c"]]=d[brad["c"]]+brad["nr"]
        else:
            d[brad["c"]]=brad["nr"]


print(d)

