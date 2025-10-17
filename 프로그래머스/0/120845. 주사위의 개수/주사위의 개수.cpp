#include <string>
#include <vector>

using namespace std;

int solution(vector<int> box, int n) {
    int answer = 1;
    
    for (int d: box) answer *= d/n;
    return answer;
}