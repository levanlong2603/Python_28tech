#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int maxn = 26;
int n, m;
char s, t;
vector<pair<int, int>> adj[maxn];

int toIndex(char c) {
    return c - 'A';
}

char toChar(int index) {
    return index + 'A';  
}

void nhap() {
    cin >> n >> m >> s;
    for (int i = 0; i < m; i++) {
        char x, y;
        int w;
        cin >> x >> y >> w;
        adj[toIndex(x)].push_back({toIndex(y), w});
        adj[toIndex(y)].push_back({toIndex(x), w});
    }
}

const int INF = 1e9;
int pre[maxn];

void dijkstra(char s) {
    vector<ll> d(n, INF);
    d[toIndex(s)] = 0;
    pre[toIndex(s)] = toIndex(s);
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> Q;
    Q.push({0, toIndex(s)});
    
    while (!Q.empty()) {
        pair<int, int> top = Q.top(); Q.pop();
        int u = top.second;
        int kc = top.first;
        if (kc > d[u]) continue;

        for (auto it : adj[u]) {
            int v = it.first;
            int w = it.second;
            if (d[v] > d[u] + w) {
                d[v] = d[u] + w;
                Q.push({d[v], v});
                pre[v] = u;
            }
        }
    }

    vector<int> path;
    for (int i = 0; i < n; i++) {
        if (toChar(i) != s) {
            t = toChar(i);
            cout << "Tu " << s << " -> " << t << ": ";
            int current = i;
            while (1) {
                path.push_back(current);
                if (current == toIndex(s)) break;
                current = pre[current];
            }
            reverse(begin(path), end(path));
            for(int j = 0; j < path.size(); j++){
				cout << toChar(path[j]);
				if(j < path.size() - 1){
					cout << " - ";
				}
			}
			cout << ", cost(" << t << ") = " << d[i] << endl;
            path.clear();
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    nhap();
    dijkstra(s);
}
