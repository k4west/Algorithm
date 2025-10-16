#include <cmath>
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    double r = sqrt(n);
    for (int i = 1; i <= r; i++) {
        if (n%i == 0) {
            answer++;
            if (i != r) {
                answer++;
            }
        }      
    }
    return answer;
}