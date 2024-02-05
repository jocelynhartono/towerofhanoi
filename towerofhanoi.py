import time
import os
from termcolor import colored

def loadingTime():
    print(colored('Please wait', 'red'))
    loading = "- "
    notcomplete = True
    i = 0
    while notcomplete:
        output = (loading*i)
        print(colored(output, 'red'), end = '\r')
        time.sleep(.5)
        i += 1
        if i == 10:
            os.system('clear')
            break

def printMenu():
    print(colored('Game:\n1.Rules\n2.Play\n3.Best History\n4.Quit', 'blue'))
    menuChoice = ""
    while menuChoice != '1' and menuChoice !='2' and menuChoice !='3' and menuChoice !='4':
        menuChoice = input(colored('Please enter your choice (1~4): ', 'blue'))
    return int(menuChoice)

def printMenu1():
    print('''Rules: 
    There are 3 polars 1,2,3. Our goal is to transport all rings from polar 1 to polar 3 without changing the order.
    Only one disk can be moved at a time.
    Each move consists of taking the upper ring from one of the polars and placing it on top of another polar. 
    A ring can only be moved if it is the uppermost ring on a polar.
    No larger ring may be placed on top of a smaller ring.
    Try to finish the task in the least moves!
    Press enter to return to menu''')
    if input() == "":
        main()
        
