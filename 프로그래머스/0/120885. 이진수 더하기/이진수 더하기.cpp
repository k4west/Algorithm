#include <string>
#include <vector>

using namespace std;

string solution(string bin1, string bin2) {
    string answer = "";
    int n1 = bin1.size() - 1;
    int n2 = bin2.size() - 1;
    
    bool carry = false, s1 = false, s2 = false;
    string r;
    while (n1 >= 0 or n2 >= 0) {
        s1 = n1 >= 0 and bin1[n1] == '1';
        s2 = n2 >= 0 and bin2[n2] == '1';
        if (s1 and s2) {
            if (carry) {
                r.push_back('1');
            } else {
                r.push_back('0');
                carry = true;
            }
        } else if (!s1 and !s2) {
            if (carry) {
                r.push_back('1');
                carry = false;
            } else {
                r.push_back('0');
            }
        } else {
            if (carry) {
                r.push_back('0');
                carry = true;
            } else {
                r.push_back('1');
            }
        }
        n1--;
        n2--;
    }
    if (carry) r.push_back('1');
    for (int i = r.size()-1; i >= 0; i--) {
        answer.push_back(r[i]);
    }
    return answer;
}