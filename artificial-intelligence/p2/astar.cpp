#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <set>
#include <cstdlib>
#include <climits>

using namespace std;
using Position = pair<int, int>;

void canonicalize_state(vector<Position>& state) {
    sort(state.begin(), state.end());
    state.erase(unique(state.begin(), state.end()), state.end());
}

int bfs_heuristic(const vector<string>& spec, const Position& state) {
    vector<Position> directions = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
    queue<pair<Position, int>> q;
    q.push({state, 0});

    vector<vector<bool>> visited(spec.size(), vector<bool>(spec[0].size(), false));

    visited[state.first][state.second] = true;

    while (!q.empty()) {
        auto st = q.front();
        q.pop();
        int x = st.first.first;
        int y = st.first.second;
        int dist = st.second;

        char curr = spec[x][y];
        if (curr == 'G' || curr == 'B') {
            return dist;
        }

        for (const auto& d: directions) {
            int newx = x + d.first;
            int newy = y + d.second;

            if (newx >= 0 && newx < spec.size() && newy >= 0 && newy < spec[0].size() &&
            spec[newx][newy] != '#' && !visited[newx][newy]) {
                q.push({{newx, newy}, dist+1});
                visited[newx][newy] = true;
            }
        }
    }   
    return 99999999;
}

int better_heuristic(const vector<string>& spec, const vector<Position>& state, vector<vector<int>>& memoized) {
    int max_val = 0;
    for (auto &pos : state) {
        int dist;
        if (memoized[pos.first][pos.second] != -1) {
            dist = memoized[pos.first][pos.second];
        }  else {
        dist = bfs_heuristic(spec, pos);
        memoized[pos.first][pos.second] = dist;
        }
        if (dist > max_val) {
            max_val = dist;
        }
    }
    return max_val;
}

int heuristic(const vector<Position>& state, const vector<Position>& goals) {
    int h = 0;
    for (const auto& pos : state) {
        int min_dist = INT_MAX;
        for (const auto& goal : goals) {
            int dist = abs(pos.first - goal.first) + abs(pos.second - goal.second);
            min_dist = min(min_dist, dist);
        }
        h = max(h, min_dist);
    }
    return h;
}

vector<Position> do_move(const vector<string>& spec, const vector<Position>& state, char move) {
    vector<Position> new_state;
    int rows = spec.size();
    int cols = spec[0].size();
    for (auto pos : state) {
        int x = pos.first, y = pos.second;
        int nx = x, ny = y;
        if (move == 'U' && x - 1 >= 0 && spec[x - 1][y] != '#')
            nx = x - 1;
        else if (move == 'D' && x + 1 < rows && spec[x + 1][y] != '#')
            nx = x + 1;
        else if (move == 'L' && y - 1 >= 0 && spec[x][y - 1] != '#')
            ny = y - 1;
        else if (move == 'R' && y + 1 < cols && spec[x][y + 1] != '#')
            ny = y + 1;
        new_state.push_back({nx, ny});
    }
    canonicalize_state(new_state);
    return new_state;
}


vector<pair<vector<Position>, string>> generate_moves(const vector<string>& spec, const vector<Position>& state, const string& path) {
    vector<pair<vector<Position>, string>> result;
    for (char move : string("UDLR")) {
        vector<Position> new_state = do_move(spec, state, move);
        result.push_back({new_state, path + move});
    }
    return result;
}

struct Node {
    int f, g;
    vector<Position> state;
    string path;
};
struct NodeCompare {
    bool operator()(const Node& a, const Node& b) {
        return a.f > b.f;
    }
};
string state_to_string(const vector<Position>& state) {
    string s;
    for (const auto& pos : state) {
        s += to_string(pos.first) + "," + to_string(pos.second) + ";";
    }
    return s;
}

string astar(const vector<string>& spec, const vector<Position>& init_state, const vector<Position>& goals) {
    vector<Position> init = init_state;
    canonicalize_state(init);
    priority_queue<Node, vector<Node>, NodeCompare> prioque;
    int h_val = heuristic(init, goals);
    prioque.push({h_val, 0, init, ""});

    // set<string> visited;
    // visited.insert(state_to_string(init));

    //dodajemy re-expanse stanow
    unordered_map<string, int> visited;
    visited[state_to_string(init)] = 0;

    vector<vector<int>> memoized_for_heuristics(spec.size(), vector<int>(spec[0].size(), -1));

    while (!prioque.empty()) {
        Node curr = prioque.top();
        prioque.pop();

        bool isGoal = true;
        for (const auto& pos : curr.state) {
            if (find(goals.begin(), goals.end(), pos) == goals.end()) {
                isGoal = false;
                break;
            }
        }
        if (isGoal) {
            return curr.path;
        }

        

        vector<pair<vector<Position>, string>> next_moves = generate_moves(spec, curr.state, curr.path);
        for (const auto& move : next_moves) {
            auto new_st = move.first;
            auto new_path = move.second;
            int new_g = curr.g + 1;
            int h1 = better_heuristic(spec, new_st, memoized_for_heuristics);
            // int h2 = heuristic(new_st, goals);
            int new_f = new_g + h1;
            string key = state_to_string(new_st);
            // if (visited.find(key) == visited.end()) {
            //     visited.insert(key);
            //     prioque.push({new_f, new_g, new_st, new_path});
            // }
            if (visited.find(key) == visited.end() || new_g < visited[key]) {
                visited[key] = new_g;
                prioque.push({new_f, new_g, new_st, new_path});
            }
        }

    }
    return "";
}


int main() {

    

    ifstream fin("zad_input.txt");
    ofstream fout("zad_output.txt");
    vector<string> spec;
    string line;
    while(getline(fin, line)) {
        if (!line.empty()) {
            spec.push_back(line);
        }
    }
    
    int X = spec.size();
    int Y = spec[0].size();

    vector<Position> initial_state;
    vector<Position> goals;
    

    for (int i = 0; i < X; i++) {
        for (int j = 0; j < Y; j++) {
            char c = spec[i][j];
            if (c == 'S' || c == 'B') {
                initial_state.push_back({i, j});
            }
            if (c == 'G' || c == 'B') {
                goals.push_back({i, j});
            }
        }
    }
    
    string path = astar(spec, initial_state, goals);
    fout << path;

    return 0;
}