#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array) {
    auto it = max_element(array.begin(), array.end());
    int max_value = *it;
    int index = distance(array.begin(), it);
    return {max_value, index};
}