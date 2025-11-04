#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board) {
    int answer = 0;
    vector<vector<int>> D = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    int n = board.size(), nr, nc;
    for (int r=0; r<n; r++) {
        for (int c=0; c<n; c++) {
            if (board[r][c] == 1) {
                for (auto& d: D) {
                    nr = r+d[0];
                    nc = c+d[1];
                    if (0 <= nr && nr < n && 0 <= nc && nc < n && board[nr][nc] == 0) {
                        board[nr][nc] = 2;
                    }
                }
            }
        }
    }
    for (int r=0; r<n; r++) {
        for (int c=0; c<n; c++) {
            if (board[r][c] == 0) answer++;
        }
    }
    return answer;
}