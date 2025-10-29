#include <string>
#include <vector>

using namespace std;

string solution(vector<string> id_pw, vector<vector<string>> db) {
    string answer = "";
    string id = id_pw[0];
    string pw = id_pw[1];
    for (vector<string> dt: db) {
        if (id_pw == dt) return "login";
        else if (id == dt[0]) return "wrong pw";
    }
    return "fail";
    return answer;
}