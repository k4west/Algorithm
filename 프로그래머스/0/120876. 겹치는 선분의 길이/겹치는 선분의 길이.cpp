#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> lines) {
    int answer = 0;
    vector<int> cnt(200, 0);
    for (vector<int>& line: lines) {
        for (int n=line[0]; n<line[1]; n++) {
            cnt[n+100]++;
        }
    }
    for (int& n: cnt) {
        if (n > 1) answer++;
    }
    return answer;
}