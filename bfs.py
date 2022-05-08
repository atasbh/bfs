#Uses python3
import sys
import queue

def BFS(adj, src, dest, v, pred, dist):
    queue = []
    visited = [False for i in range(n)];
    for i in range(v):
 
        dist[i] = 1000000
        pred[i] = -1;
    visited[src] = True;
    dist[src] = 0;
    queue.append(src);
    while (len(queue) != 0):
        u = queue[0];
        queue.pop(0);
        for i in range(len(adj[u])):
         
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.append(adj[u][i]);
  
                if (adj[u][i] == dest):
                    return True;
  
    return False;

def distance(adj, s, t):
    pred=[0 for i in range(len(adj))]
    dist=[0 for i in range(len(adj))];
    if (BFS(adj, s, t, len(adj), pred, dist) == False):
        return -1
    path = []
    crawl = t;
    crawl = t;
    path.append(crawl);
    
    while (pred[crawl] != -1):
        path.append(pred[crawl]);
        crawl = pred[crawl];
        
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
