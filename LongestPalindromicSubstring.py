def lps(input1):
    
    X = input1
    Y = input1[::-1]
    m = len(X)
    n = len(Y) 
    L = [[None]*(n+1) for i in range(m+1)]
    result = 0
    for i in range(m + 1):
            for j in range(n + 1):
                if (i == 0 or j == 0):
                    L[i][j] = 0
                elif (X[i-1] == Y[j-1]):
                    L[i][j] = L[i-1][j-1] + 1
                    result = max(result, L[i][j])
                else:
                    L[i][j] = 0
    return result