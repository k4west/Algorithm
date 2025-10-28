#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    vector<int> st;
    istringstream ss(my_string);
    string tmp;
    int sign = 1;
    while (ss >> tmp) {
        if (isdigit(tmp[0])) {
            st.push_back(stoi(tmp)*sign);
            sign = 1;
        } else if (tmp == "-") {
            sign = -1;
        }
    }
    for (int num: st) answer += num;
    return answer;
}