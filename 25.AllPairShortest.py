#Day25 All-Pairs Shortest Paths (with Negative Edges Allowed)
N,M=map(int,input().split())
INF=10**15
d=[[INF]*N for _ in range(N)]
for i in range(N):d[i][i]=0
for _ in range(M):
    u,v,w=map(int,input().split())
    d[u-1][v-1]=min(d[u-1][v-1],w)
for k in range(N):
  for i in range(N):
    for j in range(N):
      if d[i][k]<INF and d[k][j]<INF:
        d[i][j]=min(d[i][j],d[i][k]+d[k][j])
for i in range(N):
  print(*("INF" if x==INF else x for x in d[i]))
