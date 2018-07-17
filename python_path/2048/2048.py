#!/usr/bin/env python3
# -*- coding:utf8 -*-
import curses
from random import randrange
from random import choice
from collections import defaultdict
from matrix import transpose
from matrix import invert


class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset()

    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(self.width)
                         for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)]
                      for j in range(self.height)]
        # spawn 2
        self.spawn()
        self.spawn()

    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i):
                if row[i] == 0 and row[i+1] != 0:
                    # able to move
                    return True
                if row[i] != 0 and row[i+1] == row[i]:
                    # able to merge
                    return True
                return False
            return any(change(i) for i in range(len(row)-1))
        check = {}
        check['LEFT'] = lambda field: any(
            row_is_left_movable(row) for row in field)
        check['RIGHT'] = lambda field: check['LEFT'](invert(field))
        check['UP'] = lambda field: check['LEFT'](transpose(field))
        check['DOWN'] = lambda field: check['RIGHT'](transpose(field))
        if direction in check:
            return check[direction](self.field)
        return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def move(self, direction):
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row = [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2*row[i])
                        self.score += 2*row[i]
                        pair = False
                    else:
                        if i+1 < len(row) and row[i] == row[i+1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))
        moves = {}
        moves['LEFT'] = lambda field: [move_row_left(row) for row in field]
        moves['RIGHT'] = lambda field: invert(moves['LEFT'](invert(field)))
        moves['UP'] = lambda field: transpose(moves['LEFT'](transpose(field)))
        moves['DOWN'] = lambda field: transpose(
            moves['RIGHT'](transpose(field)))
        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def draw(self, screen):
        help_string1 = "(W)UP (S)DOWN (A)LEFT (D)RIGHT"
        help_string2 = "(R)RESTART (Q)EXIT"
        gameover_string = "Game Over"
        win_string = "You made it"

        def cast(string):
            screen.addstr(string+'\n')

        def draw_hor_separator():
            line = '*'+('+------'*self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num >
                         0 else '|      ' for num in row)+'|')
        screen.clear()
        cast('SCORE: '+str(self.score))
        if 0 != self.highscore:
            cast('HIGHSCORE: '+str(self.highscore))
        for row in self.field:
            draw_hor_separator()
            draw_row(row)
        draw_hor_separator()
        if self.is_win():
            cast(win_string)
        elif self.is_gameover():
            cast(gameover_string)
        else:
            cast(help_string1)
        cast(help_string2)


INIT = 0
GAME = 1
WIN = 3
LOSE = 4
EXIT = 5
actions = ['UP', 'LEFT', 'DOWN', 'RIGHT', 'RESTART', 'EXIT']
letters_codes = [ord(ch) for ch in 'WASDRQwasdrq']
# register letter codes to actions
actions_dict = dict(zip(letters_codes, actions*2))


def main(stdscr):
    game_field = GameField(win=2048)

    def init():
        game_field.reset()
        return GAME

    def get_user_action(keyboard):
        action_char = "N"
        # the parameter keyboard in this situaction is stdscr at main function
        while action_char not in actions_dict:
            action_char = keyboard.getch()
        return actions_dict[action_char]

    def end_game(status):
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: status)
        responses['RESTART'], responses['EXIT'] = INIT, EXIT
        return responses[action]

    def game():
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        if action == "RESTART":
            return INIT
        if action == "EXIT":
            return EXIT
        if game_field.move(action):
            if game_field.is_win():
                return WIN
            if game_field.is_gameover():
                return LOSE
        return GAME

    state_actions = {INIT: init, WIN: end_game(
        WIN), LOSE: end_game(LOSE), GAME: game}

    curses.use_default_colors()
    status = INIT
    while status != EXIT:
        status = state_actions[status]()


curses.wrapper(main)
