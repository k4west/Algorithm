#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers, string direction) {
    vector<int> answer;
    size_t n = numbers.size();
    answer.reserve(n);
    if (direction == "right") {
        n--;
        answer.push_back(numbers[n]);
        for (int i=0; i < n; i++) {
            answer.push_back(numbers[i]);
        }
    } else {
        for (int i=1; i < n; i++) {
            answer.push_back(numbers[i]);
        }
        answer.push_back(numbers[0]);
    }
    return answer;
}