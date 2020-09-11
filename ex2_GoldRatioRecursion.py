
def gold_ratio(n):
    if n==0:
        return 1.
    if n==1:
        return 2.
    else:
        p=1
        for g in range(2,n+1):
            p*=(1/gold_ratio(g-1))
        return p*fibss(n)
    


def fibss(n):
    fibs=[3,5]
    for x in range(n-2):
        fibs.append(fibs[x]+fibs[x+1])
    return fibs[n-2]

def gold_ratio(n):
    if n == 0:
        return 1
    else:
        return 1 + 1.0 / gold_ratio(n-1)