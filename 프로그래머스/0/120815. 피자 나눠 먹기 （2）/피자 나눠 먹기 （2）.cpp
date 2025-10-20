#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    if (n % 2 == 0) n /= 2;
    if (n % 3 == 0) n /= 3;
    return n;
}