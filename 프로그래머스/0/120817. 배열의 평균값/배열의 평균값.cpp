#include <string>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    int sm = 0;
    for (int value: numbers) {
        sm += value;
    }
    double answer = (double)sm/numbers.size();
    return answer;
}