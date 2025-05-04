#include <iostream>
#include <chrono>
#include <climits>
#include <utility>
#include <vector>
#include <random>


using namespace std;
using Clock     = chrono::steady_clock;
using TimePoint = Clock::time_point;
using Duration  = chrono::milliseconds;

struct TimeUp {};

class Reversi {
public:
    static constexpr int M = 8;
    static inline constexpr pair<int,int> DIRS[M] = {
        {-1,-1}, {-1,0}, {-1,1},
        { 0,-1},         { 0,1},
        { 1,-1}, { 1,0}, { 1,1}
    };
    using Move = pair<int,int>;
    int board[M][M];

    Reversi() {
        for(int i=0;i<M;++i){
            for(int j=0;j<M;++j){
                board[i][j] = -1;
            }
        }
        board[3][3] = board[4][4] = 1;
        board[3][4] = board[4][3] = 0;
    }

    vector<Move> getAllPossibleMoves(int player) const {
        vector<Move> moves;
        for(int i=0;i<M;++i){
            for(int j=0;j<M;++j){
                if(board[i][j] != -1) continue;
                for(auto [dx,dy] : DIRS){
                    int x = i + dx, y = j + dy;
                    bool foundOpp = false;
                    while(x>=0 && x<M && y>=0 && y<M){
                        if(board[x][y] == -1) break;
                        if(board[x][y] == player){
                            if(foundOpp){
                                moves.emplace_back(i,j);
                            }
                            break;
                        }
                        foundOpp = true;
                        x += dx; y += dy;
                    }
                }
            }
        }
        return moves;
    }

    void doMove(const Move& move, int player) {
        if(move.first<0) return;
        int x = move.first, y = move.second;
        board[x][y] = player;
        for(auto [dx,dy] : DIRS){
            int x1 = x+dx, y1 = y+dy;
            bool foundOpp = false;
            while(x1>=0 && x1<M && y1>=0 && y1<M){
                if(board[x1][y1] == -1) break;
                if(board[x1][y1] == player){
                    if(foundOpp){
                        for(int i=x+dx, j=y+dy; i!=x1 || j!=y1; i+=dx, j+=dy){
                            board[i][j] = player;
                        }
                    }
                    break;
                }
                foundOpp = true;
                x1 += dx; y1 += dy;
            }
        }
    }

    int eval(int player) const {
        static const int W[8][8] = {
            {100,-20, 10, 5, 5,10,-20,100},
            {-20,-50, -2,-2,-2,-2,-50,-20},
            { 10, -2,  1, 1, 1, 1, -2, 10},
            {  5, -2,  1, 1, 1, 1, -2,  5},
            {  5, -2,  1, 1, 1, 1, -2,  5},
            { 10, -2,  1, 1, 1, 1, -2, 10},
            {-20,-50, -2,-2,-2,-2,-50,-20},
            {100,-20, 10, 5, 5,10,-20,100}
        };
        int score = 0;
        for(int i=0;i<M;++i){
            for(int j=0;j<M;++j){
                if(board[i][j] == player)       score += W[i][j];
                else if(board[i][j] == 1-player) score -= W[i][j];
            }
        }
        return score;
    }

    Reversi* clone() const {
        Reversi* g = new Reversi();
        for(int i=0;i<M;++i)
            for(int j=0;j<M;++j)
                g->board[i][j] = board[i][j];
        return g;
    }

    // Actual disc-difference at end of game
    int result(int player) const {
        int diff = 0;
        for(int i=0;i<M;++i)
            for(int j=0;j<M;++j)
                diff += (board[i][j] == player) ? +1
                      : (board[i][j] == 1-player) ? -1
                      : 0;
        return diff;
    }
};

