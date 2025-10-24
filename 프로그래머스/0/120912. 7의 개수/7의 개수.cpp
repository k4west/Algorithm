#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    for (int n : array) {
        for (char s: to_string(n)) {
            if (s == '7') answer++;
        }
    }
    return answer;
}