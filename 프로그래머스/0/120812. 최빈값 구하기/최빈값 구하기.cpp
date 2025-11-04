#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int solution(vector<int> array) {
    int answer = 0, maxCnt = 0, cnt=0;
    unordered_map<int, int> cnts;
    cnts.reserve(array.size());
    
    for (int& num: array) {
        cnt = ++cnts[num];
        if (maxCnt < cnt) {
            maxCnt = cnt;
            answer = num;
        } else if (maxCnt == cnt) answer = -1;
    }
    return answer;
}