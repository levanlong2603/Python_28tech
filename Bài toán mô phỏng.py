# code by Lê Văn Long - B22DCVT316

import heapq

INF = int(1e9)
maxn = 26  

n, m = 0, 0
s = ''
adj = [[] for _ in range(maxn)]
pre = [0] * maxn

def to_index(c):
    return ord(c) - ord('A')  

def to_char(index):
    return chr(index + ord('A'))  

def nhap():
    global n, m, s
    n, m, s = input().split()
    n, m = int(n), int(m)
    for _ in range(m):
        x, y, w = input().split()
        w = int(w)
        adj[to_index(x)].append((to_index(y), w))
        adj[to_index(y)].append((to_index(x), w))

def dijkstra(s):
    d = [INF] * n
    d[to_index(s)] = 0
    pre[to_index(s)] = to_index(s)

    Q = []
    heapq.heappush(Q, (0, to_index(s)))

    while Q:
        kc, u = heapq.heappop(Q)
        if kc > d[u]:
            continue
        
        for v, w in adj[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(Q, (d[v], v))
                pre[v] = u

    for i in range(n):
        if to_char(i) != s:
            t = to_char(i)
            print(f"{s} -> {t}: {d[i]}")
            current = i
            path = []
            while True:
                path.append(current)
                if current == to_index(s):
                    break
                current = pre[current]
            path.reverse()
            print(" ".join(to_char(x) for x in path))

if __name__ == "__main__":
    nhap()
    dijkstra(s)
