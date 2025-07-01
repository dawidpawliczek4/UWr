#include <algorithm>
#include <chrono>
#include <climits>
#include <future>
#include <iostream>
#include <random>
#include <thread>
#include <utility>
#include <vector>

using namespace std;

class Reversi {
   public:
    static constexpr int M = 8;
    static inline constexpr pair<int, int> DIRS[M] = {
        {-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    using Move = pair<int, int>;
    int board[M][M];

    Reversi() {
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < M; ++j) {
                board[i][j] = -1;
            }
        }
        board[3][3] = board[4][4] = 1;
        board[3][4] = board[4][3] = 0;
    }

    vector<Move> getAllPossibleMoves(int player) const {
        vector<Move> moves;
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < M; ++j) {
                if (board[i][j] != -1) continue;
                for (auto [dx, dy] : DIRS) {
                    int x = i + dx, y = j + dy;
                    bool foundOpp = false;
                    while (x >= 0 && x < M && y >= 0 && y < M) {
                        if (board[x][y] == -1) break;
                        if (board[x][y] == player) {
                            if (foundOpp) {
                                moves.emplace_back(i, j);
                            }
                            break;
                        }
                        foundOpp = true;
                        x += dx;
                        y += dy;
                    }
                }
            }
        }
        return moves;
    }

    void doMove(const Move& move, int player) {
        if (move.first < 0) return;
        int x = move.first, y = move.second;
        board[x][y] = player;
        for (auto [dx, dy] : DIRS) {
            int x1 = x + dx, y1 = y + dy;
            bool foundOpp = false;
            while (x1 >= 0 && x1 < M && y1 >= 0 && y1 < M) {
                if (board[x1][y1] == -1) break;
                if (board[x1][y1] == player) {
                    if (foundOpp) {
                        for (int i = x + dx, j = y + dy; i != x1 || j != y1;
                             i += dx, j += dy) {
                            board[i][j] = player;
                        }
                    }
                    break;
                }
                foundOpp = true;
                x1 += dx;
                y1 += dy;
            }
        }
    }

    int eval(int player) const {
        static const int W[8][8] = {
            {4, 0, 2, 2, 2, 2, 0, 4}, {0, 0, 2, 1, 1, 2, 0, 0},
            {2, 2, 2, 1, 1, 2, 2, 2}, {2, 2, 1, 1, 1, 1, 2, 2},
            {2, 2, 1, 1, 1, 1, 2, 2}, {2, 2, 2, 1, 1, 2, 2, 2},
            {0, 0, 2, 1, 1, 2, 0, 0}, {4, 0, 2, 2, 2, 2, 0, 4}};
        int score = 0;
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < M; ++j) {
                if (board[i][j] == player)
                    score += W[i][j];
                else if (board[i][j] == 1 - player)
                    score -= W[i][j];
            }
        }
        return score;
    }

    Reversi* clone() const {
        Reversi* g = new Reversi();
        for (int i = 0; i < M; ++i)
            for (int j = 0; j < M; ++j) g->board[i][j] = board[i][j];
        return g;
    }

    // Actual disc-difference at end of game
    int result(int player) const {
        int diff = 0;
        for (int i = 0; i < M; ++i)
            for (int j = 0; j < M; ++j)
                diff += (board[i][j] == player)       ? +1
                        : (board[i][j] == 1 - player) ? -1
                                                      : 0;
        return diff;
    }

    int countEmpty() const {
        int empty = 0;
        for (int i = 0; i < M; ++i)
            for (int j = 0; j < M; ++j)
                if (board[i][j] == -1) ++empty;
        return empty;
    }
};

int selectDepth(const Reversi* game) {
    int empty = game->countEmpty();
    if (empty > 30) return 3;
    if (empty > 15) return 4;
    return 5;
}