def printMenu2():
    def printBoard(board,level):
        if level == 'easy':
            for i in range(3):
                print((board[0][i]).center(7),(board[1][i]).center(7),(board[2][i]).center(7))
            print(('[1]').center(7),('[2]').center(7),('[3]').center(7))
        if level == 'medium':
            for i in range(5):
                print((board[0][i]).center(11),(board[1][i]).center(11),(board[2][i]).center(11))
            print(('[1]').center(11),('[2]').center(11),('[3]').center(11))
        if level == 'hard':
            for i in range(7):
                print((board[0][i]).center(15),(board[1][i]).center(15),(board[2][i]).center(15))
            print(('[1]').center(15),('[2]').center(15),('[3]').center(15))

    def getChoice(board,rings):
        def getRing(rings):
            ringNum = ""
            while not(ringNum.isnumeric()):
                ringNum=input('Please select a ring: ')
            ringNum = int(ringNum)
            while ringNum < 1 or ringNum > len(board[0]):
                print('Error: ring out of range')
                ringNum = ""
                while not(ringNum.isnumeric()):
                    ringNum=input('Please select a ring: ')
                ringNum = int(ringNum)
            ring_=rings[ringNum]
            return ring_
        
        def findRing(ring):
            for i in range(3):
                for j in range(len(board[0])):
                    if board[i][j]==ring:
                        return i,j
                        break
        
        def validTest(bnum,index):
            #See if the ring is on top
            if index==0:
                return True
            elif board[bnum][index-1]!='|':
                return False
        
        ring=getRing(rings)
        bnum,index=findRing(ring)
        while validTest(bnum,index)==False:
            print('Error: ring not on top')
            ring=getRing(rings)
            bnum,index=findRing(ring)
        return bnum,index

    def move(i,j,board):
        def choosePolar():
            choice = ""
            while not (choice.isnumeric()):
                choice=input('Please select a polar: ')
            choice = int(choice) -1
            while choice >2 or choice <0:
                print('Error: polar out of range')
                choice = ""
                while not (choice.isnumeric()):
                    choice=input('Please select a polar: ')
                choice = int(choice) -1
            return choice
        
        choice=choosePolar()
        Index=len(board[0])-1
        while board[choice][Index]!='|' and choice!=i:
            Index-=1
        if Index != len(board[0])-1:
            while (len(board[choice][Index+1])+1)/2 < (len(board[i][j])+1)/2:
                print('Error: invalid move')
                choice=choosePolar()
                if choice==i:
                    break
                Index=len(board[0])-1
                while board[choice][Index]!='|' and choice!=i:
                    Index-=1
                if Index == len(board[0])-1:
                    break
        if choice!=i:
            board[choice][Index]=board[i][j]
            board[i][j]='|'

    level = ""
    while level != "easy" and level != "medium" and level != "hard":        
        level=input('Please choose difficulty level (easy,medium,hard): ')
    try:
        global bestHistory
        cnt=0
        if level == 'easy':
            rings={1:'1',2:'222',3:'33333'}
            board=[[('1'),('222'),('33333')],\
                    ['|','|','|'],\
                    ['|','|','|']]
            printBoard(board,level)           
            while board[2]!=[('1'),('222'),('33333')]:
                i,j=getChoice(board,rings)
                move(i,j,board)
                print()
                cnt+=1
                printBoard(board,level)
            print(f"Yeah! You finished in {cnt} moves")
            if bestHistory[0][2]=='None':
                bestHistory[0][1]=input("You break the record! Please enter your name: ")
                bestHistory[0][2]=str(cnt)
            elif int(bestHistory[0][2])>cnt:
                bestHistory[0][1]=input("You break the record! Please enter your name: ")
                bestHistory[0][2]=str(cnt)
        
        if level == 'medium':
            rings={1:'1',2:'222',3:'33333',4:'4444444',5:'555555555'}
            board=[[('1'),('222'),('33333'),('4444444'),('555555555')],\
                    ['|','|','|','|','|'],\
                    ['|','|','|','|','|']]
            printBoard(board,level)           
            while board[2]!=[('1'),('222'),('33333'),('4444444'),('555555555')]:
                i,j=getChoice(board,rings)
                move(i,j,board)
                print()
                cnt+=1
                printBoard(board,level)
            print(f"Yeah! You finished in {cnt} moves")
            if bestHistory[1][2]=='None':
                bestHistory[1][1]=input("You break the record! Please enter your name: ")
                bestHistory[1][2]=str(cnt)
            elif int(bestHistory[1][2])>cnt:
                bestHistory[1][1]=input("You break the record! Please enter your name: ")
                bestHistory[1][2]=str(cnt)
    
        if level == 'hard':
            rings={1:'1',2:'222',3:'33333',4:'4444444',5:'555555555',6:'66666666666',7:'7777777777777'}
            board=[[('1'),('222'),('33333'),('4444444'),('555555555'),('66666666666'),('7777777777777')],\
                    ['|','|','|','|','|','|','|'],\
                    ['|','|','|','|','|','|','|']]
            printBoard(board,level)           
            while board[2]!=[('1'),('222'),('33333'),('4444444'),('555555555'),('66666666666'),('7777777777777')]:
                i,j=getChoice(board,rings)
                move(i,j,board)
                print()
                cnt+=1
                printBoard(board,level)
            print(f"Yeah! You finished in {cnt} moves")
            if bestHistory[2][2]=='None':
                bestHistory[2][1]=input("You break the record! Please enter your name: ")
                bestHistory[2][2]=str(cnt)
            elif int(bestHistory[2][2])>cnt:
                bestHistory[2][1]=input("You break the record! Please enter your name: ")
                bestHistory[2][2]=str(cnt)

        print('Press enter to continue')
        if input()=="":
            main()
    except(KeyboardInterrupt):
        print()
        print(colored("Bye!","green"))

def printMenu3(L):
    print(colored("------*Leaderboard*------",'yellow'))
    print("Level".center(7),"Username".center(10),"Moves".center(5))
    for i in range(3):
        print(L[i][0].center(7),L[i][1].center(10),L[i][2].center(5))
    print('Press enter to continue')
    if input()=="":
        main()

bestHistory = [['Easy','None','None'],['Medium','None','None'],['Hard','None','None']]

def printMenu4():
    quit = ''
    while quit != 'yes' and quit != 'no':
        quit = input(colored('Are you sure you want to quit? (yes/no)\n', 'red'))
    if quit == 'yes':
        print(colored('Bye!', 'green'))
    elif quit == 'no':
        main()

def main():
    section = printMenu()
    if section == 1:
        printMenu1()
    elif section == 2:
        printMenu2()
    elif section == 3:
        printMenu3(bestHistory)
    elif section == 4:
        printMenu4()


print(colored('Welcome to ENGG1330 Tower of Hanoi', 'blue'))
loadingTime()   
main()