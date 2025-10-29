#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

long long solution(string numbers) {
    long long answer = 0;
    unordered_map<string, int> d = {
        {"one", 1}, {"two", 2}, {"three" , 3}, 
        {"four" , 4}, {"five" , 5}, {"six" , 6}, 
        {"seven" , 7}, {"eight" , 8}, {"nine", 9},
        {"zero", 0}
    };
    string tmp;
    for (char s: numbers) {
        tmp += s;
        auto it = d.find(tmp);
        if (it != d.end()) {
            tmp = "";
            answer = answer*10 + it->second;
        }
    }
    return answer;
}