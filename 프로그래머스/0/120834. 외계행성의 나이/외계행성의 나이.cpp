#include <string>
#include <vector>

using namespace std;

string solution(int age) {
    string alpha = "abcdefghij";
    string answer = "";
    for (char s: to_string(age)) {
        answer += alpha[s-'0'];
    }
    return answer;
}