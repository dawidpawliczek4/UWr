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

// stan dfsa
struct State {
    int current; //aktualny wierzcholek (czyli lacznik)
    vector<Kostka> path; //chodnik
    unordered_map<int, vector<Kostka> > graph_state;
};

bool znajdzChodnikDFS() {
    return true;
}


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

    unordered_map<int, vector<Kostka> > graf;

    for (const auto &k : wwszystkie_kostki) {
        graf[k.l].push_back(k);
    }

    stack<State> s;

    State f = {0, vector<Kostka>(), graf};
    s.push(f);
    bool found = false;
    vector<Kostka> res;

    while (!s.empty()) {
        State current_st = s.top();
        s.pop();

        if (!current_st.path.empty() && current_st.current == 0) {
            res = current_st.path;
            found = true;
            break;
        }

        if (current_st.graph_state.find(current_st.current) == current_st.graph_state.end()
            || current_st.graph_state[current_st.current].empty()
        ) {
            continue;
        }


        vector<Kostka> edges = current_st.graph_state[current_st.current];

        for (auto i = 0; i < edges.size(); i++) {
            Kostka k = edges[i];

            auto new_graph = current_st.graph_state;
            auto &edge_lst = new_graph[current_st.current];
            edge_lst.erase(edge_lst.begin() + i);

            vector<Kostka> new_path = current_st.path;
            new_path.push_back(k);

            State new_st = { k.r, new_path, new_graph };
            s.push(new_st); 
        }
    }

    if (found) {
        cout << res.size() << endl;

        for (auto &k : res) {
            cout << k.l << " " << k.m << " " << k.r << endl;
        }
    } else {
        cout << "BRAK";
    }
    return 0;
}
