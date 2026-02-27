Diction_board = {'7': ' ', '8': ' ', '9': ' ',
           '4': ' ', '5': ' ', '6': ' ',
           '1': ' ', '2': ' ', '3': ' '}
tic_tac_keys = []
for key in Diction_board:
    tic_tac_keys.append(key)

def board_print(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('--+--+--')
    print(board['4'] + '|' + board['5'] + '|' + board['4'])
    print('--+--+--')
    print(board['1'] + '|' + board['2'] + '|' + board['1'])

def game():
    turn = 'x'
    count = 0

    for i in range(10):
        board_print(Diction_board)
        print('Its your turn.' + turn + 'Move to which place?')
        move = input()
        if Diction_board[move] == ' ':
            Diction_board[move] = turn
            count+=1
        else:
            print('Thats filled \nMove to another part')
            continue
        if count >= 5:
            if Diction_board['7'] == Diction_board['8'] == Diction_board['9'] != ' ':
                board_print(Diction_board)
                print('Game over! \n')
                print('****' + turn + 'won.****')
                break

            elif Diction_board['4'] == Diction_board['5'] == Diction_board['6'] != ' ':
                board_print(Diction_board)
                print('Game over! \n')
                print('****' + turn + 'won.****')
                break

            elif Diction_board['1'] == Diction_board['2'] == Diction_board['3'] != ' ':
                board_print(Diction_board)
                print('Game over! \n')
                print('****' + turn + 'won.****')
                break

            #vertical
            elif Diction_board['1'] == Diction_board['4'] == Diction_board['7'] != ' ':
                board_print(Diction_board)
                print('Game over! \n')
                print('****' + turn + 'won.****')
                break

            elif Diction_board['8'] == Diction_board['5'] == Diction_board['6'] != ' ':
                board_print(Diction_board)
                print('Game over! \n')
                print('****' + turn + 'won.****')
                break

            elif Diction_board['9'] == Diction_board['6'] == Diction_board['3'] != ' ':
                board_print(Diction_board)
                print('Game over! \n')
                print('****' + turn + 'won.****')
                break

            #diagonal
            elif Diction_board['7'] == Diction_board['5'] == Diction_board['3'] != ' ':
                board_print(Diction_board)
                print('Game over! \n')
                print('****' + turn + 'won.****')
                break

            elif Diction_board['9'] == Diction_board['5'] == Diction_board['1'] != ' ':
                board_print(Diction_board)
                print('Game over! \n')
                print('****' + turn + 'won.****')
                break

            if count == 9:
                print('Game over!')
                print('Its a tie!')
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'

            restart = input('Do you want to play again? (y/n): ')
            if restart == 'y' or 'Y':
                for key in tic_tac_keys:
                    Diction_board[key] = ' '
                    game()

if __name__ == '__main__':
    game()