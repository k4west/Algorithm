# include <iostream>
using namespace std;

int main() {
    int s = 0;
    int i, j;
    string n;
    cin >> n;
    for (i=0; i<16; i++) {
        j = n[i] - '0';
        if (i%2==0) {
            j *= 2;
        }
        s += j%10 + j/10;
    }
    if (s%10==0) {
        cout << "DA";
    } else {
        cout << "NE";
    }
    return 0;
}