#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string letter) {
    string answer = "";
    answer.reserve(my_string.size());
    for (char s: my_string) {
        if (s == letter[0]) continue;
        answer += s;
    }
    return answer;
}