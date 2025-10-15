#include <string>
#include <vector>

using namespace std;

int solution(int n, int t) {
    int answer = n * (1 << t);
    return answer;
}