from sys import stdin, stdout


class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * (n)
        self.sizes = [1] * (n)
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]


class Log:
    def __init__(self, idx, x1, x2, y):
        self.idx = idx
        self.x1 = x1
        self.x2 = x2
        self.y = y


def print_parents(logs, parents):
    for i in range(len(logs)):
        print("i: ", i, "parent: ", parents[i])


def print_logs(logs):
    for log in logs:
        print("log: ",
              log.idx, log.x1, log.x2, log.y)


def main():
    n, q = [int(i) for i in stdin.readline().split(' ')]
    u = UFDS(n)
    logs = []
    for i in range(n):
        x1, x2, y = stdin.readline().split()
        logs.append(Log(int(i), int(x1), int(x2), int(y)))

    # 통나무의 x1 좌표를 기준으로 오름차순 정렬
    logs = sorted(logs, key=lambda log: log.x1)

    # 해당 통나무의 x좌표 범위 안에 다른 통나무의 x1좌표가 들어오면 합치기를 시도, 아니면 다음 통나무를 검사
    for i in range(len(logs)):
        for j in range(i+1, len(logs)):
            if logs[i].x1 <= logs[j].x1 and logs[i].x2 >= logs[j].x1:
                u.union(logs[i].idx, logs[j].idx)
            else:
                break

    for _ in range(q):
        a, b = stdin.readline().split()
        stdout.write("1\n" if u.find(int(a)-1) == u.find(int(b)-1) else "0\n")

    # print_parents(logs, u.parents)

main()
