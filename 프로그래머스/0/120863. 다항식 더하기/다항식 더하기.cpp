#include <string>
#include <vector>
#include <sstream>

using namespace std;

string solution(string polynomial) {
    string answer = "";
    int x=0, n=0;
    size_t i=0;
    istringstream ss(polynomial);
    string t;
    while (ss >> t) {
        if (t == "+") continue;
        
        i = t.size();
        if (t[i-1] == 'x') {
            if (i==1) x += 1;
            else {
                x += stoi(t.substr(0, i-1));
            }
        } else n += stoi(t);
    }
    if (x) {
        if (x == 1) answer += "x";
        else answer += to_string(x)+"x";
        
        if (n) answer += " + " + to_string(n);
    } else if (n) answer += to_string(n);
    if (answer.empty()) answer = "0";
    return answer;
}