#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    if (n%2 == 0) {
        answer.push_back(2);
        do n/=2;
        while (n>0 and n%2==0);
    }
    for (int i=3; i<=n; i+=2) {
        if (n%i==0) {
            answer.push_back(i);
            do n/=i;
            while (n>0 and n%i==0);
        }
    }
    return answer;
}