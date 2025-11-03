#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numlist, int n) {
    vector<int> answer;
    vector<vector<int>> diffs;
    
    size_t m = numlist.size();
    answer.reserve(m);
    diffs.reserve(m);
    
    for (int num: numlist) diffs.push_back({abs(n-num), -num});
    sort(diffs.begin(), diffs.end());
    for (auto& s: diffs) answer.push_back(-s[1]);
    return answer;
}