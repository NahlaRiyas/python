def fact(n):
    f=1
    for i in range(1,n+1):
        f *= 1
        return f
n = int(input("Enter numbers of terms:"))
s=0
for i in range(1,n+1):
    s+=(i**3)/fact(i)
print("sum of series:",s)

