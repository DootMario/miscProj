comp = "a3b2"

def unzip(zipped):
    unzipped=""
    for c in range(len(zipped)):
        if c<len(zipped)-1:
            if zipped[c+1].isdigit():
                unzipped=unzipped+(zipped[c]*int(zipped[c+1]))
                c=c+1
            if zipped[c].isalpha() and zipped[c+1].isalpha():
                unzipped=unzipped+zipped[c]
        elif zipped[c].isalpha():
            unzipped=unzipped+zipped[c]

    return unzipped

print(unzip(comp))
