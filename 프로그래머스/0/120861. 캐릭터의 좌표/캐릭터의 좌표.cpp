#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> keyinput, vector<int> board) {
    vector<int> answer = {0, 0};
    int w = board[0]/2;
    int h = board[1]/2;
    for (string key : keyinput) {
        if (key == "up") {
            if (answer[1] + 1 <= h) {
                answer[1]++;
            }
        } else if (key == "down") {
            if (answer[1] - 1 >= -h) {
                answer[1]--;
            }
        } else if (key == "left") {
            if (answer[0] - 1 >= -w) {
                answer[0]--;
            }
        } else if (key == "right") {
            if (answer[0] + 1 <= w) {
                answer[0]++;
            }
        }
    }
    return answer;
}