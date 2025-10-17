#include <string>
#include <vector>

using namespace std;

string solution(string rsp) {
    string answer = "";
    for (char value: rsp) {
        if (value == '0') answer += '5';
        else if (value == '2') answer += '0';
        else if (value == '5') answer += '2';
    }
    return answer;
}