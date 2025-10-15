#include <string>
#include <vector>

using namespace std;

int solution(vector<string> s1, vector<string> s2) {
    int answer = 0;
    for (string a1: s1) {
        for (string a2: s2) {
            if (a1 == a2) {
                answer += 1;
                break;
            }
        }
    }
    return answer;
}