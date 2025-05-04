#include <iostream>
#include <vector>

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

class MaxHeap {
    public:
        vector<Node> heap;

        void heapifyUp(int index) {
            while (index > 0) {
                int parent = (index - 1) / 2;
                if (Compare()(heap[parent], heap[index])) {
                    swap(heap[parent], heap[index]);
                    index = parent;
                } else {
                    break;
                }
            }
        }

        void heapifyDown(int index) {
            int size = heap.size();
            while (true) {
                int largest = index;
                int left = 2 * index + 1;
                int right = 2 * index + 2;

                if (left < size && Compare()(heap[largest], heap[left])) {
                    largest = left;
                }
                if (right < size && Compare()(heap[largest], heap[right])) {
                    largest = right;
                }
                if (largest != index) {
                    swap(heap[index], heap[largest]);
                    index = largest;
                } else {
                    break;
                }
            }
        }

    public:
        MaxHeap(
            int M
        ) {
            heap = vector<Node>(M);
        }

        void push(const Node &node) {
            heap.push_back(node);
            heapifyUp(heap.size() - 1);
        }

        void pop() {
            if (heap.empty()) return;
            heap[0] = heap.back();
            heap.pop_back();
            heapifyDown(0);
        }

        Node top() const {
            if (!heap.empty()) {
                return heap[0];
            }
            throw runtime_error("Heap is empty");
        }

        bool empty() const {
            return heap.empty();
        }
};


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, k;
    cin >> M >> k;
    long long lastVal = -1;

    MaxHeap pq(M);

    for (int i = 0; i < M; i++) {
        pq.heap[i] = Node{(long long)(M - i) * (M - i), (int)(M - i), (int)(M - i)};
    }

    int countDistinct = 0;
    
    while(!pq.empty() && countDistinct < k) {
        Node top = pq.top();
        pq.pop();

        if (top.val != lastVal) {
            cout << top.val << "\n";
            countDistinct++;
            lastVal = top.val;
        }   

        if (top.i > 1) {
            pq.push(
                {(long long)(top.i - 1) * top.j, top.i - 1, top.j}
            );
        }
    }

    return 0;
}
