#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> emergency) {
    vector<int> answer;
    vector<int> order;
    int M = emergency.size();
    order.reserve(M);
    for (int n : emergency) order.push_back(-n);
    sort(order.begin(), order.end());
    for (int i = 0; i < M; i++) {
        int j = find(order.begin(), order.end(), -emergency[i]) - order.begin();
        answer.push_back(j+1);
    }
    
    return answer;
}