pair<int, Reversi::Move>
minimax(Reversi* game, int depth, int player, bool isMax,
        int myPlayer, TimePoint start, Duration limit,
        int alpha = INT_MIN, int beta = INT_MAX)
{
    if(chrono::steady_clock::now() - start > limit) throw TimeUp();
    if(depth == 0) return { game->eval(myPlayer), {-1,-1} };

    auto moves = game->getAllPossibleMoves(player);
    if(moves.empty()) return { game->eval(myPlayer), {-1,-1} };

    int bestScore = isMax ? INT_MIN : INT_MAX;
    Reversi::Move bestMove{-1,-1};

    for(auto m : moves){
        if(chrono::steady_clock::now() - start > limit) throw TimeUp();
        Reversi* child = game->clone();
        child->doMove(m, player);
        auto [sc, _] = minimax(child, depth-1, 1-player, !isMax,
                               myPlayer, start, limit, alpha, beta);
        delete child;

        if(isMax){
            if(sc > bestScore){
                bestScore = sc;
                bestMove = m;
            }
            alpha = max(alpha, bestScore);
        } else {
            if(sc < bestScore){
                bestScore = sc;
                bestMove = m;
            }
            beta = min(beta, bestScore);
        }
        if(beta <= alpha) break;
    }
    return {bestScore, bestMove};
}

Reversi::Move
iterativeDeepening(Reversi* game, int me, Duration limit, int counter=3) {
    TimePoint start = Clock::now();
    Reversi::Move best{-1,-1};
    const int MAXD = max(counter, 3);
    for(int depth = 3; depth <= MAXD; ++depth){
        if(chrono::steady_clock::now() - start > limit) break;
        Reversi* copy = game->clone();
        try {
            auto [_, mv] = minimax(copy, depth, me, true, me, start, limit);
            best = mv;
        } catch(TimeUp&) {
            delete copy;
            break;
        }
        delete copy;
    }
    return best;
}

class AIPlayer {
    int playerId;
    int counter;
public:
    Reversi game;
    AIPlayer(int id) { reset(id); }

    void reset(int id){
        playerId = id;
        counter = -1;
        game = Reversi();
    }

    Reversi::Move uStart(){
        auto mv = iterativeDeepening(&game, playerId, Duration(1000));
        game.doMove(mv, playerId);
        return mv;
    }

    Reversi::Move nextMove(const Reversi::Move& oppMove){
        game.doMove(oppMove, 1-playerId);
        auto mv = iterativeDeepening(&game, playerId, Duration(1000), counter);
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
    RandomPlayer(int id)
        : playerId(id), rng(random_device{}()) {
        game = Reversi();
    }

    void reset(int id) {
        playerId = id;
        game = Reversi();
    }

    Reversi::Move uStart() {
        auto moves = game.getAllPossibleMoves(playerId);
        if(moves.empty()) return {-1,-1};
        uniform_int_distribution<size_t> dist(0, moves.size()-1);
        auto mv = moves[dist(rng)];
        game.doMove(mv, playerId);
        return mv;
    }

    Reversi::Move nextMove(const Reversi::Move& oppMove) {
        game.doMove(oppMove, 1-playerId);
        auto moves = game.getAllPossibleMoves(playerId);
        if(moves.empty()) return {-1,-1};
        uniform_int_distribution<size_t> dist(0, moves.size()-1);
        auto mv = moves[dist(rng)];
        game.doMove(mv, playerId);
        return mv;
    }
};

int main(){
    int firstWinsOrDraws = 0;
    const int ROUNDS = 1000;

    for(int i=0;i<ROUNDS;++i){
        AIPlayer p1(0);
        RandomPlayer p2(1);
        auto m1 = p1.uStart();
        auto m2 = p2.nextMove(m1);

        // play until both pass (-1,-1)
        while(!(m1.first<0 && m2.first<0)){
            m1 = p1.nextMove(m2);
            m2 = p2.nextMove(m1);
        }

        int diff = p1.game.result(0);
        if(diff >= 0) ++firstWinsOrDraws;
    }

    cout << "First player (AI) wins or draws in " 
         << firstWinsOrDraws << " out of " << ROUNDS << "\n";
    return 0;
}
