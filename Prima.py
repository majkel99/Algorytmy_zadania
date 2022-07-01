import sys
class Prima:
    def __init__(self, vertices,start):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.pred=[0]*self.V
        self.k = [sys.maxsize] * self.V
        self.start = start
        self.INF = sys.maxsize
        self.selected = [False] * self.V
    def prima(self):
        self.selected[self.start] = True
        self.k[self.start] = 0
        while (self.start < self.V-1):
            min = self.INF
            y = 0
            for i in range(self.V):
                if self.selected[i]:
                    for j in range(self.V):
                        if ((not self.selected[j]) and self.graph[i][j]):
                            if min > self.graph[i][j]:
                                min = self.graph[i][j]
                                self.pred[self.start+1] = i+1
                                y=j
            self.k[self.start+1] = min
            self.selected[y] = True
            self.start += 1
        self.printPrima()
    def printPrima(self):
        print("pred = " + str(self.pred))
        print("k = " + str(self.k))
        print("suma elemntow tablicy k = " + str(sum(self.k)))

g=Prima(5,0)
g.graph = [[0,3,0,3,5],
   [3,0,5,1,0],
   [0,5,0,2,0],
   [3,1,2,0,1],
   [5,0,0,1,0]]
g.prima()