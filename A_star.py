import sys
class A:
    def __init__(self, vertices, h, start):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.h = h
        self.start=start
        self.f = [0]*self.V
        self.g = [sys.maxsize]*self.V
        self.visited=[False]*self.V
        self.pred=[0]*self.V
    def get_min(self):
        min = sys.maxsize
        min_index = 0
        for i in range(self.V):
            if self.g[i] < min and self.visited[i] == False:
                min = self.g[i]
                min_index = i
        return min_index
    def a_star(self):
        self.g[self.start]=0
        self.f[self.start] = self.h[self.start] + self.g[self.start]
        for i in range(self.V):
            v=self.get_min()
            self.visited[v]=True
            for j in range(self.V):
                if self.graph[v][j] > 0 and self.visited[j]==False and self.g[j] > self.g[v] + self.graph[v][j]:
                    self.g[j] = self.g[v] + self.graph[v][j]
                    self.pred[j] = v
                    self.f[j] = self.g[j] + self.h[j]
        self.printA_star()
    def printA_star(self):
        print("h = " + str(self.h))
        print("g = " + str(self.g))
        print("f = " + str(self.f))
        print("pred = " + str(self.pred))
h = [4, 8, 3, 4, 5, 2, 1, 0]
g=A(8, h, 0)
g.graph = [
    [0,5,0,1,0,0,0,0],
    [0,0,2,0,1,0,0,0],
    [0,0,0,0,0,0,0,3],
    [0,0,0,0,1,2,0,0],
    [0,0,4,0,0,0,0,0],
    [4,0,0,0,0,0,2,0],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,2,0,0,0]
    ]
g.a_star()