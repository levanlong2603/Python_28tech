# Code By Lê Văn Long - B22DCVT316

import heapq
INF = int(1e9)
maxn = 100001

# Khai báo các biến toàn cục
n, m, s, t = 0, 0, 0, 0
adj = [[] for _ in range(maxn)]
pre = [-1] * maxn

def nhap():
    global n, m, s, t
    n, m, s, t = map(int, input().split())
    for _ in range(m):
        x, y, w = map(int, input().split())
        adj[x].append((y, w))

def dijkstra(s, t):
    # Mảng lưu khoảng cách đường đi
    d = [INF] * (n + 1)
    d[s] = 0
    pre[s] = s
    Q = []
    # {khoảng cách, đỉnh}
    heapq.heappush(Q, (0, s))
    
    while Q:
        kc, u = heapq.heappop(Q)
        if kc > d[u]:
            continue
        
        # Relaxation: cập nhật khoảng cách với các đỉnh kề với u
        for v, w in adj[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(Q, (d[v], v))
                pre[v] = u  # trước v là u
    
    print(d[t])
    
    # Tìm đường đi
    path = []
    while True:
        path.append(t)
        if t == s:
            break
        t = pre[t]
    
    path.reverse()
    print(" ".join(map(str, path)))

if __name__ == "__main__":
    nhap()
    dijkstra(s, t)
