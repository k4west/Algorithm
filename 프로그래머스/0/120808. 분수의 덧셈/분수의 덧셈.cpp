#include <string>
#include <vector>
#include <numeric>

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    int n = gcd(denom1, denom2);
    int num=(numer1*denom2 + numer2*denom1)/n, den=denom1*denom2/n;
    int m = gcd(num, den);
    
    return {num/m, den/m};
}