pair<int, Reversi::Move> minimax(Reversi* game, int depth, int player,
                                 bool isMax, int myPlayer, int alpha = INT_MIN,
                                 int beta = INT_MAX) {
    if (depth == 0) return {game->eval(myPlayer), {-1, -1}};
    auto moves = game->getAllPossibleMoves(player);
    if (moves.empty()) return {game->eval(myPlayer), {-1, -1}};

    int bestScore = isMax ? INT_MIN : INT_MAX;
    Reversi::Move bestMove{-1, -1};

    for (auto m : moves) {
        Reversi* child = game->clone();
        child->doMove(m, player);
        auto [sc, _] = minimax(child, depth - 1, 1 - player, !isMax, myPlayer,
                               alpha, beta);
        delete child;

        if (isMax) {
            if (sc > bestScore) {
                bestScore = sc;
                bestMove = m;
            }
            alpha = max(alpha, bestScore);
        } else {
            if (sc < bestScore) {
                bestScore = sc;
                bestMove = m;
            }
            beta = min(beta, bestScore);
        }
        if (beta <= alpha) break;
    }
    return {bestScore, bestMove};
}

Reversi::Move iterativeDeepening(Reversi* game, int me, int move_count) {
    Reversi::Move best{-1, -1};    
    int depth = 5;
    if (move_count > 35) {
        depth = 7;
    } else if (move_count > 45) {
        depth = 10;
    } else if (move_count > 52) {
        depth = 14;
    }

    auto moves = game->getAllPossibleMoves(me);
    if (moves.empty()) return best;

    vector<future<pair<int, Reversi::Move>>> futures;
    futures.reserve(moves.size());
    for (auto m : moves) {
        futures.emplace_back(async(
            launch::async, [game, me, m, depth]() -> pair<int, Reversi::Move> {
                Reversi* child = game->clone();
                child->doMove(m, me);
                auto res = minimax(child, depth - 1, 1 - me, false, me);
                delete child;

                return make_pair(res.first, m);
            }));
    }
    int bestScore = INT_MIN;
    for (auto& f : futures) {
        auto [sc, mv] = f.get();
        if (sc > bestScore) {
            bestScore = sc;
            best = mv;
        }
    }

    return best;
}

class AIPlayer {
    int playerId;
    int counter;

   public:
    Reversi game;
    AIPlayer(int id) { reset(id); }

    void reset(int id) {
        playerId = id;
        counter = -1;
        game = Reversi();
    }

    Reversi::Move uStart() {
        auto mv = iterativeDeepening(&game, playerId, 0);
        game.doMove(mv, playerId);
        return mv;
    }

    Reversi::Move nextMove(const Reversi::Move& oppMove, int move_count) {
        game.doMove(oppMove, 1 - playerId);
        auto mv = iterativeDeepening(&game, playerId, move_count);
        game.doMove(mv, playerId);
        counter++;
        return mv;
    }
};

// RandomPlayer wybiera losowy ruch z możliwych
class RandomPlayer {
    int playerId;
    Reversi game;
    mt19937 rng;

   public:
    RandomPlayer(int id) : playerId(id), rng(random_device{}()) {
        game = Reversi();
    }

    void reset(int id) {
        playerId = id;
        game = Reversi();
    }

    Reversi::Move uStart() {
        auto moves = game.getAllPossibleMoves(playerId);
        if (moves.empty()) return {-1, -1};
        uniform_int_distribution<size_t> dist(0, moves.size() - 1);
        auto mv = moves[dist(rng)];
        game.doMove(mv, playerId);
        return mv;
    }

    Reversi::Move nextMove(const Reversi::Move& oppMove) {
        game.doMove(oppMove, 1 - playerId);
        auto moves = game.getAllPossibleMoves(playerId);
        if (moves.empty()) return {-1, -1};
        uniform_int_distribution<size_t> dist(0, moves.size() - 1);
        auto mv = moves[dist(rng)];
        game.doMove(mv, playerId);
        return mv;
    }
};

int main() {
    int firstWinsOrDraws = 0;
    const int ROUNDS = 1000;

    for (int i = 0; i < ROUNDS; ++i) {        
        AIPlayer p1(0);
        RandomPlayer p2(1);
        auto m1 = p1.uStart();
        auto m2 = p2.nextMove(m1);
        int move_count = 1;     
        // play until both pass (-1,-1)
        while (!(m1.first < 0 && m2.first < 0)) {       
            
            m1 = p1.nextMove(m2, move_count);
            m2 = p2.nextMove(m1);
            move_count++;
        }

        int diff = p1.game.result(0);
        if (diff >= 0) ++firstWinsOrDraws;
    }

    cout << "First player (AI) wins or draws in " << firstWinsOrDraws
         << " out of " << ROUNDS << "\n";
    return 0;
}
