#include <string>
#include <vector>

using namespace std;

int solution(int slice, int n) {
    int answer = n / slice + (n % slice > 0 ? 1 : 0);
    return answer;
}