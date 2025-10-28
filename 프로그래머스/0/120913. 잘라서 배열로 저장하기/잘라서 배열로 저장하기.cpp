#include <string>
#include <vector>

using namespace std;

vector<string> solution(string my_str, int n) {
    vector<string> answer;
    string tmp;
    for (int i=0; i<my_str.size(); i++) {
        tmp.push_back(my_str[i]);
        if ((i+1)%n == 0) {
            answer.push_back(tmp);
            tmp = "";            
        }
    }
    if (tmp != "") {
        answer.push_back(tmp);
    }
    return answer;
}