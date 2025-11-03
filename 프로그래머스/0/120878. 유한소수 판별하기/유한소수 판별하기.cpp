#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int c = 1, d = b;
    while (b){
        c = a%b;
        a = b;
        b = c;
    }
    d /= a;
    while (d%2 ==0) {
        d >>= 1;
    }
    while (d%5 ==0) {
        d /= 5;
    }
    return d == 1 ? 1 : 2;
}