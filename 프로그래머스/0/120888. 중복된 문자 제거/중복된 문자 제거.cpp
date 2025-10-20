#include <string>
#include <vector>
#include <set>

using namespace std;

string solution(string my_string) {
    string answer = "";
    set<char> charset;
    for (char s: my_string) {
        if (charset.count(s)) continue;
        charset.insert(s);
        answer += s;
    }
    return answer;
}