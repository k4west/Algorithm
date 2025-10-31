#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> dots) {
    int xmin=256, xmax=-256, ymin=256, ymax=-256;
    for (vector<int> xy: dots) {
        int a=xy[0], b=xy[1];
        if (xmin > a) xmin = a;
        if (xmax < a) xmax = a;
        if (ymin > b) ymin = b;
        if (ymax < b) ymax = b;
    }
    return (xmax-xmin)*(ymax-ymin);
}