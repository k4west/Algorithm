#include <string>
#include <vector>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    for (char s: my_string) {
        if (isdigit(s)) answer += s - '0';
    }
    return answer;
}