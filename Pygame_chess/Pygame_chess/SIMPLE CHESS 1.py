import csv

def value_for_white(c,k,l):
    white_points=0
    for j in c:
        z=j[0]
        z=l.get(z)       
        count=0
        for i in k:
            if (z in i):                
                w=k[count][1]          
                
                white_points= white_points+int(w)
            else:
                count=count+1
    return(str(white_points))

def value_for_black(d,k,l):
    black_points=0
    for j in d:
        z=j[0]
        z=l.get(z)        
        count=0
        for i in k:
            if (z in i):
                
                w=k[count][1]
                
                
                black_points+=int(w)
            else:
                count=count+1
    return(str(black_points))


def player_score(white_cutcoin,black_cutcoin):
    
    c=white_cutcoin
    print(c)
    d=black_cutcoin
    print(d)
    k=[]
    
    l={'bN':'Knight','wN':'Knight', 'bB':'Bishop',
       'wB':'Bishop','bR':'Rook','wR':'Rook','wP':'Pawn',
       'bP':'Pawn','bQ':'Queen','wQ':'Queen','wK':'King','bK':'King'}
    
    with open ("coins_value.txt", 'r') as f:
        reader=csv.reader(f)
        size_to_read = 100
        f_contents=f.read(size_to_read)

        while len(f_contents)>0:
            
            a=(f_contents)
            b=a.split()
            
            f_contents=f.read(size_to_read)
    for i in range(1,6):
        k.append((b[i]).split(','))
    print(k)
    
    
    a=value_for_white(c,k,l)
    print(a)
    
    b=value_for_black(d,k,l)
    print(b)

    
    with open("player_score.txt", 'r') as score:
        lines=score.readlines()
        print(lines)
     
        lan=len(lines)
               
        last_lines=[lines[lan-2]]
        global s_no
     

        s_no=str((last_lines[0][0]))
        print(s_no)
        
    score.close()    
    
    with open("player_score.txt", 'a')as score_append:
        
        writer1=csv.writer(score_append)
        yz=str(int(s_no)+1)
        print(yz)
        writer1.writerow([yz,'     ',(a),'     ',(b)])
    score_append.close()

    
    with open("player_score.txt", 'r') as points:
        reader=csv.reader(points)
        file=points.read()
        print(file)

   
    


def instructions():
    print('''This game of chess is very similar to regular chess execpt for the pieces and numberings used.
            Every coin is denoted with two letters,
                o The first letter (b,w) refer to the colour of the coin i.e (black/white)
                o The second letter (P,R,B,N,Q,K) refers to the type of coin i.e (Pawn,Rook,Bishop,Knight,Queen,King)
            as the game progress chose the spaces u would like to move from the given options, dont pick an impossible
            move or a deleted coin

            Enjoy the game :) ''')
          



