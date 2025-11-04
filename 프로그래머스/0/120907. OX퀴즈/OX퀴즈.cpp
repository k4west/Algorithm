#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<string> solution(vector<string> quiz) {
    vector<string> answer;
    string X, Y, Z, op;
    for (string formula: quiz) {
        istringstream iss(formula);
        iss >> X >> op >> Y >> Z >> Z;
        if (op == "+") stoi(X) + stoi(Y) == stoi(Z) ? answer.push_back("O") : answer.push_back("X");
        else stoi(X) - stoi(Y) == stoi(Z) ? answer.push_back("O") : answer.push_back("X");
    }
    return answer;
}