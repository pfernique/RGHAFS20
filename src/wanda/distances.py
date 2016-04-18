import itertools
import math

def intra(X, Y ,Z, op=min):
    _d = []
    for i, j in itertools.combinations(zip(X, Y, Z), 2):
        _d.append(math.sqrt(sum([math.pow(i[k]-j[k],2) for k in range(3)])))
    d = []
    i = 0
    for j in range(X.shape[0]-1):
        d.append(op(_d[i:i+X.shape[0]-1-j]))
        i = X.shape[0]-1-j
    return d

def inter(X0, Y0, Z0, X1, Y1, Z1, op=min):
    d = []
    for i in zip(X0, Y0, Z0):
        _d = []
        for j in zip(X1, Y1, Z1):
            _d.append(math.sqrt(sum([math.pow(i[k]-j[k],2) for k in range(3)])))
        if not len(_d) == 0:
            d.append(op(_d))
    return d
