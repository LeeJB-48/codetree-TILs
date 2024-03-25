n,m = map(int,input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
stack = [1]
seen = set()
count = -1
while(stack):
    cur = stack.pop()
    if cur not in seen:
        seen.add(cur)
        count += 1
        for next_node in range(1,n+1):
            if graph[cur][next_node]:
                stack.append(next_node)
    else:
        continue
print(count)