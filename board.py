#!usr/bin/env python



def print_board(board):


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

			


board =[]
for i in range (9):
	board.append(-1)


print_board(board)