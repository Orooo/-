#include <bits/stdc++.h>

using namespace std;

// 왼쪽 자식, 오른쪽 자식, 양/늑대 값
int left_[20], right_[20], g_info[20];
int n;
int answer = 1;
int visited[1 << 17]; // visited[x] : 상태 x를 방문했는가?

// 상태에 대한 DFS 함수
void DFS(int state)
{
    if (visited[state])
        return;
    visited[state] = 1;
    int wolf_num = 0, node_num = 0;
    for (int i = 0; i < n; i++)
    {
        if (state & (1 << i))
        {
            node_num++;
            wolf_num += g_info[i];
        }
    }

    // 만약 늑대가 절반 이상일 경우 방문할 수 없는 상태이니 종료
    if (2 * wolf_num >= node_num)
        return;
    // 현재 state의 양의 수가 ans보다 클 경우 ans를 갱신
    answer = max(answer, node_num - wolf_num);
    // 이제 다음 상태로 넘어갈 시간
    for (int i = 0; i < n; i++)
    {
        // i번째 비트가 꺼져있는 경우 해당 정점이 없으니 넘어감
        if (!(state & (1 << i)))
            continue;
        // 현재 보고 있는 i번째 정점의 left가 있다면
        if (left_[i] != -1)
            DFS(state | (1 << left_[i]));
        // 현재 보고 있는 i번째 정점의 right가 있다면
        if (right_[i] != -1)
            DFS(state | (1 << right_[i]));
    }
}

int solution(vector<int> info, vector<vector<int>> edges)
{
    n = info.size();
    fill(left_, left_ + n, -1);
    fill(right_, right_ + n, -1);
    for (int i = 0; i < n; i++)
        g_info[i] = info[i];
    for (int i = 0; i < n - 1; i++)
    {
        int parent = edges[i][0];
        int child = edges[i][1];
        if (left_[parent] == -1)
            left_[parent] = child;
        else
            right_[parent] = child;
    }
    DFS(1); // 0번 노드만 포함된 상태에서 dfs 시작
    return answer;
}

int main(void)
{
    vector<int> info = {0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1};
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {1, 4}, {0, 8}, {8, 7}, {9, 10}, {9, 11}, {4, 3}, {6, 5}, {4, 6}, {8, 9}};
    cout << solution(info, edges) << '\n';
    return 0;
}