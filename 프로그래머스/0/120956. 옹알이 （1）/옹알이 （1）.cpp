#include <string>
#include <vector>

using namespace std;

int solution(vector<string> babbling) {
    int answer = 0;
    int idx;
    vector<string> candi = {"aya", "ye", "woo", "ma"};
    for (string s: babbling) {
        for (string c: candi) {
            int len = c.size();
            if ((idx = s.find(c, 0)) != string::npos) {
                s.replace(idx, len, "_");
            }
        }
        while ((idx = s.find("_", 0)) != string::npos) {
            s.replace(idx, 1, "");
        }
        if (s == "") answer++;
    }
    return answer;
}
