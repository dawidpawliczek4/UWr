#include <iostream>
#include <vector>
typedef long long ll;
using namespace std;

struct Kostka {
    int l;
    int m;
    int r;
};

bool znajdzChodnikBT(vector<Kostka> available, int current, vector<Kostka>& path) {
    if (!path.empty() && current == 0) {
        return true;
    }
        
    for (size_t i = 0; i < available.size(); ++i) {
        if (available[i].l == current) {            
            Kostka k = available[i];

            path.push_back(k);
                        
            available.erase(available.begin() + i);
                        
            if (znajdzChodnikBT(available, k.r, path)) {
                return true;
            }            

            path.pop_back();
        }
    }
    
    return false;
}

int main() {
    vector<Kostka> wwszystkie_kostki;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int l, m, r;
        cin >> l >> m >> r;
        Kostka k = {l, m, r};
        wwszystkie_kostki.push_back(k);
    }

    vector<Kostka> chodnik;
    if (znajdzChodnikBT(wwszystkie_kostki, 0, chodnik)) {        
        cout << chodnik.size() << endl;
        for (const auto& k : chodnik) {            
            cout << k.l << " " << k.m << " " << k.r << endl;
        }
    } else {
        cout << "BRAK" << endl;
    }
    
    return 0;
}
