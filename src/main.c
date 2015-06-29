#include "main.h"
/*

SPAGHETTI CODE FOR EVERYONE
https://en.wikipedia.org/wiki/Spaghetti_code

*/
int main(){turn = 1;while(game_over()==0) {if(x !=0 && y != 0){printf("Current Box: x=%d,y=%d\n", x, y);printf("-----------\n");}print_board();take_move(1);system("clear");};system("clear");print_board();printf("Player%d Wins!", game_over());}void take_move(int pass){int x1;int y1;if(pass == 1){if(x==0 && y ==0){printf("Player%d, Select Starting box. Enter your move in the form: x,y\n", turn);}else{printf("Player%d, Enter your move in the form: x,y\n", turn);}}scanf("%d,%d",&x1,&y1);if(!legal(x1,y1)){printf("Move is illegal, try again\n");take_move(0);return;}if(x==0 && y==0){x = x1;y = y1;return;}Board[x-1][y-1].board[x1-1][y1-1] = turn;turn = (turn==1)? 2: 1;x = x1;y = y1;}