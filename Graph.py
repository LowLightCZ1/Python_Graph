class Graph:
    def __init__(self, n) -> None:
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def add_edge(self, x, y, weight = 1):
        if 0 <= x < self.n and 0 <= y < self.n:
            self.matrix[x][y] = weight
        else:
            raise Exception(f"Chyba: Neplatný index uzlu({x} nebo {y})!")

    def remove_edge(self, x, y):
        self.add_edge(x,y,weight=0)

    def has_loop(self,x,y):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                if self.matrix[x][y] == x:
                    return True
        return False

    def get_edge(self, x,y):
        return self.matrix[x][y]

    def has_edge(self, x,y):
        return self.matrix[x][y] > 0

    def is_oriented(self, x, y ):
        return self.has_edge(x,y) and not self.has_edge(y,x)


    def print_graph(self):
        print("    "+"  ".join(f"{c}" for c in range(self.n)))
        print("  +"+"---" * self.n)
        for r in range(self.n):
            row_str = " ".join(f"{self.matrix[r][c]}"for c in range(self.n))
            print(f"{r} | {row_str}")
    

