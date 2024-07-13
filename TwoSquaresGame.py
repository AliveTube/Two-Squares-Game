import time as t
print("""Welcome to Two Square Game\n
This game is played on a board of 4x4 squares and two players take turns;
each of them takes turn to place a rectangle (that covers two squares) on the board, covering any 2 squares.
Only one rectangle can be on a square.
A square cannot be covered twice.
The last player who can place a card on the board is the winner.
""")
t.sleep(3)
print("Have fun :)")
bool = True
counter = 0
# A list for all possible numbers from 1 to 16
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
nums1 = []
nums2 = []
checking_winner = []
# The board where the players will play at
board =f"""                 ___________________________
                |  {nums[0]}   |  {nums[1]}   |  {nums[2]}   |  {nums[3]}   |
                |      |      |      |      |
                |______|______|______|______|
                |  {nums[4]}   |  {nums[5]}   |  {nums[6]}   |  {nums[7]}   |
                |      |      |      |      |
                |______|______|______|______|
                |  {nums[8]}   |  {nums[9]}  |  {nums[10]}  |  {nums[11]}  |
                |      |      |      |      |
                |______|______|______|______|
                |  {nums[12]}  |  {nums[13]}  |  {nums[14]}  |  {nums[15]}  |
                |      |      |      |      |
                |______|______|______|______|"""
print(board)

