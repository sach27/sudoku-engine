import sys
from tkinter import *
sys.setrecursionlimit(1500)
window=Tk()
#Label(window, text="Sudoku").grid(row=10,column=0)
def Ui():   
        ################---------- INTIALISING BOARD---------#################3
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    def out1():
    ###############------------PRINTING THE BOARD------###################
        def show(board):
            op=5
            ok=3
            #window.delete()
            for i in range(0,len(board)):
                op=op+1
                ok=3
                for j in range(0,len(board[i])):
                        ok=ok+1
                        Button(win,text=board[i][j],width=3).grid(row=op,column=ok)
        #############-------------FINDING EMPTY VALUES-------#################
        def find(board):
            for k in range(0,len(board)):
                for l in range(0,len(board[0])):
                    if(str(board[k][l])=="0"):
                        return(k,l)
            return None
        ###########--------------VALIDATING THE BOADR--------#################
            #Validating in row
        def validate(board,num,pos):
            for i in range(len(board[0])):
                if str(board[pos[0]][i]) == str(num) and pos[1] != i:# Pos[0] esentially comes form solve where we have actually pointed it from list of empty position as we have given row, col=empty
                #And pos is taken as row,col pos[0] is equal to row and pos[1]=column
                    return False            
            #Validating in column
            for j in range(0,len(board[0])):
                if str(board[j][pos[1]])==str(num) and pos[0]!=j:
                    return False
            #Validating in box 
            boxx=pos[1]//3
            boxy=pos[0]//3
            for k in range(boxy*3, boxy*3+3):
                for l in range(boxx*3,boxx*3+3):
                    if(str(board[k][l])==str(num) and (k,l)!=pos):
                        return False
            return True
        ############------------ACTUALLY SOLVING THE BOARD-----############## 
        def solve(board):
            empty=find(board)
            if not empty:
                return(True)
            else:
                row, col=empty
            for i in range(1,10):
                if validate(board,i,(row,col)):
                    board[row][col]=str(i)
                    if solve(board):
                        return True
                    board[row][col]="0"
            return(False)
        o1=[En11.get(),En12.get(),En13.get(),En14.get(),En15.get(),En16.get(),En17.get(),En18.get(),En19.get()]
        o2=[En21.get(),En22.get(),En23.get(),En24.get(),En25.get(),En26.get(),En27.get(),En28.get(),En29.get()]
        o3=[En31.get(),En32.get(),En33.get(),En34.get(),En35.get(),En36.get(),En37.get(),En38.get(),En39.get()]
        o4=[En41.get(),En42.get(),En43.get(),En44.get(),En45.get(),En46.get(),En47.get(),En48.get(),En49.get()]
        o5=[En51.get(),En52.get(),En53.get(),En54.get(),En55.get(),En56.get(),En57.get(),En58.get(),En59.get()]
        o6=[En61.get(),En62.get(),En63.get(),En64.get(),En65.get(),En66.get(),En67.get(),En68.get(),En69.get()]
        o7=[En71.get(),En72.get(),En73.get(),En74.get(),En75.get(),En76.get(),En77.get(),En78.get(),En79.get()]
        o8=[En81.get(),En82.get(),En83.get(),En84.get(),En85.get(),En86.get(),En87.get(),En88.get(),En89.get()]
        o9=[En91.get(),En92.get(),En93.get(),En94.get(),En95.get(),En96.get(),En97.get(),En98.get(),En99.get()]
        win=Tk()
        board=[o1,o2,o3,o4,o5,o6,o7,o8,o9]
        for t in range(0,len(board)):
            for p in range(0,len(board[0])):
                if(len(board[t][p])==0):
                    board[t][p]="0"
                else:
                    pass
       
        show(board)
        solve(board)
        show(board)
    En11=StringVar()
    En12=StringVar()
    En13=StringVar()
    En14=StringVar()
    En15=StringVar()
    En16=StringVar()
    En17=StringVar()
    En18=StringVar()
    En19=StringVar()
    En21=StringVar()
    En22=StringVar()
    En23=StringVar()
    En24=StringVar()
    En25=StringVar()
    En25=StringVar()
    En26=StringVar()
    En27=StringVar()
    En28=StringVar()
    En29=StringVar()
    En31=StringVar()
    En32=StringVar()
    En34=StringVar()
    En35=StringVar()
    En36=StringVar()
    En37=StringVar()
    En38=StringVar()
    En39=StringVar()
    En41=StringVar()
    En42=StringVar()
    En43=StringVar()
    En44=StringVar()
    En45=StringVar()
    En46=StringVar()
    En47=StringVar()
    En48=StringVar()
    En49=StringVar()
    En51=StringVar()
    En52=StringVar()
    En53=StringVar()
    En54=StringVar()
    En55=StringVar()
    En56=StringVar()
    En57=StringVar()
    En58=StringVar()
    En59=StringVar()
    En61=StringVar()
    En62=StringVar()
    En63=StringVar()
    En63=StringVar()
    En64=StringVar()
    En65=StringVar()
    En66=StringVar()
    En67=StringVar()
    En68=StringVar()
    En69=StringVar()
    En71=StringVar()
    En72=StringVar()
    En72=StringVar()
    En73=StringVar()
    En74=StringVar()
    En75=StringVar()
    En76=StringVar()
    En77=StringVar()
    En78=StringVar()
    En79=StringVar()
    En81=StringVar()
    En82=StringVar()
    En83=StringVar()
    En87=StringVar()
    En84=StringVar()
    En85=StringVar()
    En86=StringVar()
    En88=StringVar()
    En89=StringVar()
    En91=StringVar()
    En92=StringVar()
    En93=StringVar()
    En94=StringVar()
    En95=StringVar()
    En96=StringVar()
    En97=StringVar()
    En98=StringVar()
    En99=StringVar() 
    En11=Entry(window,width=3)
    En11.grid(row=5,column=5)
    En12=StringVar()
    En12=Entry(window,width=3)
    En12.grid(row=5,column=6)
    En13=Entry(window,width=3)
    En13.grid(row=5,column=7)
    En14=Entry(window,width=3)
    En14.grid(row=5,column=8)
    En15=Entry(window,width=3)
    En15.grid(row=5,column=9)
    En16=Entry(window,width=3)
    En16.grid(row=5,column=10)
    En17=Entry(window,width=3)
    En17.grid(row=5,column=11)
    En18=Entry(window,width=3)
    En18.grid(row=5,column=12)
    En19=Entry(window,width=3)
    En19.grid(row=5,column=13)
    En21=Entry(window,width=3)
    En21.grid(row=6,column=5)
    En22=Entry(window,width=3)
    En22.grid(row=6,column=6)
    En23=Entry(window,width=3)
    En23.grid(row=6,column=7)
    En24=Entry(window,width=3)
    En24.grid(row=6,column=8)
    En25=Entry(window,width=3)
    En25.grid(row=6,column=9)
    En26=Entry(window,width=3)
    En26.grid(row=6,column=10)
    En27=Entry(window,width=3)
    En27.grid(row=6,column=11)
    En28=Entry(window,width=3)
    En28.grid(row=6,column=12)
    En29=Entry(window,width=3)
    En29.grid(row=6,column=13)
    En31=Entry(window,width=3)
    En31.grid(row=7,column=5)
    En32=Entry(window,width=3)
    En32.grid(row=7,column=6)
    En33=Entry(window,width=3)
    En33.grid(row=7,column=7)
    En34=Entry(window,width=3)
    En34.grid(row=7,column=8)
    En35=Entry(window,width=3)
    En35.grid(row=7,column=9)
    En36=Entry(window,width=3)
    En36.grid(row=7,column=10)
    En37=Entry(window,width=3)
    En37.grid(row=7,column=11)
    En38=Entry(window,width=3)
    En38.grid(row=7,column=12)
    En39=Entry(window,width=3)
    En39.grid(row=7,column=13)
    En41=Entry(window,width=3)
    En41.grid(row=8,column=5)
    En42=Entry(window,width=3)
    En42.grid(row=8,column=6)
    En43=Entry(window,width=3)
    En43.grid(row=8,column=7)
    En44=Entry(window,width=3)
    En44.grid(row=8,column=8)
    En45=Entry(window,width=3)
    En45.grid(row=8,column=9)
    En46=Entry(window,width=3)
    En46.grid(row=8,column=10)
    En47=Entry(window,width=3)
    En47.grid(row=8,column=11)
    En48=Entry(window,width=3)
    En48.grid(row=8,column=12)
    En49=Entry(window,width=3)
    En49.grid(row=8,column=13)
    En51=Entry(window,width=3)
    En51.grid(row=9,column=5)
    En52=Entry(window,width=3)
    En52.grid(row=9,column=6)
    En53=Entry(window,width=3)
    En53.grid(row=9,column=7)
    En54=Entry(window,width=3)
    En54.grid(row=9,column=8)
    En55=Entry(window,width=3)
    En55.grid(row=9,column=9)
    En56=Entry(window,width=3)
    En56.grid(row=9,column=10)
    En57=Entry(window,width=3)
    En57.grid(row=9,column=11)
    En58=Entry(window,width=3)
    En58.grid(row=9,column=12)
    En59=Entry(window,width=3)
    En59.grid(row=9,column=13)
    En61=Entry(window,width=3)
    En61.grid(row=10,column=5)
    En62=Entry(window,width=3)
    En62.grid(row=10,column=6)
    En63=Entry(window,width=3)
    En63.grid(row=10,column=7)
    En64=Entry(window,width=3)
    En64.grid(row=10,column=8)
    En65=Entry(window,width=3)
    En65.grid(row=10,column=9)
    En66=Entry(window,width=3)
    En66.grid(row=10,column=10)
    En67=Entry(window,width=3)
    En67.grid(row=10,column=11)
    En68=Entry(window,width=3)
    En68.grid(row=10,column=12)
    En69=Entry(window,width=3)
    En69.grid(row=10,column=13)
    En71=Entry(window,width=3)
    En71.grid(row=11,column=5)
    En72=Entry(window,width=3)
    En72.grid(row=11,column=6)
    En73=Entry(window,width=3)
    En73.grid(row=11,column=7)
    En74=Entry(window,width=3)
    En74.grid(row=11,column=8)
    En75=Entry(window,width=3)
    En75.grid(row=11,column=9)
    En76=Entry(window,width=3)
    En76.grid(row=11,column=10)
    En77=Entry(window,width=3)
    En77.grid(row=11,column=11)
    En78=Entry(window,width=3)
    En78.grid(row=11,column=12)
    En79=Entry(window,width=3)
    En79.grid(row=11,column=13)
    En81=Entry(window,width=3)
    En81.grid(row=12,column=5)
    En82=Entry(window,width=3)
    En82.grid(row=12,column=6)
    En83=Entry(window,width=3)
    En83.grid(row=12,column=7)
    En84=Entry(window,width=3)
    En84.grid(row=12,column=8)
    En85=Entry(window,width=3)
    En85.grid(row=12,column=9)
    En86=Entry(window,width=3)
    En86.grid(row=12,column=10)
    En87=Entry(window,width=3)
    En87.grid(row=12,column=11)
    En88=Entry(window,width=3)
    En88.grid(row=12,column=12)
    En89=Entry(window,width=3)
    En89.grid(row=12,column=13)
    En91=Entry(window,width=3)
    En91.grid(row=13,column=5)
    En92=Entry(window,width=3)
    En92.grid(row=13,column=6)
    En93=Entry(window,width=3)
    En93.grid(row=13,column=7)
    En94=Entry(window,width=3)
    En94.grid(row=13,column=8)
    En95=Entry(window,width=3)
    En95.grid(row=13,column=9)
    En96=Entry(window,width=3)
    En96.grid(row=13,column=10)
    En97=Entry(window,width=3)
    En97.grid(row=13,column=11)
    En98=Entry(window,width=3)
    En98.grid(row=13,column=12)
    En99=Entry(window,width=3)
    En99.grid(row=13,column=13)
    k=Button(window, text="PRESS ME TO CONTINUE",command= out1).grid(row=15,column=5,columnspan=9)
##########--------------INITALLISING RECURSION------#################
Ui()

#
#abc()

