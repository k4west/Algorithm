#include <string>
#include <vector>
#include <set>

using namespace std;

int solution(vector<int> array) {
    int answer = 0, maxCnt = 0;
    set<int> nums;
    vector<int> cnt(1001, 0);
    for (int& num: array) {
        cnt[num]++;
        nums.insert(num);
    }
    
    for (int num: nums) {
        if (maxCnt < cnt[num]) {
            maxCnt = cnt[num];
            answer = num;
        } else if (maxCnt == cnt[num]) answer = -1;
    }
    return answer;
}