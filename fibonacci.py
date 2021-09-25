"""
la suite de fibonacci
"""

def fibo(n):
    """
    # une implémentation naïve et inefficace
    """
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
