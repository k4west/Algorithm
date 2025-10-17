#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    answer.reserve(my_string.size());
    
    string vowel = "aeiou";
    for (char s: my_string) {
        if (vowel.find(s) == string::npos) answer += s;
    }
    return answer;
}