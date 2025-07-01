#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import random
import sys
import chess
import copy

PST = {
    chess.PAWN: [
        0,   0,   0,   0,   0,   0,   0,   0,
        5,  10,  10, -20, -20,  10,  10,   5,
        5,  -5, -10,   0,   0, -10,  -5,   5,
        0,   0,   0,  20,  20,   0,   0,   0,
        5,   5,  10,  25,  25,  10,   5,   5,
        10,  10,  20,  30,  30,  20,  10,  10,
        50,  50,  50,  50,  50,  50,  50,  50,
        0,   0,   0,   0,   0,   0,   0,   0
    ],
    chess.KNIGHT: [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20,   0,   0,   0,   0, -20, -40,
        -30,   0,  10,  15,  15,  10,   0, -30,
        -30,   5,  15,  20,  20,  15,   5, -30,
        -30,   0,  15,  20,  20,  15,   0, -30,
        -30,   5,  10,  15,  15,  10,   5, -30,
        -40, -20,   0,   5,   5,   0, -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50
    ],
    chess.BISHOP: [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10,   5,   0,   0,   0,   0,   5, -10,
        -10,  10,  10,  10,  10,  10,  10, -10,
        -10,   0,  10,  10,  10,  10,   0, -10,
        -10,   5,   5,  10,  10,   5,   5, -10,
        -10,   0,   5,  10,  10,   5,   0, -10,
        -10,   0,   0,   0,   0,   0,   0, -10,
        -20, -10, -10, -10, -10, -10, -10, -20
    ],
    chess.ROOK: [
         0,   0,   0,   5,   5,   0,   0,   0,
        -5,   0,   0,   0,   0,   0,   0,  -5,
        -5,   0,   0,   0,   0,   0,   0,  -5,
        -5,   0,   0,   0,   0,   0,   0,  -5,
        -5,   0,   0,   0,   0,   0,   0,  -5,
        -5,   0,   0,   0,   0,   0,   0,  -5,
         5,  10,  10,  10,  10,  10,  10,   5,
         0,   0,   0,   0,   0,   0,   0,   0
    ],
    chess.QUEEN: [
        -20, -10, -10,  -5,  -5, -10, -10, -20,
        -10,   0,   0,   0,   0,   0,   0, -10,
        -10,   0,   5,   5,   5,   5,   0, -10,
         -5,   0,   5,   5,   5,   5,   0,  -5,
          0,   0,   5,   5,   5,   5,   0,  -5,
        -10,   5,   5,   5,   5,   5,   0, -10,
        -10,   0,   5,   0,   0,   0,   0, -10,
        -20, -10, -10,  -5,  -5, -10, -10, -20
    ],
    chess.KING: [
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -20, -30, -30, -40, -40, -30, -30, -20,
        -10, -20, -20, -20, -20, -20, -20, -10,
         20,  20,   0,   0,   0,   0,  20,  20,
         20,  30,  10,   0,   0,  10,  30,  20
    ]
}

MATERIAL = {
    chess.PAWN:   100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK:   500,
    chess.QUEEN:  900,
    chess.KING:     0
}


class Chess:
    def __init__(self):
        self.board = chess.Board()

    def update(self, uci_move):
        try:
            move = chess.Move.from_uci(uci_move)
        except ValueError:
            raise WrongMove

        if move not in self.board.legal_moves:
            raise WrongMove

        self.board.push(move)
        out = self.board.outcome()
        if out is None:
            return None
        if out.winner is None:
            return 0
        if out.winner:
            return -1
        else:
            return +1

    def moves(self):
        return [str(m) for m in self.board.legal_moves]

    def draw(self):
        print(self.board)

    def eval(self):
        """
        evaluates board from white's perspective
        """
        if self.board.is_checkmate():            
            return -10_000 if self.board.turn == chess.WHITE else +10_000
        if self.board.is_stalemate() or self.board.is_insufficient_material() \
           or self.board.can_claim_fifty_moves() or self.board.can_claim_threefold_repetition():
            return 0

        score = 0

        #material
        for sq, piece in self.board.piece_map().items():
            sign = 1 if piece.color == chess.WHITE else -1
            score += sign * MATERIAL[piece.piece_type]
            #bonus za dany material na danym polu, dla czarnych odwracamy wspolrzednie zeby korzystac z tej samej tablicy
            if piece.piece_type in PST:
                idx = sq if piece.color == chess.WHITE else chess.square_mirror(
                    sq)
                score += sign * PST[piece.piece_type][idx]

        #mobilnosc
        mobility = len(list(self.board.legal_moves))        
        score += mobility * (1 if self.board.turn == chess.WHITE else -1) * 10

        # kontrola centrum
        center = [chess.D4, chess.D5, chess.E4, chess.E5]
        ctrl = 0
        for c in center:
            ctrl += len(self.board.attackers(chess.WHITE, c))
            ctrl -= len(self.board.attackers(chess.BLACK, c))
        score += ctrl * 15

        return score
    
    def eval_for(self, player: int):
        """ evaluates the board for player
        big number -> good for player
        """
        if player == 0:
            return self.eval()
        else:
            return -1 * self.eval()


