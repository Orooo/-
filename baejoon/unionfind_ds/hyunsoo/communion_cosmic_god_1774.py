import math
# Union-Find Disjoint Sets Library written in OOP manner
# using both path compression and union by rank heuristics


class UnionFind:                                # OOP style
    def __init__(self, N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.setSize = [1 for i in range(N)]
        self.numSets = N

    def findSet(self, i):
        if (self.p[i] == i):
            return i
        else:
            self.p[i] = self.findSet(self.p[i])
            return self.p[i]

    def isSameSet(self, i, j):
        return self.findSet(i) == self.findSet(j)

    def unionSet(self, i, j):
        if (self.isSameSet(i, j)):
            return

        self.numSets -= 1
        x = self.findSet(i)
        y = self.findSet(j)
        # rank is used to keep the tree short
        if (self.rank[x] > self.rank[y]):
            self.p[y] = x
            self.setSize[x] += self.setSize[y]
        else:
            self.p[x] = y
            self.setSize[y] += self.setSize[x]
            if (self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def numDisjointSets(self):
        return self.numSets

    def sizeOfSet(self, i):
        return self.setSize[self.findSet(i)]


def calcDist(u, v, points):
    return math.sqrt((points[u][0] - points[v][0]) ** 2 + (points[u][1] - points[v][1]) ** 2)


def main():
    V, E = map(int, input().split(" "))
    # Kruskal's algorithm
    points = []
    for _ in range(V):
        x, y = map(int, input().split())  # read as (x, y) 좌표
        points.append([x, y])

    # 각 정정간의 거리 및 정점쌍을 엣지 리스트에 추가
    EL = []
    for i in range(V):
        for j in range(i+1, V):
            w = calcDist(i, j, points)            # 각 정정간의 거리 계산
            EL.append((w, i, j))                    # reorder as (w, u, v)
    EL.sort()                                       # sort by w, O(E log E)

    mst_cost = 0
    num_taken = 0
    UF = UnionFind(V)                               # all V are disjoint sets

    for _ in range(E):
        u, v = map(int, input().split())
        UF.unionSet(u-1, v-1)                           # 입력 받은 이미 연결된 통로는 합쳐줌

    for el in EL:                              # for each edge, O(E)
        if num_taken == V-1:
            break
        w, u, v = el
        if (not UF.isSameSet(u, v)):                # check
            num_taken += 1                          # 1 more edge is taken
            mst_cost += w                           # add w of this edge
            UF.unionSet(u, v)                       # link them
            # note: the runtime cost of UFDS is very light

    # note: the number of disjoint sets must eventually be 1 for a valid MST
    # print("MST cost = {:.2f} (Kruskal's)".format(mst_cost))
    print("{:.2f}".format(mst_cost))


main()
