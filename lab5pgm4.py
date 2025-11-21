# armstrong.py

def is_armstrong(n):
    p = len(str(n))
    return n == sum(int(d)**p for d in str(n))