class MinMaxPlayer(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.game = Chess()
        self.my_player = 1
        self.say('RDY')

    def say(self, what):
        sys.stdout.write(what)
        sys.stdout.write('\n')
        sys.stdout.flush()

    def hear(self):
        line = sys.stdin.readline().split()
        return line[0], line[1:]

    def minimax(self, game: Chess, player: int, isMaxPlayer: bool, depth: int, alpha: int, beta: int):
        if depth == 0 or len(game.moves()) == 0:
            return game.eval_for(self.my_player), None

        if isMaxPlayer:
            best_val, best_move = float('-inf'), None
        else:
            best_val, best_move = float('inf'), None

        for move in game.moves():
            game.board.push(chess.Move.from_uci(move))
            
            val, _ = self.minimax(
                game, 1 - player, not isMaxPlayer, depth - 1, alpha, beta)
            
            game.board.pop()

            if isMaxPlayer:
                if val > best_val:
                    best_val, best_move = val, move
                    alpha = max(alpha, best_val)
                    if alpha >= beta:
                        break
            else:
                if val < best_val:
                    best_val, best_move = val, move
                    beta = min(beta, best_val)
                    if alpha >= beta:
                        break
            

        return best_val, best_move

    def get_move(self):
        _, move = self.minimax(self.game, self.my_player,
                               True, 2, float('-inf'), float('inf'))
        return move

    def loop(self):
        while True:
            cmd, args = self.hear()
            if cmd == 'HEDID':
                unused_move_timeout, unused_game_timeout = args[:2]
                move = args[2]

                self.game.update(move)
            elif cmd == 'ONEMORE':
                self.reset()
                continue
            elif cmd == 'BYE':
                break
            else:
                assert cmd == 'UGO'
                # assert not self.game.move_list
                self.my_player = 0

            move = self.get_move()
            self.game.update(move)

            self.say('IDO ' + move)


def make_simulation():
    wins = 0
    for i in range(10):        
        minmaxagent = MinMaxPlayer()
        minmaxagent.my_player = 0
        move = 1
        while (not minmaxagent.game.board.is_game_over()):
            if move:
                minmaxagent.game.update(minmaxagent.get_move())
            else:
                minmaxagent.game.update(random.choice(minmaxagent.game.moves()))
            move = 1 - move
        if minmaxagent.game.board.turn == chess.BLACK:
            wins += 1
        print("game: ", i, " won: ", minmaxagent.game.board.turn == chess.BLACK)
    
    for i in range(10):        
        minmaxagent = MinMaxPlayer()
        minmaxagent.my_player = 1
        move = 0
        while (not minmaxagent.game.board.is_game_over()):
            if move:
                minmaxagent.game.update(minmaxagent.get_move())
            else:
                minmaxagent.game.update(random.choice(minmaxagent.game.moves()))
            move = 1 - move
        if minmaxagent.game.board.turn == chess.WHITE:
            wins += 1
        print("game: ", i, " won: ", minmaxagent.game.board.turn == chess.WHITE)


    print(wins)
        


if __name__ == '__main__':
    Player = MinMaxPlayer()
    Player.loop()
    # make_simulation()