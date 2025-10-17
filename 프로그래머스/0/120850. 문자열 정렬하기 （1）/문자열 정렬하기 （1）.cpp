#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(string my_string) {
    vector<int> answer;
    string nums = "0123456789";
    for (char s: my_string) {
        if (nums.find(s) != string::npos) {
            answer.push_back(s - '0');
        }
    }
    sort(answer.begin(), answer.end());
    return answer;
}