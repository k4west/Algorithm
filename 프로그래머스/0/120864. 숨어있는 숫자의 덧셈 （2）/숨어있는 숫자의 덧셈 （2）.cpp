#include <string>
#include <vector>
#include <cctype>
#include <sstream>

using namespace std;

int solution(string my_string) {
    string tmp;
    tmp.reserve(my_string.size());
    
    for (char s: my_string) {
        if (isdigit(s)) tmp.push_back(s);
        else tmp.push_back(' ');
    }
    
    int answer = 0, num;
    stringstream ss(tmp);
    while (ss >> num) answer += num;
    return answer;
}