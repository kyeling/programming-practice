# Duolingo HackerRank

def isOpposite(dxn1, dxn2):
    if dxn1 == 'n':
        return dxn2 == 's'
    elif dxn1 == 's':
        return dxn2 == 'n'
    elif dxn1 == 'e':
        return dxn2 == 'w'
    else:
        return dxn2 == 'e'

def isPerpendicular(dxn1, dxn2):
    return (dxn1 != dxn2 and not isOpposite(dxn1, dxn2))

def solution(path):
    n = len(path)
    i = 0
    run_dxns = []
    run_cnts = []
    res = []

    while i < n:
        run_dxns.append(path[i])
        count = 1
        while i+1 < n and path[i] == path[i+1]:
            count += 1
            i += 1
        run_cnts.append(count)
        i += 1
    print(run_dxns, run_cnts)

    m = len(run_dxns) - 1

    for i in range(m):
        if isOpposite(run_dxns[i], run_dxns[i+1]):
            pass
        elif i+2 < m and isOpposite(run_dxns[i], run_dxns[i+2]): # isPerpendicular(run_dxns[i], run_dxns[i+1]) implied
            pass

if __name__ == "__main__":
    path = ['s', 'e', 'e', 's', 's', 'w', 'w', 'e', 'e', 's']
    res = solution(path)
    print(res)