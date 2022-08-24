Q = int(input())
chess = [[0] * Q for _ in range(Q)]

def issafe(i, j):
    for k in range(0, Q):
        if chess[i][k] == 1 or chess[k][j] == 1:
            return True
    for k in range(0, Q):
        for l in range(0, Q):
            if (k + l == i + j) or (k - l == i - j):
                if chess[k][l] == 1:
                    return True
    return False
def queens(n):
    if n == 0:
        return True
    for i in range(0, Q):
        for j in range(0, Q):
            
            if (not(issafe(i,j))) and (chess[i][j]!=1):
                chess[i][j] = 1
                if queens(n - 1) == True:
                    return True
                chess[i][j] = 0

    return False

queens(Q)
for s in chess:
    print (s)
