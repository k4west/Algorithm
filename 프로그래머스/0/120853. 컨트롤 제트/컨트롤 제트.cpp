#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string s) {
    int answer = 0;
    stringstream ss(s);
    vector<int> v;
    v.reserve(s.size());
    
    string tmp = "0";
    int t;
    while (ss >> tmp) {
        if (tmp == "Z") {
            if(!v.empty()) {
                v.pop_back();
            }
        }
        else {
            t = stoi(tmp);
            v.push_back(t);
        }
    }
    for (int n: v) {
        answer += n;
    }
    return answer;
}