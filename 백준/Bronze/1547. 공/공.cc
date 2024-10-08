#include <iostream>
using namespace std;

int main() {
    int k = 1;
    int i, n, a, b;
    cin >> n;
    for (i=0; i<n; i++) {
        cin >> a >> b;
        if (a == k){
            k = b;
        } else if (b==k){
            k = a;
        }
    }
    cout << k;
    return 0;
}