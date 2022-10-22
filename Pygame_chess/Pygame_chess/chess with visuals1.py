import pygame
from sys import exit

screen = pygame.display.set_mode((480,480))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

#transparent
transparent = (0, 0, 0, 0)

#Black Pieces:
Black_pieces = {'bP':pygame.image.load('Black/bPawn.png'),
                'bR':pygame.image.load('Black/bRook.png'),
                'bK':pygame.image.load('Black/bKing.png'),
                'bB':pygame.image.load('Black/bBishop.png'),
                'bQ':pygame.image.load('Black/bQueen.png'),
                'bN':pygame.image.load('Black/bKnight.png')}

#White Pieces:
White_pieces=  {'wP':pygame.image.load('White/wPawn.png'),
                'wR':pygame.image.load('White/wRook.png'),
                'wK':pygame.image.load('White/wKing.png'),
                'wB':pygame.image.load('White/wBishop.png'),
                'wQ':pygame.image.load('White/wQueen.png'),
                'wN':pygame.image.load('White/wKnight.png')}

#Background:
BG1 = pygame.image.load('BG/bg1.png')
BG2 = pygame.image.load('BG/bg2.png')
BG3 = pygame.image.load('BG/bg3.png')



def play_game():

    board=[      [7,'bR','bN','bB','bQ','bK','bB','bN','bR'],
                 [6,'bP','bP','bP','bP','bP','bP','bP','bP'],
                 [5,'--','--','--','--','--','--','--','--'],
                 [4,'--','--','--','--','--','--','--','--'],
                 [3,'--','--','--','--','--','--','--','--'],
                 [2,'--','--','--','--','--','--','--','--'],
                 [1,'wP','wP','wP','wP','wP','wP','wP','wP'],
                 [0,'wR','wN','wB','wQ','wK','wB','wN','wR'],
               ['   0','  1',' 2',' 3',' 4',' 5',' 6',' 7']]
    
    game_position_of_black={'bP1':[0,6],
                   'bP2':[1,6],
                   'bP3':[2,6],
                   'bP4':[3,6],
                   'bP5':[4,6],
                   'bP6':[5,6],
                   'bP7':[6,6],
                   'bP8':[7,6],
                   'bR1':[0,7],
                   'bN1':[1,7],
                   'bB1':[2,7],
                   'bKk':[4,7],
                   'bQq':[3,7],
                   'bB2':[5,7],
                   'bN2':[6,7],
                   'bR2':[7,7]}

    game_position_of_white={'wP1':[0,1],
                   'wP2':[1,1],
                   'wP3':[2,1],
                   'wP4':[3,1],
                   'wP5':[4,1],
                   'wP6':[5,1],
                   'wP7':[6,1],
                   'wP8':[7,1],
                   'wR1':[0,0],
                   'wN1':[1,0],
                   'wB1':[2,0],
                   'wQq':[3,0],
                   'wKk':[4,0],
                   'wB2':[5,0],
                   'wN2':[6,0],
                   'wR2':[7,0]}

    white_keys = list(game_position_of_white.keys())
    white_coords = list(game_position_of_white.values())
    black_keys = list(game_position_of_black.keys())
    black_coords = list(game_position_of_black.values())


    def Knight(i_coord,j_coord):
        a=i_coord
        b=j_coord
        avl_coords=[]

        for i in range(1,3):
            for j in range(2,0,-1):
                if (i==1) and (j==2):
                    p1=[a+i,b+j]
                    p2=[a+i,b-j]
                    p3=[a-i,b+j]
                    p4=[a-i,b-j]
                elif (i==2) and (j==1):
                    p5=[a+i,b+j]
                    p6=[a+i,b-j]
                    p7=[a-i,b+j]
                    p8=[a-i,b-j]

                else:
                    pass
        p_coords=[p1,p2,p3,p4,p5,p6,p7,p8]

        for i in (p_coords):
            if (i[0]>=0 and i[0]<=7) and (i[1]>=0 and i[1]<=7):
                avl_coords.append(i)
            else:
                pass
        return(avl_coords)

    def check_Knight_white(i_coord,j_coord):
        a=Knight(i_coord,j_coord)
        pos_for_Knight=[]
        b=list(game_position_of_black.values())

        for i in a:
            if i in b:
                pos_for_Knight.append(i)
                
        
        for i in (a):
            line_in=(i[1]-7)//-1
            pos_inline=i[0]+1
            w=board[line_in][pos_inline]
            if (w=='--'):
                pos_for_Knight.append(i)
            
           
        return(pos_for_Knight)

    def Bishop(i_coord,j_coord):
        pos_coords1=[]
        pos_coords2=[]
        pos_coords3=[]
        pos_coords4=[]
        avl_coords=[]
        a=i_coord
        b=j_coord

        for i in range (1,8):
            pos_xy1=[a+i,b+i]
            pos_xy2=[a-i,b-i]

            pos_yx1=[a-i,b+i]
            pos_yx2=[a+i,b-i]

            if (pos_xy1[0]>=0 and pos_xy1[0]<=7) and (pos_xy1[1]>=0 and pos_xy1[1]<=7):
                pos_coords1.append(pos_xy1)
            else:
                pass

            if (pos_xy2[0]>=0 and pos_xy2[0]<=7) and (pos_xy2[1]>=0 and pos_xy2[1]<=7):
                pos_coords2.append(pos_xy2)
            else:
                pass

            if (pos_yx1[0]>=0 and pos_yx1[0]<=7) and (pos_yx1[1]>=0 and pos_yx1[1]<=7):
                pos_coords3.append(pos_yx1)
            else:
                pass

            if (pos_yx2[0]>=0 and pos_yx2[0]<=7) and (pos_yx2[1]>=0 and pos_yx2[1]<=7):
                pos_coords4.append(pos_yx2)
            else:
                pass
                
        avl_coords=[pos_coords1,pos_coords2,pos_coords3,pos_coords4]
        return(avl_coords)

    def check_Bishop_white(i_coord,j_coord):
        a=Bishop(i_coord,j_coord)
        pos_for_Bishop=[]
        for i in (a):
            if i!=[]:
                for j in (i):
                    line_in=(j[1]-7)//-1
                    pos_inline=j[0]+1
                    w=board[line_in][pos_inline]
                    b=list(game_position_of_black.values())
                    if j in b:
                        pos_for_Bishop.append(j)
                    if (w=='--'):
                        pos_for_Bishop.append(j)
                   
                    else:
                        break
                        
            else:
                pass
        return(pos_for_Bishop)

    def Rook(i_coord,j_coord):
        pos_coords1=[]
        pos_coords2=[]
        pos_coords3=[]
        pos_coords4=[]
        avl_coords=[]
        a=i_coord
        b=j_coord

        for i in range (1,8):
            pos_xy1=[a,b+i]
            pos_xy2=[a,b-i]

            pos_yx1=[a-i,b]
            pos_yx2=[a+i,b]

            if (pos_xy1[0]>=0 and pos_xy1[0]<=7) and (pos_xy1[1]>=0 and pos_xy1[1]<=7):
                pos_coords1.append(pos_xy1)
            else:
                pass

            if (pos_xy2[0]>=0 and pos_xy2[0]<=7) and (pos_xy2[1]>=0 and pos_xy2[1]<=7):
                pos_coords2.append(pos_xy2)
            else:
                pass

            if (pos_yx1[0]>=0 and pos_yx1[0]<=7) and (pos_yx1[1]>=0 and pos_yx1[1]<=7):
                pos_coords3.append(pos_yx1)
            else:
                pass

            if (pos_yx2[0]>=0 and pos_yx2[0]<=7) and (pos_yx2[1]>=0 and pos_yx2[1]<=7):
                pos_coords4.append(pos_yx2)
            else:
                pass
                
        avl_coords=[pos_coords1,pos_coords2,pos_coords3,pos_coords4]
        return(avl_coords)

    def check_Rook_white(i_coord,j_coord):
        a=Rook(i_coord,j_coord)
        pos_for_Rook=[]
        for i in (a):
            if i!=[]:
                for j in (i):
                    line_in=(j[1]-7)//-1
                    pos_inline=j[0]+1
                    w=board[line_in][pos_inline]
                    b=list(game_position_of_black.values())
                    if j in b:
                        pos_for_Rook.append(j)
                    if (w=='--'):
                        pos_for_Rook.append(j)
                   
                    else:
                        break
                        
            else:
                pass
        return(pos_for_Rook)


    def Queen(i_coord,j_coord):
        pos_coords1=[]
        pos_coords2=[]
        pos_coords3=[]
        pos_coords4=[]
        avl_coords=[]
        a=i_coord
        b=j_coord

        for i in range (1,8):
                pos_xy1=[a+i,b+i]
                pos_xy2=[a-i,b-i]

                pos_yx1=[a-i,b+i]
                pos_yx2=[a+i,b-i]

                if (pos_xy1[0]>=0 and pos_xy1[0]<=7) and (pos_xy1[1]>=0 and pos_xy1[1]<=7):
                    pos_coords1.append(pos_xy1)
                else:
                    pass

                if (pos_xy2[0]>=0 and pos_xy2[0]<=7) and (pos_xy2[1]>=0 and pos_xy2[1]<=7):
                    pos_coords2.append(pos_xy2)
                else:
                    pass

                if (pos_yx1[0]>=0 and pos_yx1[0]<=7) and (pos_yx1[1]>=0 and pos_yx1[1]<=7):
                    pos_coords3.append(pos_yx1)
                else:
                    pass

                if (pos_yx2[0]>=0 and pos_yx2[0]<=7) and (pos_yx2[1]>=0 and pos_yx2[1]<=7):
                    pos_coords4.append(pos_yx2)
                else:
                    pass

        pos_coords5=[]
        pos_coords6=[]
        pos_coords7=[]
        pos_coords8=[]
        avl_coords=[]
        a=i_coord
        b=j_coord
        for i in range (1,8):
                pos_xy1=[a,b+i]
                pos_xy2=[a,b-i]

                pos_yx1=[a-i,b]
                pos_yx2=[a+i,b]


                if (pos_xy1[0]>=0 and pos_xy1[0]<=7) and (pos_xy1[1]>=0 and pos_xy1[1]<=7):
                    pos_coords5.append(pos_xy1)
                else:
                    pass

                if (pos_xy2[0]>=0 and pos_xy2[0]<=7) and (pos_xy2[1]>=0 and pos_xy2[1]<=7):
                    pos_coords6.append(pos_xy2)
                else:
                    pass

                if (pos_yx1[0]>=0 and pos_yx1[0]<=7) and (pos_yx1[1]>=0 and pos_yx1[1]<=7):
                    pos_coords7.append(pos_yx1)
                else:
                    pass

                if (pos_yx2[0]>=0 and pos_yx2[0]<=7) and (pos_yx2[1]>=0 and pos_yx2[1]<=7):
                    pos_coords8.append(pos_yx2)
                else:
                    pass            
        avl_coords=[pos_coords1,pos_coords2,pos_coords3,pos_coords4,pos_coords5,pos_coords6,pos_coords7,pos_coords8]
        return(avl_coords)


    def check_Queen_white(i_coord,j_coord):
        a=Queen(i_coord,j_coord)
        pos_for_Queen=[]
        for i in (a):
            if i!=[]:
                for j in (i):
                    line_in=(j[1]-7)//-1
                    pos_inline=j[0]+1
                    w=board[line_in][pos_inline]
                    b=list(game_position_of_black.values())
                    if j in b:
                        pos_for_Queen.append(j)
                    if (w=='--'):
                        pos_for_Queen.append(j)
                   
                    else:
                        break
                        
            else:
                pass
        return(pos_for_Queen)


    def King(i_coord,j_coord):
        avl_coords=[]
        a=i_coord
        b=j_coord

        pos_coord=[[a,b+1],[a,b-1],[a+1,b],[a-1,b],[a+1,b+1],[a-1,b-1],[a-1,b+1],[a+1,b-1]]
        for i in (pos_coord):
            if (i[0]>=0 and i[0]<=7) and (i[1]>=0 and i[1]<=7):
                avl_coords.append(i)
            else:
                pass
        return(avl_coords)


    def check_King_white(i_coord,j_coord):
        a=King(i_coord,j_coord)
        pos_for_King=[]
        for i in (a):
                    line_in=(i[1]-7)//-1
                    pos_inline=i[0]+1
                    w=board[line_in][pos_inline]
                    b=list(game_position_of_black.values())
                    if i in b:
                        pos_for_King.append(i)
                    if (w=='--'):
                        pos_for_King.append(i)
                   
                    else:
                        break
        return(pos_for_King)


    def PawnWhite(i_coord,j_coord):
        avl_coords=[]
        a=i_coord
        b=j_coord

        if b==1:
            avl_coords=[[a,2],[a,3]]
        elif b>1:
            avl_coords=[[a,b+1]]
        return(avl_coords)

    def check_PawnWhite(i_coord,j_coord):
        a=PawnWhite(i_coord,j_coord)#[[3,2],[3,4]]
        pos_for_PawnWhite=[]
            
        if len (a)==2:
                   line_in=(a[0][1]-7)//-1
                   pos_inline=a[0][0]+1
                   w=board[line_in][pos_inline]
                   b=list(game_position_of_black.values())
                   i=a[0]
                   c1=i[0]-1
                   c2=i[1]
                   d1=i[0]+1
                   d2=i[1]
                   l1=[c1,c2]
                   l2=[d1,d2]
                   if l2 in b:
                           pos_for_PawnWhite.append(l2)
                   if l1 in b:
                           pos_for_PawnWhite.append(l1)
                       
                   
                   if (w=='--'):
                          pos_for_PawnWhite.append(a[0])
                          pos_for_PawnWhite.append(a[1])
                        
                   
          
                          
                   else:
                              pass
        if len(a)==1:
                   line_in=(a[0][1]-7)//-1
                   pos_inline=a[0][0]+1
                   w=board[line_in][pos_inline]
                   b=list(game_position_of_black.values())
                   for i in a:
                       c1=i[0]-1
                       c2=i[1]
                       d1=i[0]+1
                       d2=i[1]
                       l1=[c1,c2]
                       l2=[d1,d2]
                       if l2 in b:
                           pos_for_PawnWhite.append(l2)
                       if l1 in b:
                           pos_for_PawnWhite.append(l1)
                   if (w=='--'):
                          pos_for_PawnWhite.append(a[0])
                   else:
                              pass
        return(pos_for_PawnWhite)





    def move_coins(char_pressed, coords_box):  #do for black also

        if (char_pressed == 'wN1' or  char_pressed=='wN2'):
            pos_moves = check_Knight_white(coords_box[0],coords_box[1])
            
            print(pos_moves)
            ani_pos(pos_moves)
            return([pos_moves, coords_box])

        if (char_pressed == 'wR1' or  char_pressed=='wR2'):
            pos_moves = check_Rook_white(coords_box[0],coords_box[1])
            ani_pos(pos_moves)

        if (char_pressed == 'wB1' or  char_pressed=='wB2'):
            pos_moves = check_Bishop_white(coords_box[0],coords_box[1])
            ani_pos(pos_moves)

        if (char_pressed=='wQq'):
            pos_moves = check_Queen_white(coords_box[0],coords_box[1])
            ani_pos(pos_moves)

        if (char_pressed == 'wKk'):
            pos_moves = check_King_white(coords_box[0],coords_box[1])
            ani_pos(pos_moves)

        for i in range (1,9):
            if (char_pressed == 'wP' + str(i)):
                pos_moves = check_PawnWhite(coords_box[0],coords_box[1])
                print(pos_moves)
                ani_pos(pos_moves)                
                return([pos_moves, coords_box])
                break


    def ani_pos(pos_moves):        
        for coord in (pos_moves):
            x = coord[0]
            y = 7-coord[1]            
            screen.blit(BG3,(x*60,y*60))
            
           
    def move_selected_piece(org_col, org_pos, going_pos, piece, nos_going_pos): # complete it last def add change_pos_inode
        screen.blit(org_col,org_pos)
        for i in range(nos_going_pos):
             print(i)
             if ((blue_square[0][i][0]) + (blue_square[0][i][1]))%2==0:
                 going_col = BG2
                 screen.blit(going_col,[blue_square[0][i][0]*60,(7-blue_square[0][i][1])*60])
             else:
                 going_col = BG1
                 screen.blit(going_col,[blue_square[0][i][0]*60,(7-blue_square[0][i][1])*60])
                
        screen.blit(piece,going_pos)
        print(org_pos,going_pos)


    '''def change_pos_incode(piece,org_pos,going_pos):#have to finish(change current pos in board and dict) 
        game_position_of_white[piece] = coords_box1
        org_coords = [org_pos[0]//60, org_pos[1]//60]
        going_coords = [going_pos[0]//60, going_pos[1]//60]

        if board[going_coords
        '''
        
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:                       #makes that it triggers only once when key is pressed
                mouse_presses = pygame.mouse.get_pressed()                 
                if mouse_presses[0]:                                    #gives a boolean of (x,y,z) of left ,middle, right key if pressed
                    x = pygame.mouse.get_pos()                             #gives tuple of (x,y) coord relative to top left
                    coords_boxs = [x[0]//60, 7-(x[1]//60)]


                    if coords_boxs in white_coords:                      #FOR WHITE
                        coords_box = coords_boxs                        
                        pos_char = white_coords.index(coords_box)
                        global char_pressed
                        char_pressed = white_keys[pos_char]
                        global blue_square
                        blue_square = move_coins(char_pressed,coords_box)
                        print(char_pressed)
                        
                        
                    if coords_boxs in black_coords:                      #FOR BLACK
                        coords_box = coords_boxs 
                        a = black_coords.index(coords_box)
                        char_pressed = black_keys[a]
                        print(char_pressed)


                if mouse_presses[2]:
                    y = pygame.mouse.get_pos()
                    global coords_box1     #to change pos in dict of all coins in move_selected_piece
                    coords_box1 = [y[0]//60, 7-(y[1]//60)]

                    if coords_box1 in blue_square[0]:
                        going_pos = [coords_box1[0]*60, (7-coords_box1[1])*60]                        
                        org_pos = [blue_square[1][0]*60, (7-blue_square[1][1])*60]
                        piece = White_pieces.get(char_pressed[:-1])
                        nos_going_pos = len(blue_square[0])

                        
                        if (blue_square[1][0]+blue_square[1][1])%2 == 0:                            
                            org_col = BG2
                        else:                            
                            org_col = BG1

                        move_selected_piece(org_col, org_pos, going_pos, piece, nos_going_pos)    
                    else:
                        print('no')   #make it remove the blue boxes

                    
                        
                else:
                    pass
                            
                    


                    
def new_board():
    pics = [BG1,BG2]
    num = 0
    for i in range (0,8):
        for j in range (0,8):
            if num%2 != 0:
                screen.blit(pics[1],(i*60,j*60))
                
            if num%2 == 0:
                screen.blit(pics[0],(i*60,j*60))
                
            num=num+1
        num=num+1      
                
    for i in range (8):
        if i == 0 or i == 7:
            screen.blit(Black_pieces.get('bR'),(i*60,0))
            screen.blit(White_pieces.get('wR'),(i*60,420))
         
        elif i == 1 or i == 6:
            screen.blit(Black_pieces.get('bN'),(i*60,0))
            screen.blit(White_pieces.get('wN'),(i*60,420))

        elif i == 2 or i == 5:
            screen.blit(Black_pieces.get('bB'),(i*60,0))
            screen.blit(White_pieces.get('wB'),(i*60,420))

        elif i == 3:
            screen.blit(Black_pieces.get('bQ'),(i*60,0))
            screen.blit(White_pieces.get('wQ'),(i*60,420))

        elif i == 4:
            screen.blit(Black_pieces.get('bK'),(i*60,0))
            screen.blit(White_pieces.get('wK'),(i*60,420))
               
        else:
            pass
        screen.blit(White_pieces.get('wP'),(i*60,360))
        screen.blit(Black_pieces.get('bP'),(i*60,60))

         
new_board()



while True:
    
    play_game()
    pygame.display.update()
    clock.tick(60)

