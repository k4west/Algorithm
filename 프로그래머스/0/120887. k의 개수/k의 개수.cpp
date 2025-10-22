#include <string>
#include <vector>

using namespace std;

int solution(int i, int j, int k) {
    int answer = 0;
    int x;
    for (int num=i; num<=j; num++) {
        x = num;
        while (x > 0) {
            if (x%10 == k) 
                answer++;
            x /= 10;
        }
    }
    return answer;
}