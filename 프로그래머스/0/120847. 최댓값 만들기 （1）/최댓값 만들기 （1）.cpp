#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    for (int i = 0; i < numbers.size(); i++) {
        int a = numbers[i];
        for (int j = i+1; j < numbers.size(); j++) {
            int b = a * numbers[j];
            if (answer < b) {
                answer = b;
            }
        }
    }
    return answer;
}