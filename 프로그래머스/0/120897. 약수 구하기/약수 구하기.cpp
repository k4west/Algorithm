#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    answer.reserve(answer.size());
    int i = 1;
    while (i*i <= n) {
        if (n % i == 0) {
            answer.push_back(i);
            if (i*i < n) {
                answer.push_back(n/i);
            }
        }
        i++;
    }
    sort(answer.begin(), answer.end());
    return answer;
}