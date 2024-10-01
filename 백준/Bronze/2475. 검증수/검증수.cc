#include <iostream>
using namespace std;

int main() 
{ 
    int s, t, i;
    s = 0;
    for (i=0; i<5; i++){
        cin >> t;
        s += t*t;
    }
    cout << s%10;
}