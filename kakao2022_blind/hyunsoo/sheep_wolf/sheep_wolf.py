# https://www.youtube.com/watch?v=caGtdr3_nxs&t=1501s
# 양과 늑대

left = [-1] * 20
right = [-1] * 20
g_info = []
n = 0
answer = 1
visited = [0] * (1 << 17)


def DFS(state):
    global answer
    if visited[state]:
        return None
    visited[state] = 1
    wolf_num, node_num = 0, 0
    for i in range(n):
        if state & (1 << i):
            node_num += 1
            wolf_num += g_info[i]

    # 만약 늑대가 절반 이상일 경우 방문할 수 없는 상태이니 종료
    if 2*wolf_num >= node_num:
        return None
    # 현재 state의 양의 수가 answer보다 클 경우 answer를 갱신
    answer = max(answer, node_num - wolf_num)

    # 이제 다음 상태로 넘어갈 시간
    for i in range(n):
        if not state & (1 << i):
            continue
        # 현재 보고 있는 i번째 정점의 left가 있다면
        if left[i] != -1:
            DFS(state | (1 << left[i]))
        if right[i] != -1:
            DFS(state | (1 << right[i]))


def solution(info, edges):
    global n, g_info
    n = len(info)
    g_info = info
    for parent, child in edges:
        if left[parent] == -1:
            left[parent] = child
        else:
            right[parent] = child

    DFS(1)
    return answer


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [
    9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
# result = 5

# intfo = [0,1,0,1,1,0,1,0,0,1,0]
# edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
# resutl = 5

print(solution(info, edges))
