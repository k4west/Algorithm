#include <string>
#include <vector>

using namespace std;

int solution(vector<int> sides) {
    int answer = sides[0]+sides[1] - abs(sides[0]-sides[1]) - 1;
    return answer;
}