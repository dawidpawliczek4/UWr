#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import random
import sys


class Reversi:
    M = 8
    DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def __init__(self):
        self.board = self.initial_board()
        self.fields = set()
        for i in range(self.M):
            for j in range(self.M):
                if self.board[i][j] is None:
                    self.fields.add((j, i))

    def clone(self):
        new = Reversi()
        new.board = [row[:] for row in self.board]
        new.fields = set(self.fields)
        return new

    def initial_board(self):
        B = [[None] * self.M for _ in range(self.M)]
        B[3][3] = 1
        B[4][4] = 1
        B[3][4] = 0
        B[4][3] = 0
        return B

    def moves(self, player):
        res = []
        for (x, y) in self.fields:
            if any(self.can_beat(x, y, direction, player)
                   for direction in self.DIRS):
                res.append((x, y))
        return res

    def can_beat(self, x, y, d, player):
        dx, dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x, y) == 1 - player:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x, y) == player

    def get(self, x, y):
        if 0 <= x < self.M and 0 <= y < self.M:
            return self.board[y][x]
        return None

    def do_move(self, move, player):
        if move is None:
            return
        x, y = move
        x0, y0 = move
        self.board[y][x] = player
        self.fields -= set([move])
        for dx, dy in self.DIRS:
            x, y = x0, y0
            to_beat = []
            x += dx
            y += dy
            while self.get(x, y) == 1 - player:
                to_beat.append((x, y))
                x += dx
                y += dy
            if self.get(x, y) == player:
                for (nx, ny) in to_beat:
                    self.board[ny][nx] = player


    def result(self):
        # liczy przewage nad graczem '1'
        # duzy wynik -> '1' ma duzo pionkow
        res = 0
        for y in range(self.M):
            for x in range(self.M):
                b = self.board[y][x]
                if b == 0:
                    res -= 1
                elif b == 1:
                    res += 1
        return res
    

    #we add how good is position for that player
    def eval(self, player):
        res = self.result()
        if player == 1:
            return res
        else:
            return -res    
        
    
def minimax(game: Reversi, player: int, depth: int, isMaxPlayer: bool, alpha, beta):
    # sys.stderr.write("something")
    
    if depth == 0 or len(game.moves(player)) == 0:
        return game.eval(player), None  
    
    if isMaxPlayer:
        best_val, best_move = float('-inf'), None
    else:
        best_val, best_move = float('inf'), None

    for move in game.moves(player):
        new_game = game.clone()
        new_game.do_move(move, player)
        val, _ = minimax(new_game, 1-player, depth-1, not isMaxPlayer, alpha, beta)
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
            if beta <= alpha:
                break
    
    return best_val, best_move



        



class Player(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.game = Reversi()
        self.my_player = 1
        self.say('RDY')

    def say(self, what):
        sys.stdout.write(what)
        sys.stdout.write('\n')
        sys.stdout.flush()

    def hear(self):
        line = sys.stdin.readline().split()
        return line[0], line[1:]

    def loop(self):
        CORNERS = { (0,0), (0,7), (7,0), (7,7)}
        while True:
            cmd, args = self.hear()
            if cmd == 'HEDID':
                unused_move_timeout, unused_game_timeout = args[:2]
                move = tuple((int(m) for m in args[2:]))
                if move == (-1, -1):
                    move = None
                self.game.do_move(move, 1 - self.my_player)
            elif cmd == 'ONEMORE':
                self.reset()
                continue
            elif cmd == 'BYE':
                break
            else:
                assert cmd == 'UGO'
                self.my_player = 0

            moves = self.game.moves(self.my_player)
            better_moves = list(set(moves) & CORNERS)

            _, move = minimax(self.game, self.my_player, 4, True, float('-inf'), float('inf'))

            if better_moves:
                move = random.choice(better_moves)
                self.game.do_move(move, self.my_player)    
            elif move:                
                self.game.do_move(move, self.my_player)
            else:
                self.game.do_move(None, self.my_player)
                move = (-1, -1)
            self.say('IDO %d %d' % move)


if __name__ == '__main__':
    player = Player()
    player.loop()