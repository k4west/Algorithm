#include <cmath>
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int r = sqrt(n);
    if (r*r == n) return 1;
    return 2;
}