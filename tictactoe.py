import random

kEmpty = '?'
kPlayer1Mark = 'X'
kPlayer2Mark = 'O'
players = {1:kPlayer1Mark, 2:kPlayer2Mark}
board = [[kEmpty]*3 for _ in range(3)]

def DrawBoard():
    for r in range(3):
        line_txt=''
        for c in range(3):
            line_txt+=board[r][c]
        print(line_txt)
    print('')

def PutMarker(mark,r,c):
    if r<0 or r>3 or c<0 or c>3: return False
    if mark not in [kPlayer1Mark, kPlayer2Mark]: return False
    if board[r][c] != kEmpty: return False
    board[r][c] = mark
    return True

player_num = random.randint(1,2)
while True:
    DrawBoard()
    
    marker_valid = False
    while not marker_valid:
        if player_num==2:#bot
            r=random.randint(0,2)
            c=random.randint(0,2)
        else:
            while True:
                markstr = input("Player{}, put your mark as R,C. E.g. 2,2: ".format(player_num))
                if markstr in ['q','Q','quit','Quit']: exit(0)
                splitted = markstr.split(",")
                if len(splitted)!=2: continue
                try:
                    r=int(splitted[0])
                    c=int(splitted[1])
                except:
                    continue
                break
        marker_valid = PutMarker(players[player_num],r,c)
    player_num+=1
    if player_num==3: player_num=1
