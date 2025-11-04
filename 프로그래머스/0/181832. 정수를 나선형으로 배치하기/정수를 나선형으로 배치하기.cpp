#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(int n) {
    vector<vector<int>> D = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    vector<int> tmp(n, 0);
    vector<vector<int>> answer(n, tmp);
    int r=0, c=-1, d=0, num=1;
    
    for (int i=0; i<2*n-1; i++) {
        for (int j=0; j<n-(i+1)/2; j++) {
            r += D[d][0];
            c += D[d][1];
            answer[r][c] = num;      
            num++;
        }
        d = (d+1)%4;
    }
    return answer;
}