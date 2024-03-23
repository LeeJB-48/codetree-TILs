n = int(input())
sy = [1,1]
if n == 1 or n == 2:
    print(sy[n-1])
else:
    for i in range(2,n):
        sy.append(sy[i-2]+sy[i-1])
    print(sy[n-1])