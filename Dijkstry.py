import sys
from heapq import *
class Dijkstra():
    def __init__(self, vertices,start):
        self.start=start
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.pred=[0]*self.V
        self.dist = [sys.maxsize] * self.V
        self.Q=[]
    def dijkstra(self):
        self.dist[self.start] = 0
        for i in range(self.V):
            heappush(self.Q, (self.dist[i],i+1))
        temp=[i[1] for i in self.Q]
        while self.Q:
            v=heappop(self.Q)
            u=v[1]
            temp.remove(u)
            for i in range(self.V):
                a=self.graph[u-1][i-1]
                if a:
                    x=self.dist[u-1]+a
                    if x<self.dist[i-1]:
                        self.pred[i-1] = u
                        self.dist[i-1] = x
                    else:
                        continue
        self.printDjikstra()
    def printDjikstra(self):
        print("pred = " + str(self.pred))
        print("dist = " + str(self.dist))
g = Dijkstra(5,0)
g.graph =[[0,3,0,3,5],
          [3,0,5,1,0],
          [0,5,0,2,0],
          [3,1,2,0,1],
          [5,0,0,1,0]]
g.dijkstra()