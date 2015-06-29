#include<stdio.h>
#ifndef BOARD_H
#define BOARD_H

typedef struct small_board{int board[3][3];} small_board;small_board Board[3][3];int turn;int x;int y;void print_board();int game_over();int legal(int y1,int x1);

#endif