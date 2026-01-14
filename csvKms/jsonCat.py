import json


def average(infile, outfile):
    with open(infile, 'r') as json_in:
        cat = json.load(json_in)


    lst=[]
    for entry in cat:
        lst.append({'id':entry["id"],'avg':(entry["test1"]+entry["test2"])/2})


    with open(outfile, 'w') as json_out:
        json.dump(lst, json_out)

average("example.json","output.json")
