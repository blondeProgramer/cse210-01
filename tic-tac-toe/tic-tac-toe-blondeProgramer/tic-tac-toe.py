# CSE 210
# Developer - Solo Code Submission
# Tic Tac Toe game
#
# by Alina Zalozna

def main():
    """Main function"""
    
    print("Welcome to the Tic Tac Toe!\n")
    
    # get size of array for the future board
    # and check the correct value
    # (max size = 10 for normal drawing)
    board_size = 0
    while board_size < 3 or board_size > 10:
        try:
            board_size = int(input("Please, enter the size of board (min 3, max 10): "))
            #check entering data
        except:
            print("\033[91mPlease, enter correct number\033[0m")
    
    # create and fill two-dimmensional array
    board = [0] * board_size
    next_num = 1
    for i in range(board_size):
        board[i] = [0] * board_size
        for j in range(board_size):
            board[i][j] = str(next_num)
            next_num += 1

    # print start info
    print("\n\33[32mOK! GAME STARTING!\033[0m\n")
    num_of_steps = 0
    while is_win(board, board_size) == False:
        print("YOUR BOARD NOW:")
        drawing_board(board, board_size)
              
        if num_of_steps == board_size**2:
            print("Draw!!!")
            exit()

        num_cell = 0
        # getting cell with checking fill and correct choose
        while True:
            try:
                if num_of_steps%2 == 0:
                    num_cell = int(input("Player X, choose your cell: "))
                else:
                    num_cell = int(input("Player O, choose your cell: "))
            except:
                print("\033[91mPlease, enter correct number\033[0m")
                continue
            if num_cell < 1 or num_cell > board_size**2 :
                print("\033[91mPlease, enter number from board\033[0m")
                continue
            new_i = int((num_cell - 1) / board_size)
            new_j = (num_cell - 1) % board_size
            if board[new_i][new_j] == "X" or board[new_i][new_j] == "O":
                print("\033[91mPlease, choose cell with number!\033[0m")
                continue
            break
        if num_of_steps%2 == 0:
            board[new_i][new_j] = "X"
        else:
            board[new_i][new_j] = "O"

        num_of_steps += 1  

def drawing_board (board, board_size):
    """
    This function drawing the game board from the two-dimensional array

    Parameter
        board - two-dimensional array of char type
        board_size - size of first line array

    Return
        nothing    
    """

    for i in range(board_size):
        for j in range(board_size-1):
            print(f"{board[i][j]: ^3}║", end='')
        print(f"{board[i][board_size-1]: ^3}")
        
        if(i < board_size-1):
            for j in range(board_size-1):
                print("═══╬", end='')
            print("═══")

def is_win(board, board_size):
    """
    This function check array for finding win combination
    
    Parameter
        board - two-dimensional array of char type
        board_size - size of first line array

    Return
        True/False 
    """
    # check horisontal lines
    for i in range(board_size):
        first_flag = board[i][0]
        num_of_same = 0
        for j in range(board_size):
            if first_flag != board[i][j]:
                break
            num_of_same += 1
        if num_of_same == board_size:
            drawing_board(board, board_size)
            print(f"{first_flag} WIN!!!")
            return True
    
    # check vertical lines
    for i in range(board_size):
        first_flag = board[0][i]
        num_of_same = 0
        for j in range(board_size):
            if first_flag != board[j][i]:
                break
            num_of_same += 1
        if num_of_same == board_size:
            drawing_board(board, board_size)
            print(f"{first_flag} WIN!!!")
            return True
    
    # check left diagonal line
    first_flag = board[0][0]
    num_of_same = 0
    for i in range(board_size):
        if first_flag != board[i][i]:
            break
        else:
            num_of_same += 1
    if num_of_same == board_size:
        drawing_board(board, board_size)
        print(f"{first_flag} WIN!!!")
        return True

    # check right diagonal line
    first_flag = board[0][board_size-i-1]
    num_of_same = 0
    for i in range(board_size):
        if first_flag != board[i][board_size-i-1]:
            break
        else:
            num_of_same += 1
    if num_of_same == board_size:
        drawing_board(board, board_size)
        print(f"{first_flag} WIN!!!")
        return True

    return False




if __name__ == "__main__":
    main()