#include <unordered_set>
#include <string>
#include <vector>

using namespace std;

int solution(vector<string> s1, vector<string> s2) {
    unordered_set<string> set1 = unordered_set(s1.begin(), s1.end());
    int answer = 0;
    for (string a: s2) {
        if (set1.count(a)) answer++;
    }
    return answer;
}