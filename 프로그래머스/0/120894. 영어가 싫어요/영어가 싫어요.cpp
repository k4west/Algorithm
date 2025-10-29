#include <string>
#include <vector>

using namespace std;

long long solution(string numbers) {
    long long answer = 0;
    vector<string> num = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int index;
    for (int i=0; i<10; i++) {
        while ((index = numbers.find(num[i])) != string::npos) {
            numbers.replace(index, num[i].size(), to_string(i));
        }
    }
    answer = stoll(numbers);
    return answer;
}