#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>

using namespace std;

struct Kostka {
    int l;
    int m;
    int r;
};

struct Frame {
    int v;
    int nextIdx;
    int blockUsed;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<Kostka> wwszystkie_kostki(n);

    for (int i = 0; i < n; i++) {
        int l, m, r;
        cin >> l >> m >> r;
        Kostka k = {l, m, r};
        wwszystkie_kostki[i] = k;
    }

    vector<vector<int> > graf(10001);

    for (int i = 0; i < n; i++) {
        graf[wwszystkie_kostki[i].l].push_back(i);
    }

    vector<bool> used(n, false);
    vector<Frame> s;

    Frame init_frame = {0,0,-1};
    s.push_back(init_frame);
    
    bool found = false;

    while (!s.empty()) {
        Frame &top = s.back();

        if (top.v == 0 && s.size() > 1) {
            found = true;
            break;
        }

        if (top.nextIdx < graf[top.v].size()) {
            int blockIdx = graf[top.v][top.nextIdx];
            top.nextIdx++;
            if (!used[blockIdx]) {
                used[blockIdx] = true;
                Frame new_frame = {wwszystkie_kostki[blockIdx].r , 0, blockIdx};
                s.push_back(
                    new_frame
                );
            }
        } else {
            Frame popped = s.back();
            s.pop_back();
            if (popped.blockUsed != -1 ) {
                used[popped.blockUsed] = false;
            }
        }

    }

    if (found) {
        vector<int> res;
        for (size_t i = 1; i < s.size(); i ++) {
            res.push_back(s[i].blockUsed);
        }
        cout << res.size() << endl;
        for (int idx : res) {
            cout << wwszystkie_kostki[idx].l << " " << wwszystkie_kostki[idx].m << " " << wwszystkie_kostki[idx].r << endl;
        }
    } else {
        cout << "BRAK";
    }
    return 0;
}
