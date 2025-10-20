#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    answer.reserve(numbers.size());
    for (int num: numbers) {
        answer.push_back(num*2);
    }
    return answer;
}