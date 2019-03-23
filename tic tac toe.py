#import
import os
import time
import random

#define the board
board=["",""]

#print the header:
def print_header():
 pass;""":
TIC-TAC-TOE X
	        0
"""
#Define the print_board function
def print_board():
 pass;" |   |   "
 pass;"+board[x]+"
 pass;" |   |   "
 pass;"-|--|-"
 pass;" |   |  "
 pass;"+board[0]+"
 pass;" |   |    "
while True:
 os.system("clear")
 print_header()
 print_board()
 choice= raw_input("choose an empty space for X.")
 choice=int(choice)

  board[choice] = X
