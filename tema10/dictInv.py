dick = {"a":1,
        "b":2,
        "c":3,
        "f":3,
        "d":4,
        "e":5}

def invert(d):
    inverse={}
    for key,value in d.items():
        if value not in inverse.keys():
            inverse.update({value:[]})
        inverse[value].append(key)
    d.clear()
    for k in inverse.keys():
        d.update({k:inverse[k]})

invert(dick)

print(dick)