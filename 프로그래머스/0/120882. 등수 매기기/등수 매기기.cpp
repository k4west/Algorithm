#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<vector<int>> score) {
    vector<int> answer;
    vector<int> summed;
    vector<int> ordered;
    
    size_t n = score.size();
    summed.reserve(n);
    ordered.reserve(n);
    
    for (vector<int>& s: score) summed.push_back(s[0]+s[1]);
    ordered = summed;
    sort(ordered.begin(), ordered.end(), greater<int>());
    
    for (int s: summed) answer.push_back(find(ordered.begin(), ordered.end(), s)-ordered.begin()+1);
    return answer;
}