def playgame():
    import csv
    white_cut=[]
    global white_cutcoin
    white_cutcoin=[]
    

    black_cut=[]
    global black_cutcoin
    black_cutcoin=[]
 

    board=[      [7,'bR','bN','bB','bQ','bK','bB','bN','bR'],
                 [6,'bP','bP','bP','--','bP','bP','bP','bP'],
                 [5,'--','--','--','bP','--','--','--','--'],
                 [4,'--','--','--','--','--','--','--','--'],
                 [3,'--','--','--','--','--','--','--','--'],
                 [2,'--','--','--','--','--','--','--','--'],
                 [1,'wP','wP','wP','wP','wP','wP','wP','wP'],
                 [0,'wR','wN','wB','wQ','wK','wB','wN','wR'],
               ['   0','  1',' 2',' 3',' 4',' 5',' 6',' 7']]

    game_position_of_black={'bP1':[0,6],
                   'bP2':[1,6],
                   'bP3':[2,6],
                   'bP4':[3,5],
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

    def check_Knight_black(i_coord,j_coord):
        a=Knight(i_coord,j_coord)
        pos_for_Knight=[]
        b=list(game_position_of_white.values())

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

    def check_Bishop_black(i_coord,j_coord):
        a=Bishop(i_coord,j_coord)
        pos_for_Bishop=[]
        for i in (a):
            if i!=[]:
                for j in (i):
                    line_in=(j[1]-7)//-1
                    pos_inline=j[0]+1
                    w=board[line_in][pos_inline]
                    b=list(game_position_of_white.values())
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

    def check_Rook_black(i_coord,j_coord):
        a=Rook(i_coord,j_coord)
        pos_for_Rook=[]
        for i in (a):
            if i!=[]:
                for j in (i):
                    line_in=(j[1]-7)//-1
                    pos_inline=j[0]+1
                    w=board[line_in][pos_inline]
                    b=list(game_position_of_white.values())
                    if j in b:
                        pos_for_Rook.append(j)
                    if (w=='--'):
                        pos_for_Rook.append(j)
                   
                    else:
                        break
                        
            else:
                pass
        return(pos_for_Rook)

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

    def check_King_black(i_coord,j_coord):
        a=King(i_coord,j_coord)
        pos_for_King=[]
        for i in (a):
                    line_in=(i[1]-7)//-1
                    pos_inline=i[0]+1
                    w=board[line_in][pos_inline]
                    b=list(game_position_of_white.values())
                    if i in b:
                        pos_for_King.append(i)
                    if (w=='--'):
                        pos_for_King.append(i)
                   
                    else:
                        break
                        

        return(pos_for_King)


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

    def check_Queen_black(i_coord,j_coord):
        a=Queen(i_coord,j_coord)
        pos_for_Queen=[]
        for i in (a):
            if i!=[]:
                for j in (i):
                    line_in=(j[1]-7)//-1
                    pos_inline=j[0]+1
                    w=board[line_in][pos_inline]
                    b=list(game_position_of_white.values())
                    if j in b:
                        pos_for_Queen.append(j)
                    if (w=='--'):
                        pos_for_Queen.append(j)
                   
                    else:
                        break
                        
            else:
                pass
        return(pos_for_Queen)

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

    def PawnBlack(i_coord,j_coord):
        avl_coords=[]
        a=i_coord
        b=j_coord

        if b==6:
            avl_coords=[[a,5],[a,4]]
        elif b<6:
            avl_coords=[[a,b-1]]
        return(avl_coords)

    def check_PawnBlack(i_coord,j_coord):
        a=PawnBlack(i_coord,j_coord)
        pos_for_PawnBlack=[]
            
        if len (a)==2:
                   line_in=(a[0][1]-7)//-1
                   pos_inline=a[0][0]+1
                   w=board[line_in][pos_inline]
                   b=list(game_position_of_white.values())
                   i=a[0]
                   c1=i[0]-1
                   c2=i[1]
                   d1=i[0]+1
                   d2=i[1]
                   l1=[c1,c2]
                   l2=[d1,d2]
                   if l2 in b:
                           pos_for_PawnBlack.append(l2)
                   if l1 in b:
                           pos_for_PawnBlack.append(l1)
                   
                   if (w=='--'):
                          pos_for_PawnBlack.append(a[0])
                          pos_for_PawnBlack.append(a[1])
          
                          
                   else:
                              pass
        if len(a)==1:
                   line_in=(a[0][1]-7)//-1
                   pos_inline=a[0][0]+1
                   w=board[line_in][pos_inline]
                   b=list(game_position_of_white.values())
                   for i in a:
                       c1=i[0]-1
                       c2=i[1]
                       d1=i[0]+1
                       d2=i[1]
                       l1=[c1,c2]
                       l2=[d1,d2]
                       if l2 in b:
                           pos_for_PawnBlack.append(l2)
                       if l1 in b:
                           pos_for_PawnBlack.append(l1)
                   if (w=='--'):
                          pos_for_PawnBlack.append(a[0])
                   else:
                              pass
        return(pos_for_PawnBlack)  




    def logic_of_choise_white(move,lent,r,coin,input_1):
        if lent!=0:
           
            i=0
            while i<lent:
                    x=str(move[i])
                    y=str(i)
                    z=(y+x)
                    i+=1
                    print(z)
            input_2=int(input("which position do you like move:"))
            print()

            going_pos=move[input_2]
            a=list(game_position_of_black.values())
            if going_pos in a:
                
                line_in=(going_pos[1]-7)//-1
                pos_linein=going_pos[0]+1
                                         

                line_in1=(r[1]-7)//-1
                pos_linein1=r[0]+1

                acood=board[line_in][pos_linein]
                white_cut.append([acood+'*',(going_pos[0], going_pos[1])] )
                white_cutcoin.append([acood,(going_pos[0], going_pos[1])] )#cut counter
                game_position_of_white
                
                bcood=board[line_in1][pos_linein1]
                board[line_in][pos_linein]=bcood
                board[line_in1][pos_linein1]='--'
                a=str(coin)+str(input_1)
                game_position_of_white[a]=going_pos

                            
            else:
                line_in=(going_pos[1]-7)//-1
                pos_linein=going_pos[0]+1
                                         

                line_in1=(r[1]-7)//-1
                pos_linein1=r[0]+1

                acood=board[line_in][pos_linein]
                
                bcood=board[line_in1][pos_linein1]
                white_cut.append([bcood, (going_pos[0],going_pos[1])])#move counter
                board[line_in][pos_linein]=bcood
                board[line_in1][pos_linein1]=acood

            

                a=str(coin)+str(input_1)
                game_position_of_white[a]=going_pos

            
        if(lent==0):
            print("no possible moves")
            print("choose again")
            move_for_white()


    def logic_of_choise_black(move,lent,r,coin,input_1):
        if lent!=0:
            
            i=0
            while i<lent:
                    x=str(move[i])
                    y=str(i)
                    z=(y+x)
                    i+=1
                    print(z)
            input_2=int(input("which position do you like move:"))
            print()

            going_pos=move[input_2]
            a=list(game_position_of_white.values())
            if going_pos in a:
                
                
                line_in=(going_pos[1]-7)//-1
                pos_linein=going_pos[0]+1
                                         

                line_in1=(r[1]-7)//-1
                pos_linein1=r[0]+1

                acood=board[line_in][pos_linein]
                black_cut.append([acood+'*',(going_pos[0], going_pos[1])])#cut counter
                black_cutcoin.append([acood,(going_pos[0], going_pos[1])])
                
                bcood=board[line_in1][pos_linein1]
                board[line_in][pos_linein]=bcood
                board[line_in1][pos_linein1]='--'
                game_position_of_white[acood]=[""]
                
                a=str(coin)+str(input_1)
                game_position_of_black[a]=going_pos
             
                    
            else:
                line_in=(going_pos[1]-7)//-1
                pos_linein=going_pos[0]+1
                                         

                line_in1=(r[1]-7)//-1
                pos_linein1=r[0]+1

                acood=board[line_in][pos_linein]
                
              
                bcood=board[line_in1][pos_linein1]
                black_cut.append([bcood, (going_pos[0],going_pos[1])])#move counter
                board[line_in][pos_linein]=bcood
                board[line_in1][pos_linein1]=acood
                a=str(coin)+str(input_1)
                game_position_of_black[a]=going_pos

            

            '''a=str(coin)+str(input_1)
            game_position_of_black[a]=going_pos'''

            
        if(lent==0):
            print("no possible moves")
            print("choose again")
            move_for_black() 




    def move_for_white():
                              print("Which piece would","like to move")
                              cons={1:'Pawn',2:'King',3:'Queen',4:'Bishop',5:'Knight',6:'Rook'}
                              print(cons)
                              move_white= int(input("enter which piece:"))
                              


                              if move_white==1:
                                                        for i in  range(8):
                                                                    print(i+1, game_position_of_white.get('wP'+str(i+1)))
                                                        k=int(input("which pawn would u like to move:"))
                                                        b=game_position_of_white.get("wP"+str(k))

                                            
                                                    
                                                        i_coorda=b[0]
                                                        i_coordb=b[1]
                                                        
                                                        move=check_PawnWhite(i_coorda,i_coordb)
                                                        print("possible positions for pawn",move)
                 
                                                        '''input_1=input("what is your move:")
                                                        if input_1=='1':'''
                                                                           
                                                        c="wP"+str(k)
                                                        a=game_position_of_white.get(c)
                                                        a_icood=a[0]
                                                        b_jcood=a[1]
                                                        move=check_PawnWhite(a_icood,b_jcood)
                                                        lent=len(move)
                                                            
                                                        logic_of_choise_white(move,lent,a,c,'')

                                                                         
                                                        '''if input_1=='2':
                                                                      
                                                               c="wP"+str(k)
                                                               a=game_position_of_white.get(c)
                                                               a_icood=a[0]
                                                               b_jcood=a[1]
                                                               move=check_PawnWhite(a_icood,b_jcood)
                                                               lent=len(move)
                                                               print(move)
                                                               logic_of_choise_white(move,lent,a,c,'')'''


                              elif move_white==(2)or(3):
                                                        if move_white==3:
                                                               a=game_position_of_white.get("wQq")
                                                               a_icood=a[0]
                                                               b_jcood=a[1]
                                                               move=check_Queen_white(a_icood,b_jcood)
                                                               lent=len(move)
                                                        
                                                               logic_of_choise_white(move,lent,a,'wQq','')
                                                        if move_white==2:
                                                              b=game_position_of_white.get("wKk")
                                                              a_icood=b[0]
                                                              b_jcood=b[1]
                                                              move=check_King_white(a_icood,b_jcood)
                                                              lent=len(move)
                                                              logic_of_choise_white(move,lent,b,'wKk','')

                              if move_white==4 or 5 or 6:
                                                      if move_white==4: 
                                                          a=game_position_of_white.get("wB1")
                                                          b=game_position_of_white.get("wB2")
                                                          print(a,b)
                                                          input_1=input("which Bishop would u like to move(1/2):")
                                                          s="wB"+str(input_1)
                                                          t=game_position_of_white.get(s)
                                                          i_coord=t[0]
                                                          j_coord=t[1]
                                                          move=check_Bishop_white(i_coord,j_coord)
                                                          lent=len(move)
                                                          logic_of_choise_white(move,lent,t,'wB',input_1)



                                                      if move_white==5: 
                                                          a=game_position_of_white.get("wN1")
                                                          b=game_position_of_white.get("wN2")
                                                          print(a,b)
                                                          input_1=input("which Knight would u like to move(1/2):")
                                                          s="wN"+str(input_1)
                                                          t=game_position_of_white.get(s)
                                                          i_coord=t[0]
                                                          j_coord=t[1]
                                                          move=check_Knight_white(i_coord,j_coord)
                                                          lent=len(move)
                                                    
                                                          logic_of_choise_white(move,lent,t,'wN',input_1)


                                                      if move_white==6: 
                                                          a=game_position_of_white.get("wR1")
                                                          b=game_position_of_white.get("wR2")
                                                          print(a,b)
                                                          input_1=input("which Rook would u like to move(1/2):")
                                                          s="wR"+str(input_1)
                                                          t=game_position_of_white.get(s)
                                                          i_coord=t[0]
                                                          j_coord=t[1]
                                                          move=check_Rook_white(i_coord,j_coord)
                                                          lent=len(move)
                                                          logic_of_choise_white(move,lent,t,'wR',input_1)
                                                    
                              else:
                                  print("please press valid key")              





    def move_for_black():
                              print("Which piece would you","like to move")
                              cons={1:'Pawn',2:'King',3:'Queen',4:'Bishop',5:'Knight',6:'Rook'}
                              print(cons)
                              move_black= int(input("enter which piece:"))


                              if move_black==1:
                                                        for i in  range(8):
                                                                    print(i+1, game_position_of_black.get('bP'+str(i+1)))
                                                        k=int(input("which pawn would you like to move:"))
                                                        b=game_position_of_black.get("bP"+str(k))
                                                    
                                                    
                                                        i_coorda=b[0]
                                                        i_coordb=b[1]
                                                        
                                                        move=check_PawnBlack(i_coorda,i_coordb)
                                                        print("possible positions for pawn",move)
                 
                                                        '''input_1=input("what is your move:")
                                                        if input_1=='1':'''
                                                                          
                                                        c="bP"+str(k)
                                                        a=game_position_of_black.get(c)
                                                        a_icood=a[0]
                                                        b_jcood=a[1]
                                                        move=check_PawnBlack(a_icood,b_jcood)
                                                        lent=len(move)
                                                        print(move)
                                                        logic_of_choise_black(move,lent,a,c,'')

                                                                          
                                                        '''if input_1=='2':'''
                                                                          
                                                        '''c="bP"+str(k)
                                                        a=game_position_of_black.get(c)
                                                        a_icood=a[0]
                                                        b_jcood=a[1]
                                                        move=check_PawnBlack(a_icood,b_jcood)
                                                        lent=len(move)
                                                        print(move)
                                                        logic_of_choise_black(move,lent,a,c,'')'''

                              elif move_black==(2)or(3):
                                                        if move_black==3:
                                                               a=game_position_of_black.get("bQq")
                                                               a_icood=a[0]
                                                               b_jcood=a[1]
                                                               move=check_Queen_black(a_icood,b_jcood)
                                                               lent=len(move)
                                                               
                                                               logic_of_choise_black(move,lent,a,'bQq','')
                                                        if move_black==2:
                                                              b=game_position_of_black.get("bKk")
                                                              a_icood=b[0]
                                                              b_jcood=b[1]
                                                              move=check_King_black(a_icood,b_jcood)
                                                              lent=len(move)
                                                              logic_of_choise_black(move,lent,b,'bKk','')

                              if move_black==4 or 5 or 6:
                                                      if move_black==4: 
                                                          a=game_position_of_black.get("bB1")
                                                          b=game_position_of_black.get("bB2")
                                                          print(a,b)
                                                          input_1=input("which Bishop would u like to move(1/2):")
                                                          s="bB"+str(input_1)
                                                          t=game_position_of_black.get(s)
                                                          i_coord=t[0]
                                                          j_coord=t[1]
                                                          move=check_Bishop_black(i_coord,j_coord)
                                                          lent=len(move)
                                                          logic_of_choise_black(move,lent,t,'bB',input_1)



                                                      if move_black==5: 
                                                          a=game_position_of_black.get("bN1")
                                                          b=game_position_of_black.get("bN2")
                                                          print(a,b)
                                                          input_1=input("which Knight would u like to move(1/2):")
                                                          s="bN"+str(input_1)
                                                          t=game_position_of_black.get(s)

                                                    
                                                          i_coord=t[0]
                                                          j_coord=t[1]
                                                          move=check_Knight_black(i_coord,j_coord)
                                                          lent=len(move)
                                                    
                                                          logic_of_choise_black(move,lent,t,'bN',input_1)


                                                      if move_black==6: 
                                                          a=game_position_of_black.get("bR1")
                                                          b=game_position_of_black.get("bR2")
                                                          print(a,b)
                                                          input_1=input("which Rook would u like to move(1/2):")
                                                          s="bR"+str(input_1)
                                                          t=game_position_of_black.get(s)
                                                          i_coord=t[0]
                                                          j_coord=t[1]
                                                          move=check_Rook_black(i_coord,j_coord)
                                                          lent=len(move)
                                                          logic_of_choise_black(move,lent,t,'bR',input_1)

                              else:
                                  print("please press valid key")



    def maingameloop():
                 print('*'*105)
                 print("WELCOME TO CHESS")
                 print()
                 Gameloop=True
                 player_change=0
                 while(Gameloop):
                              for i in board:
                                    print(i)
                              print()

                              if player_change%2==0:
                                  print("It is white's turn")
                                  move_for_white()
                                  player_change=player_change+1
                                  a=board
                                  king=[]
                                  for i in a:
                                      
                                      for j in i:
                                          king.append(j)
                                  if 'bK' not in king:
                                      print("WHITE WINS")
                                      break
                                  else:
                                      pass
                                  for i in board:
                                         print(i)
                                  print()
                            
                              if player_change%2!=0:
                                  print("It is black's turn")
                                  move_for_black()
                                  player_change=player_change+1
                                  a=board
                                  king=[]
                                  for i in a:
                                      for j in i:
                                          king.append(j)
                                  if 'wK' not in king:
                                      print("BLACK WINS")
                                      break
                                  else:
                                      pass
                                
                 
    maingameloop()
    #print(white_cut)
    #print(black_cut)
    lent_b=len(black_cut)
    lent_w=len(white_cut)
    lent=min(lent_b,lent_w)
    #print(lent)
    combine_moves=[]
    for i in range(lent):
            a=white_cut
            b=black_cut
            combine_moves.append([a[i],b[i]])
            
        
    #print(combine_moves)            


    with open ("cut_coins.csv",'w') as cutcoin:

        csv_writer=csv.writer(cutcoin)
        csv_writer.writerow(['white moves','black moves'])
        for i in combine_moves:
            csv_writer.writerow(i)
    

def moves_made():
    with open("cut_coins.csv", 'r') as f:
        reader=csv.reader(f)
        file=f.read()

        if file==(""):
            print("play a game to know your moves")

        else:
            print (file)



   




prgloop=True
while(prgloop):
    print('*'*110)
    print(" "*20 + "WELCOME TO CHESS")
    print("1. Play the game")
    print("2. Instructions")
    print("3. View moves made in game")
    print("4. View all game info based on points scored")
    print("5. Exit")

    player_choise=int(input("Enter your choice:"))

    if player_choise==1:
        playgame()
    if player_choise==2:
        instructions()
    if player_choise==3:
        moves_made()
    if player_choise==4:
        player_score(white_cutcoin,black_cutcoin)
    if player_choise==5:
        prgloop=False

print('*'*110)
        
        
    
        











                 
        
        
            
        
        
    
    
        



        
    
    




    


                                                                  
