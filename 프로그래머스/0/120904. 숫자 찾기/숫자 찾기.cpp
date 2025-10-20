#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int num, int k) {
    int answer = 0;
    vector<int> digits;
    while (num > 0) {
        digits.push_back(num%10);
        num /= 10;
    }
    reverse(digits.begin(), digits.end());
    for (int i=0; i < digits.size(); i++) {
        if (digits[i] == k) {
            return i+1;
        }
    }
    return -1;
}