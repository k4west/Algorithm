#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    int n = numbers.size();
    sort(numbers.begin(),numbers.end());
    answer = max(numbers[0]*numbers[1], numbers[n-1]*numbers[n-2]);
    return answer;
}