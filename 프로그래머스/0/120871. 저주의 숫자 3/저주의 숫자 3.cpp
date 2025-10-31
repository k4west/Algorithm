#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int num=0;
    string str_num;
    while (n) {
        num++;
        str_num = to_string(num);
        if (num%3 == 0 || str_num.find('3') != string::npos) continue;
        n--;
    }
    return num;
}