while bool:
    while True:
        # Taking inputs from The first Player
        try :
            print("Player_1 please enter two numbers")
            pl1,ppl1=map(str,input().split())
            if pl1.isdigit() and ppl1.isdigit():
                pl1 = int(pl1)
                ppl1 = int(ppl1)
            else:
                # Defensive programming for not taking strings
                print("Please enter two numbers not strings !")
                continue
            # Checking if the inputs were correct or not
            if (pl1 == 8 and ppl1 == 9) or (pl1 == 9 and ppl1 == 8) or (pl1 == 4 and ppl1 == 5) or (pl1 == 5 and ppl1 == 4) or (pl1 == 12 and ppl1 == 13) or (pl1 == 13 and ppl1 == 12):
                print("Please enter a valid moves ")
                continue
            # If the input was correct then the code will continue
            elif (pl1 not in nums1) and (ppl1 not in nums1) and  pl1 > 0 and ppl1 > 0 and (abs(pl1-ppl1) == 1  or abs(pl1-ppl1)==4) :
                # This code makes sure that the board don't get ruined
                if pl1 < 10 and ppl1 < 10 :
                    board = board.replace(str(nums[ppl1-1]),"X",1)
                    board = board.replace(str(nums[pl1-1]),"X",1)
                    nums1.append(pl1)
                    nums1.append(ppl1)
                elif pl1 < 10 and ppl1 >= 10:
                    board = board.replace(str(nums[ppl1-1]),"X ",1)
                    board = board.replace(str(nums[pl1-1]),"X",1)
                    nums1.append(pl1)
                    nums1.append(ppl1)
                elif pl1 >= 10 and ppl1 < 10 :
                    board = board.replace(str(nums[ppl1-1]),"X",1)
                    board = board.replace(str(nums[pl1-1]),"X ",1)
                    nums1.append(pl1)
                    nums1.append(ppl1)
                else:
                    board = board.replace(str(nums[ppl1-1]),"X ",1)
                    board = board.replace(str(nums[pl1-1]),"X ",1)
                    nums1.append(pl1)
                    nums1.append(ppl1)
                # Checking Winner
                if len(nums1) == 14 :
                    for i in nums :
                        if i not in nums1:
                            checking_winner.append(i)
                    if abs(checking_winner[0]-checking_winner[1]) != 4 and abs(checking_winner[0]-checking_winner[1]) != 1:
                        print(board)
                        print("Congratulations Player_1, You WON !! ")
                        exit()
                # Special case for Checking Winner
                elif len (nums1) == 12:
                    for i in nums:
                        if i not in nums1:
                            nums2.append(i)
                    if abs(nums2[0]-nums2[1]) != 1 and abs(nums2[0]-nums2[1]) != 4 and abs(nums2[1]-nums2[2]) != 1 and abs(nums2[1]-nums2[2]) != 4 and abs(nums2[2]-nums2[3]) != 1 and abs(nums2[2]-nums2[3]) != 4 and abs(nums2[1]-nums2[3]) != 1 and abs(nums2[1]-nums2[3]) != 4:
                        print("Congratulations Player_1, You WON !! ")
                        print(board)
                        exit()
                # Checking Winner
                elif len(nums1) == 16 :
                    print(board)
                    print("Congratulations Player_1, You WON !!")
                    exit()
                print(board)
                break
            # If the player entered a wrong input
            else:
                print("Please enter a valid input ! ")
                continue
        # If the player entered strings or anything other than integers
        except ValueError and IndexError:
            print("Please enter two numbers ")
    while True:
        # Taking inputs from The first Player
        try :
            print("Player_2 please enter two numbers")
            pl2,ppl2=map(str,input().split())
            if pl2.isdigit() and ppl2.isdigit():
                pl2 = int(pl2)
                ppl2 = int(ppl2)
            else:
                # Defensive programming for not taking strings
                print("Please enter two numbers not strings !")
                continue
            if (pl2 == 8 and ppl2 == 9) or (pl2 == 9 and ppl2 == 8) or (pl2 == 4 and ppl2 == 5) or (pl2 == 5 and ppl2 == 4) or (pl2 == 12 and ppl2 == 13) or (pl2 == 13 and ppl2 == 12):
                print("Please enter a valid moves ")
                continue
            # If the input was correct then the code will continue
            elif (pl2 not in nums1) and (ppl2 not in nums1) and (abs(pl2-ppl2) == 1  or abs(pl2-ppl2)==4) and pl2 > 0 and ppl2 > 0 :
                # This code makes sure that the board don't get ruined
                if pl2 < 10 and ppl2 < 10 :
                    board = board.replace(str(nums[ppl2-1]),"X",1)
                    board = board.replace(str(nums[pl2-1]),"X",1)
                    nums1.append(pl2)
                    nums1.append(ppl2)
                elif pl2 < 10 and ppl2 >= 10:
                    board = board.replace(str(nums[ppl2-1]),"X ",1)
                    board = board.replace(str(nums[pl2-1]),"X",1)
                    nums1.append(pl2)
                    nums1.append(ppl2)
                elif pl2 >= 10 and ppl2 < 10 :
                    board = board.replace(str(nums[ppl2-1]),"X",1)
                    board = board.replace(str(nums[pl2-1]),"X ",1)
                    nums1.append(pl2)
                    nums1.append(ppl2)
                else:
                    board = board.replace(str(nums[ppl2-1]),"X ",1)
                    board = board.replace(str(nums[pl2-1]),"X ",1)
                    nums1.append(pl2)
                    nums1.append(ppl2)
                if len(nums1) == 14 :
                    for i in nums :
                        if i not in nums1:
                            checking_winner.append(i)
                            print(checking_winner)
                    if abs(checking_winner[0]-checking_winner[1]) != 4 and abs(checking_winner[0]-checking_winner[1]) != 1:
                        print(board)
                        print("Congratulations Player_2, You WON !! ")
                        exit()
                elif len (nums1) == 12:
                    for i in nums:
                        if i not in nums1:
                            nums2.append(i)
                    if abs(nums2[0]-nums2[1]) != 1 and abs(nums2[0]-nums2[1]) != 4 and abs(nums2[1]-nums2[2]) != 1 and abs(nums2[1]-nums2[2]) != 4 and abs(nums2[2]-nums2[3]) != 1 and abs(nums2[2]-nums2[3]) != 4 and abs(nums2[1]-nums2[3]) != 1 and abs(nums2[1]-nums2[3]) != 4:
                        print(board)
                        print("Congratulations Player_2, You WON !! ")
                        exit()
                # Checking Winner
                elif len(nums1) == 16 :
                    print(board)
                    print("Congratulations Player_2, You WON !! ")
                    exit()
                print(board)
                break
            # If the player entered a wrong input
            else:
                print("Please enter a valid input ! ")
                continue
        # If the player entered strings or anything other than integers
        except ValueError and IndexError:
            print("Please enter two numbers ")
