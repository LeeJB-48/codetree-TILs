N = int(input())

lst = sorted([list(map(int,input().split())) for _ in range(N)])
distances_btw = []
min_R = 1000000

for i in range(N-1):
    if lst[i][1] == 0 or lst[i+1][1] == 0:
        min_R = min(min_R,lst[i+1][0]-lst[i][0])

min_R -= 1


cnt = 0
prev = -1
infecting = False
for position,infected in lst:
    if not infecting: #새로운 infecting point  설정 
        if not infected:#근데 지금 not infected된 사람이라면 
            pass
        else:
            prev = position
            cnt += 1
            infecting = True
    else: #이미 infecting point가 있는 경우
        if not infected:
            infecting = False
        else:
            if position - prev <= min_R:
                prev = position
            else:
                prev = position
                cnt += 1
print(cnt)