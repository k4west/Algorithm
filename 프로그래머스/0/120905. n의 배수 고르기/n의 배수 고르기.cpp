#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, vector<int> numlist) {
    vector<int> answer;
    for (int value: numlist) {
        if (value % n == 0) {
            answer.push_back(value);
        }
    }
    return answer;
}