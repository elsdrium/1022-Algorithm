setlist = {}

def MakeSet(x):
    if FindSet(x):
        return
    setlist[x] = [x]

def Union(x1, x2):
    k1 = FindSet(x1)
    k2 = FindSet(x2)
    if k1 != k2 and k1 != None and k2 != None:
        if len(setlist[k1]) >= len(setlist[k2]):
            setlist[k1] = setlist[k1] + setlist[k2]
            del setlist[k2]
        else:
            setlist[k2] = setlist[k2] + setlist[k1]
            del setlist[k1]

def FindSet(x):
    for k in setlist.keys():
        if x in setlist[k]:
            return k
    return None


for i in range(1, 17):
    MakeSet(i)
for i in range(1, 16, 2):
    Union(i, i+1)
for i in range(1, 14, 4):
    Union(i, i+2)

Union(1, 5)
Union(11, 13)
Union(1, 10)
print FindSet(2), FindSet(9)
