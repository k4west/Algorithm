#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<vector<int>> score) {
    vector<vector<int>> sm;    
    size_t n = score.size();
    int i = 0, rank = 1;
    sm.reserve(n);
    
    for (auto& s: score) {
        sm.push_back({s[0]+s[1], i});
        i++;
    }
    sort(sm.begin(), sm.end(), greater<vector<int>>());
    
    vector<int> answer(n);
    answer[sm[0][1]] = rank;
    for (int j=1; j < n; j++) {
        if (sm[j-1][0] > sm[j][0]) rank = j+1;
        answer[sm[j][1]] = rank;
    }
    return answer;
}