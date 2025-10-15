#include <string>
#include <vector>

using namespace std;

int solution(int slice, int n) {
    int answer = (n-1) / slice + 1;
    return answer;
}