#include <iostream>
#include <queue>
#include <utility>
#include <functional>
#include <set>
#include <unordered_set>
using namespace std;

struct Node {
    long long val;
    int i, j;
};

struct Compare {
    bool operator()(const Node &a, const Node &b) {
        return a.val < b.val;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long M, k;
    cin >> M >> k;
    long long lastVal = -1;

    
    vector<Node> initial(M);
    for (int i = 0; i <= M; i++) {
        initial[i] = {(1LL * (M - i) * (M - i)), (int)(M-i), (int)(M-i)};        
    }

    priority_queue<Node, vector<Node>, Compare> pq(initial.begin(), initial.end());
    int countDistinct = 0;
    
    while(!pq.empty() && countDistinct < k) {
        Node top = pq.top();
        pq.pop();

        if (top.val != lastVal) {
            cout << top.val << "\n";
            countDistinct++;
            lastVal = top.val;
        }

        int new_i = top.i - 1;        

        if (new_i > 0) {
            long long new_val = 1LL * new_i * top.j;
            pq.push(
                {new_val, new_i, top.j}
            );
        }
    }

    return 0;
}