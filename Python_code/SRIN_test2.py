test_case = [
    ["5 5","4 3 2 3 4 1 5 3 2 1"]
]

def pasangkan(arrData):
    dat = []
    arrDat = []
    for i in range(len(arrData)):
        if i % 2 == 0:
            dat.append(arrData[i])
        else:
            dat.append(arrData[i])
            arrDat.append(dat)
            dat = []
    return arrDat

def linkedList(arrData):
    dict = {}
    for i in range(len(arrData)):
        dict.update({arrData[i][0]:{"out":[arrData[i][1]]}})
        dict.update({arrData[i][1]:{"in":[arrData[i][0]]}})
    print(dict)
    for x,y in dict.items():
        for z, zz in y.items():
            for i in range(len(arrData)):
                if arrData[i][1] == x and arrData[i][0] not in zz:
                    dict[x][z].append(arrData[i][0])
                if arrData[i][0] == x and arrData[i][1] not in zz:
                    dict[x][z].append(arrData[i][1])
    print(dict)
    return 0

def solusi(N,M,arrData):
    dict = {}
    for i in range(len(arrData)):
        dict.update({arrData[i][0]:[arrData[i][1]]})
    print(dict)
    for x in dict:
        for i in range(len(arrData)):
            if arrData[i][0] == x:
                dict[x].append(arrData[i][1])
            elif arrData[i][1] == x:
                dict[x].append(arrData[i][0])
    print(dict)
    return 0
T=1
for i in range(1,T+1):
    N,M = map(int,test_case[i-1][0].split())
    arrData = test_case[i-1][1].split()
    arrData = pasangkan(arrData)
    # result = solusi(N,M,arrData)
    result = linkedList(arrData)
    print("#%d "%i,result)