#include <string>
#include <vector>

using namespace std;

string solution(string cipher, int code) {
    string answer = "";
    int n = cipher.size();
    answer.reserve(n/code);
    for (int i=code-1; i < n; i+=code) {
        answer += cipher[i];
    }
    return answer;
}