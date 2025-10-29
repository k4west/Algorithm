#include <string>
#include <vector>

using namespace std;

int solution(int balls, int share) {
    long double answer = 1;
    for (int i=0; i<share; i++) {
        answer *= balls-i;
        answer /= i+1;
    }
    return (int) answer;
}