#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> array) {
    int max_v, max_idx;
    max_v = 0; max_idx = 0;
    for (int i = 0; i < array.size(); i++) {
        int value = array[i];
        if (max_v < value) {
            max_v = value;
            max_idx = i;
        }
    }
    return {max_v, max_idx};
}