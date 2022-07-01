class Floyd:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.p = [[None for i in range(self.V)]for j in range(self.V)]
        self.d = [[None for i in range(self.V)]for j in range(self.V)]
    def floyda_w(self):
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j]>0:
                    self.p[i][j]=i+1
                else:
                    self.p[i][j]=0

        for i in range(self.V):
            for j in range(self.V):
                if i==j:
                    self.d[i][j]=0
                elif self.graph[i][j]>0:
                    self.d[i][j]=self.graph[i][j]
                else:
                    self.d[i][j]=float("inf")

        for i in range(self.V):
            for j in range(self.V):
                if i == j:
                    continue
                for n in range(self.V):
                    if n==i:
                        continue
                    x = self.d[j][i]+self.d[i][n]
                    if x<self.d[j][n]:
                        self.d[j][n]=x
                        self.p[j][n]=self.p[i][n]
        self.print_F()
    def print_F(self):
        print("Macierz d: ")
        for i in range(self.V):
            for j in range(self.V):
                print(self.d[i][j], end="  ")
            print("\n")
        print("Macierz p: ")
        for i in range(self.V):
            for j in range(self.V):
                print(self.p[i][j], end= "  ")
            print("\n")

g = Floyd(7)
g.graph =  [
    [0,1,5,0,0,0,0],
    [0,0,2,0,0,0,0],
    [0,0,0,0,0,0,0],
    [7,0,0,0,1,0,0],
    [0,0,0,0,0,1,0],
    [2,0,0,4,0,0,0],
    [6,0,0,0,0,3,0]
]
g.floyda_w()