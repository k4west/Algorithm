#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = n/7 + (n%7 > 0 ? 1 : 0);
    return answer;
}