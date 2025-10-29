#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<string> spell, vector<string> dic) {
    int answer = 0;
    int len = spell.size();
    sort(spell.begin(), spell.end());
    string str;
    for (string c : spell) str += c;
    for (string s: dic) {
        if (s.size() == len) {
            sort(s.begin(), s.end());
            if (s == str) return 1;
        }
    }
    return 2;
}