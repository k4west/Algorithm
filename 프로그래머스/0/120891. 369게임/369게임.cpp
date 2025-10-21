#include <string>
#include <vector>

using namespace std;

int solution(int order) {
    int answer = 0;
    string str = to_string(order);
    for (char s: str) {
        switch (s) {
            case '3':
                answer++;
                continue;
            case '6':
                answer++;
                continue;
            case '9':
                answer++;
        }
    }
    return answer;
}