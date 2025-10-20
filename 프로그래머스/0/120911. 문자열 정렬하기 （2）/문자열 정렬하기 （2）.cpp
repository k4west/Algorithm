#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    vector<int> li(26);
    for (char s: my_string) {
        s = tolower(s);
        int idx = s - 'a';
        li[idx]++;
    }
    for (int i = 0; i < 26; i++) {
        char s = i+'a';
        int cnt = li[i];
        for (int j = 0; j < cnt; j++) {
            answer += s;
        }
    }
    
    return answer;
}