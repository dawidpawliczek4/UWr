#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

unordered_set<string> forbidden;
bool validColoring(int prev1,int prev2,int newCol);

int main() {

    int n, p, m;
    cin >> n >> p >> m;

    for (int i = 0; i < p; i++) {
        string s1, s2, s3;
        cin >> s1 >> s2 >> s3;
        forbidden.insert(s1 + s2 + s3);
    }

    vector<vector<int>> dp(32, vector<int>(32,0));

    for (int prev1 = 0; prev1 < 32; prev1++) {
        for (int prev2 = 0; prev2 < 32; prev2++) {
            dp[prev1][prev2] = 1;
        }
    }

    for (int i = 3; i <= n; i++) {
        vector<vector<int>> newDp (32, vector<int>(32,0));

        for (int prev1 = 0; prev1 < 32; prev1++) {
            for (int prev2 = 0; prev2 < 32; prev2++) {
                int poprawne = dp[prev1][prev2];
                if (poprawne) {
                    for (int newCol = 0; newCol < 32; newCol++) {
                        if (validColoring(prev1, prev2, newCol)) {
                            newDp[prev2][newCol] = (newDp[prev2][newCol] + poprawne) % m;
                        }
                    }
                }
            }
        }
        dp = newDp;
    }

    long long res = 0;
    for (int prev1 = 0; prev1 < 32; prev1++) {
        for (int prev2 = 0; prev2 < 32; prev2++) {
            res = (res + dp[prev1][prev2]) % m;
        }
    }

    cout << res << endl;
}
    
bool validColoring(int prev1,int prev2,int newCol) {
    for (int start = 0; start < 3; start++) {
        string block;
        for (int i = start; i < start + 3; i++) {
            char c1 = ((prev1 >> i) & 1) ? 'x' : '.';
            char c2 = ((prev2 >> i) & 1) ? 'x' : '.';
            char c3 = ((newCol >> i) & 1) ? 'x' : '.';
            block.push_back(c1);
            block.push_back(c2);
            block.push_back(c3);
        }
        if (forbidden.find(block) != forbidden.end()) {
            return false;
        }
    }
    return true;
}