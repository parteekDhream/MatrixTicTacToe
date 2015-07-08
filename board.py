#!usr/bin/env python


import numpy
def print_board(mini_board):


	for i in range(3):
		print " ",
		for j in range(3):
			if board[i*3+j] == 1:
				print 'X',
			elif board[i*3+j] == 0:
				print 'O',
			else:
				print ' ',

			if j != 2:
				print " | ",
		print

		if i != 2:
			print "-----------------"
		else:
			print 
			

def print_board2 (board):
	for i in range(3):
		print " ",
		for j in range(3):
			if large_board[i*3+j] == 1:
				print 'X',
			elif board[i*3+j] == 0:
				print 'O',
			else:
				print ' ',

			if j != 2:
				print " | ",
		print

		if i != 2:
			print "-----------------"
		else:
			print 
			



mini_board=[]
for i in range (9):
	mini_board.append(-1)

large_board=[mini_board]



print_board(board)


