#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1;
    long f = 1;
    while (f <= n) {
        answer++;
        f *= answer;
    }
    return answer-1;
}