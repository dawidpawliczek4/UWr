#include <iostream>
#include <sstream>
#include <chrono>
#include <climits>
#include <utility>

using namespace std;

using Clock    = std::chrono::steady_clock;
using TimePoint= Clock::time_point;
using Duration = std::chrono::milliseconds;
using Move     = std::pair<int,int>;
struct TimeUp {};

class Reversi {
    public:
    static constexpr int M = 8;
    static constexpr pair<int, int>DIRS[M]  = {
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1},          {0, 1},
        {1, -1}, {1, 0}, {1, 1}
    };
    using Move = pair<int,int>;
    int board[M][M];

    Reversi() {
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < M; ++j) {                
                if ((i == 3 && j == 3) || (i == 4 && j == 4)) {
                    board[i][j] = 1;
                } else if ((i == 3 && j == 4) || (i == 4 && j == 3)) {
                    board[i][j] = 0;
                } else {
                    board[i][j] = -1;                    
                }
            }
        }
    }

    vector<Move> getAllPossibleMoves(int player) {
        vector<Move> moves;
        
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < M; ++j) {
                if (board[i][j] == -1) {
                    for (const auto& dir : DIRS) {
                        int x = i + dir.first;
                        int y = j + dir.second;
                        bool foundOpponent = false;
                        while (x >= 0 && x < M && y >= 0 && y < M) {
                            if (board[x][y] == -1) break;
                            if (board[x][y] == player) {
                                if (foundOpponent) {
                                    moves.push_back({i, j});
                                }
                                break;
                            }
                            foundOpponent = true;
                            x += dir.first;
                            y += dir.second;
                        }
                    }
                }
            }
        }

        return moves;
    }

    void doMove(Move move, int player) {
        if (move == Move{-1, -1}) return;
        int x = move.first;
        int y = move.second;
        if (board[x][y] == -1) {
            board[x][y] = player;
        }
        for (const auto& dir : DIRS) {
            int x1 = x + dir.first;
            int y1 = y + dir.second;
            bool foundOpponent = false;
            while (x1 >= 0 && x1 < M && y1 >= 0 && y1 < M) {
                if (board[x1][y1] == -1) break;
                if (board[x1][y1] == player) {
                    if (foundOpponent) {
                        for (int i = x + dir.first, j = y + dir.second; i != x1 || j != y1; i += dir.first, j += dir.second) {
                            board[i][j] = player;
                        }
                    }
                    break;
                }
                foundOpponent = true;
                x1 += dir.first;
                y1 += dir.second;
            }
        }
    }


    int eval(int player){
        static const int WEIGHTS[8][8] = {
            { 100, -20,  10,   5,   5,  10, -20, 100},
            { -20, -50,  -2,  -2,  -2,  -2, -50, -20},
            {  10,  -2,   1,   1,   1,   1,  -2,  10},
            {   5,  -2,   1,   1,   1,   1,  -2,   5},
            {   5,  -2,   1,   1,   1,   1,  -2,   5},
            {  10,  -2,   1,   1,   1,   1,  -2,  10},
            { -20, -50,  -2,  -2,  -2,  -2, -50, -20},
            { 100, -20,  10,   5,   5,  10, -20, 100}
        };

        int score = 0;
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < M; ++j) {
                if (board[i][j] == player) {
                    score += WEIGHTS[i][j];
                } else if (board[i][j] == 1 - player) {
                    score -= WEIGHTS[i][j];
                }
            }
        }
        return score;
    }

    Reversi* clone() {
        Reversi* newGame = new Reversi();
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < M; ++j) {
                newGame->board[i][j] = this->board[i][j];
            }
        }
        return newGame;
    }



};


std::pair<int, Reversi::Move> minimax(Reversi* game, int depth, int player, bool isMaxPlayer,int myPlayer, TimePoint moveStart, Duration timeLimit, int alpha = INT_MIN, int beta = INT_MAX) {

    auto elapsed = chrono::steady_clock::now() - moveStart;
    // cerr << "Elapsed time: " << chrono::duration_cast<chrono::milliseconds>(elapsed).count() << "ms\n";
    if (chrono::duration_cast<chrono::milliseconds>(elapsed).count() > timeLimit.count()) {
        throw TimeUp();

    }

    if (depth == 0) {
        return {game->eval(myPlayer), {-1, -1}};
    }

    vector<Reversi::Move> moves = game->getAllPossibleMoves(player);
    if (moves.empty()) {
        return {game->eval(myPlayer), {-1, -1}};
    }

    int bestScore = isMaxPlayer ? INT_MIN : INT_MAX;
    Reversi::Move bestMove = {-1, -1};

    for (const auto& move : moves) {
        auto elapsed = chrono::steady_clock::now() - moveStart;
        if (chrono::duration_cast<chrono::milliseconds>(elapsed).count() > timeLimit.count()) {
            throw TimeUp();
        }

        Reversi* newGame = game->clone();
        newGame->doMove(move, player);
        auto [score, _] = minimax(newGame, depth - 1, 1-player, !isMaxPlayer, myPlayer,moveStart, timeLimit, alpha, beta);
        delete newGame;

        if (isMaxPlayer) {
            if (score > bestScore) {
                bestScore = score;
                bestMove = move;
            }
            alpha = max(alpha, bestScore);
            if (beta <= alpha) {
                break;
            }
        } else {
            if (score < bestScore) {
                bestScore = score;
                bestMove = move;
            }
            beta = min(beta, bestScore);
            if (beta <= alpha) {
                break;
            }
        }
    }

    return {bestScore, bestMove};
}


Reversi::Move iterativeDeepening(Reversi* game, int myPlayer, Duration timeLimit) {
    TimePoint moveStart = Clock::now();    
    Reversi::Move bestMove = {-1, -1};
    int maxDepth = 4;

    for (int depth = 4; depth <= maxDepth; ++depth) {
        auto elapsed = chrono::steady_clock::now() - moveStart;
        if (chrono::duration_cast<chrono::milliseconds>(elapsed).count() > timeLimit.count()) {
            return bestMove;
        }
        try {
            auto [score, move] = minimax(game, depth, myPlayer, true, myPlayer, moveStart, timeLimit);
            bestMove = move;
        } catch (TimeUp&) {
            return bestMove;
        }
    }
    return bestMove;
}

class Player {
    public:
    Reversi game;
    int player;
    void say(string message) {
        cout << message << "\n";
        cout.flush();
    };
    Player() {
        reset();
    };
    void reset() {
        game = Reversi();
        player = 1;
        say("RDY");
    };
 
    pair<string, vector<string>> hear() {
        string line;
        if (!getline(cin, line)) {
            return {"", {}};
        }
        istringstream iss(line);
        string cmd;
        iss >> cmd;
        vector<string> args;
        string arg;
        while (iss >> arg) {
            args.push_back(arg);
        }
        
        return {cmd, args};
    };
    void loop() {
        while (true) {
            auto [command, args] = hear();
            if (command == "HEDID") {
                Reversi::Move move = {stoi(args[3]), stoi(args[2])};
                game.doMove(move, 1 - player);                        
            } else if (command == "ONEMORE") {
                reset();
                continue;
            } else if (command == "BYE") {
                break;
            } else if (command == "UGO") {
                player = 0;                                
            }

            Reversi* new_game = game.clone();
            auto move = iterativeDeepening(new_game, player, Duration(4000));
            delete new_game;
            game.doMove(move, player);
            cout << "IDO " << move.second << " " << move.first << "\n";
            cout.flush();
        }
    }
};


int main(){ 
    Player player = Player();
    player.loop();
    return 0;
}