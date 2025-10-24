#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int solution(vector<int> array, int n) {
    int answer = array[0];
    sort(array.begin(), array.end());
    int dist = abs(n-array[0]);
    for (int num: array) {
        int diff = abs(n-num);
        if (dist > diff) {
            dist = diff;
            answer = num;
        }
    }
    return answer;
}