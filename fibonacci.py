"""
la suite de fibonacci
"""

cache={0:0,1:1}

def fibo_cached(n):
    if n in cache:
        return cache[n]
    if n<0:
        return False
    value= fibo_cached(n-2)+fibo_cached(n-1)
    cache[n]=value
    return value