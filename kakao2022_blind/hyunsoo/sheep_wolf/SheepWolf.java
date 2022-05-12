package kakao2022_blind.sheep_wolf;

import java.util.*;

class Solution {
    int[] _left = new int[20];
    int[] _right = new int[20];
    int[] _info = new int[20];
    int _n;
    int _answer = 1;
    boolean[] visited = new boolean[1 << 17];

    // 상태에 대한 dfs 함수
    void dfs(int state) {
        if (visited[state] == true)
            return;
        visited[state] = true;
        int wolfNum = 0, nodeNum = 0;
        for (int i = 0; i < _n; i++) {
            if ((state & (1 << i)) != 0) {
                nodeNum++;
                wolfNum += _info[i];
            }
        }

        // 만약 늑대가 절반 이상일 경우 방문할 수 없는 상태이니 종료
        if (2 * wolfNum >= nodeNum)
            return;
        // 현재 state의 양의 수가 answer보다 클 경우 answer를 갱신
        _answer = Math.max(_answer, nodeNum - wolfNum);
        // 이제 다음 상태로 넘어갈 시간
        for (int i = 0; i < _n; i++) {
            // i번째 비트가 꺼져있는 경우 해당 정점이 없으니 넘어감
            if ((state & (1 << i)) == 0)
                continue;
            // 현재 보고 있는 i번째 정점의 _left가 있다면
            if (_left[i] != -1)
                dfs(state | (1 << _left[i]));
            if (_right[i] != -1)
                dfs(state | (1 << _right[i]));
        }
    }

    public int solution(int[] info, int[][] edges) {
        _n = info.length;
        Arrays.fill(_left, -1);
        Arrays.fill(_right, -1);
        for (int i = 0; i < _n; i++)
            _info[i] = info[i];
        for (int i = 0; i < _n - 1; i++) {
            int parent = edges[i][0];
            int child = edges[i][1];
            if (_left[parent] == -1)
                _left[parent] = child;
            else
                _right[parent] = child;
        }
        dfs(1); // 0번 노드만 포함된 상태에서 dfs 시작
        return _answer;
    }
}

public class SheepWolf {
    public static void main(String[] args) {
        int[] info = { 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1 };
        int[][] edges = { { 0, 1 }, { 1, 2 }, { 1, 4 }, { 0, 8 }, { 8, 7 }, { 9, 10
        }, { 9, 11 }, { 4, 3 }, { 6, 5 },
                { 4, 6 }, { 8, 9 } };
        Solution so = new Solution();
        System.out.println(so.solution(info, edges));
    }
}
