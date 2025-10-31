#include <string>
#include <vector>

using namespace std;

int solution(string A, string B) {
    size_t m = A.size();
    for (size_t i=0; i<m; i++){
        if (A==B) return i;
        A = A[m-1] + A.substr(0, m-1);
    }
    return -1;
}