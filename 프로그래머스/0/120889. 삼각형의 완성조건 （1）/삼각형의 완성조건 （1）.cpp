#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> sides) {
    int answer = 0;
    int sm = sides[0] + sides[1] + sides[2];
    int max_side = *max_element(sides.begin(), sides.end());
    if (sm > max_side * 2) {
        answer = 1;
    } else {
        answer = 2;
    }
    return answer;
}