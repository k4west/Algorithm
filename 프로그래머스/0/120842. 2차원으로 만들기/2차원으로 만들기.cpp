#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<int> num_list, int n) {
    int m = num_list.size();
    vector<vector<int>> answer(m/n + ((m%n > 0) ? 1 : 0));
    for (int i = 0; i < m; i++) {
        answer[i/n].push_back(num_list[i]);
    }
    return answer;
}