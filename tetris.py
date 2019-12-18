from kivy.clock import *
from functools import *
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window, Keyboard, WindowBase
from kivy.core.image import Image
from kivy.graphics import Rectangle, Canvas, Color
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import numpy as np
import random as r
import copy #модуль для создания копии обЬекта а не ссылки
import math
import threading
height = 600;
width = 300;
field_width = 10
field_height = 20
size_factor = height / field_height
Config.set("graphics", "height", height)
Config.set("graphics", "weight", width)
Config.set("graphics", "resizable", 0)
Config.write()
Window.size = (600, 600)
sm = ScreenManager(transition=FadeTransition())
canvas = Canvas()
canvas_lab=Canvas()
fall = False
is_Game = False
game_Over = False
is_Used = False
is_pause=False
fig_list = []
fig_colors = [["line", 1], ["ssform", 2], ["wform", 3], ["rform", 4], ["hardform", 5], ["sform", 6],
              ["tform", 7], ["fourform", 8], ["gform", 9], ["anglef", 10], ["surikenform", 11], ["nfform", 12]
              ]
player_score = 0


def simple_rect(i, j, color,canvas=canvas):
    global height
    color_name = ""
    if (color[0] > 0):
        color_name = fig_colors[color[0] - 1][0]
        return Rectangle(texture=Image(color_name + ".png").texture, size=(size_factor, size_factor),
                         pos=(j * size_factor, height - (i + 1) * size_factor))
    else:
        canvas.add(Color(0, 0, 0))
        return Rectangle(size=(size_factor, size_factor), pos=(j * size_factor, height - (i + 1) * size_factor))

next_f_mat=[
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    ]
mat = [
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

]
can_r = True
temp_mat=[]
def can_Rotate():
    global mat
    global temp_mat
    global f
    global can_r
    global field_height
    global field_width
    res_arr = get_rotate_arr()
    if(res_arr==[]):return False # если пустой то не можем вращать
    temp_mat= copy.deepcopy(mat)# создаём полную копию а не ссылку
    can_r = True
    k=0
    clean_all(mat=temp_mat)
    for i in f.rotate_square:
        temp_mat[i[0]][i[1]] = res_arr[k]
        k += 1

    for i in range(field_height):
        for j in range(field_width):
            if(temp_mat[i][j][1]==1 and mat[i][j][0]!=0 and mat[i][j][1]==0):
                return False
    for i in f.rotate_square:
        if (i[0] >= field_height or i[1] >= field_width):
            can_r = False
            break
        # if (mat[i[0]][i[1]][0] > 0 and mat[i[0]][i[1]][1] == 0 or (i[0] < 0 or i[1] < 0)):
        #     can_r = False
        #     break
    return can_r


def set_unUnsed():
    global mat
    for i in mat:
        for j in i:
            j[1] = 0
def clear_Used():# активные ячейки становятся [0,0]
    global mat
    for i in mat:
        for j in i:
            if(j[1] == 1):
                j[1] = 0
                j[0] = 0
def clean_all(mat=mat):
    for i in mat:
        for j in i:
            j[1] = 0
            j[0] = 0
def show_mat(mat=mat):
    v=0
    for i in mat:
        for j in i:
            print(j, end=' ')
        print(v)
        v+=1

def find_rot_square_neighb():#возвращает массивы индексов граничных элементов rot_square элементов left,right,up,dowm
    global  f
    i_ind=[]
    j_ind=[]
    for i in f.rotate_square:
        i_ind.append(i[0])
        j_ind.append(i[1])

    i_ind=set(i_ind)
    j_ind=set(j_ind)
    i_ind=sorted(list(i_ind))
    j_ind=sorted(list(j_ind))
    imax=max(i_ind)# граница снизу
    imin=min(i_ind)# сверху
    jmax=max(j_ind)# слева
    jmin=min(j_ind)#справа
    left_n=[]
    right_n=[]
    up_n=[]
    down_n=[]
    left_board=[]
    right_board=[]
    up_board=[]
    down_board=[]
    for i in range(int(math.sqrt(len(f.rotate_square)))):
        left_n.append([i_ind[i],jmin-1])
        right_n.append([i_ind[i],jmax+1])
        up_n.append([imin-1,j_ind[i]])
        down_n.append([imax+1,j_ind[i]])
        left_board.append([i_ind[i], jmin])
        right_board.append([i_ind[i], jmax ])
        up_board.append([imin , j_ind[i]])
        down_board.append([imax , j_ind[i]])
    return left_n,right_n,up_n,down_n,left_board,right_board,up_board,down_board

def can_rev_left():#слева от rot_square существует сосед с текстурой
    global field_height
    left_n, right_n, up_n, down_n, left_board, right_board, up_board, down_board = find_rot_square_neighb()  # индексы граничных rot_square элементов
    must_reverse = False
    board_cons_act = False  # граница rot_square содержит активный элемент
    has_neighb = False
    for i in left_board:
        if (mat[i[0]][i[1]][1] == 1):
            board_cons_act = True
            break

    if (left_board[0][1] == 0 and not board_cons_act):
        must_reverse = True
    else:
        for i in range(len(left_n)):
            if (mat[left_n[i][0]][left_n[i][1]][0] > 0):
                has_neighb = True
                break
    if (has_neighb and not board_cons_act): must_reverse = True
    return must_reverse

def can_rev_right():
    global field_width
    left_n, right_n, up_n, down_n, left_board, right_board, up_board, down_board = find_rot_square_neighb()  # индексы граничных rot_square элементов

    must_reverse = False
    board_cons_act = False  # граница rot_square содержит активный элемент
    has_neighb = False
    for i in right_board:
        if (mat[i[0]][i[1]][1] == 1):
            board_cons_act = True
            break

    if (right_board[0][1] == field_width-1 and not board_cons_act):
        must_reverse = True
    else:
         for i in range(len(right_n)):
            if (mat[right_n[i][0]][right_n[i][1]][0] > 0):
                has_neighb = True
                break
    if (has_neighb and not board_cons_act): must_reverse = True

    return must_reverse


def exist_up_n():#слева от rot_square существует сосед с текстурой # не доделана
    left_n, right_n, up_n, down_n,left_board, right_board, up_board, down_board = find_rot_square_neighb()  # индексы соседних c rot_square элементов
    for i in range(len(up_n)):
        if(mat[up_n[i][0]][up_n[i][1]][0]>0):
            return True
    return False
def can_rev_down():#слева от rot_square существует сосед с текстурой или граница экрана
    global field_height
    left_n, right_n, up_n, down_n,left_board, right_board, up_board, down_board = find_rot_square_neighb()  # индексы граничных rot_square элементов

    must_reverse=False
    board_cons_act=False# граница rot_square содержит активный элемент
    has_neighb=False
    for i in down_board:
        if(mat[i[0]][i[1]][1]==1):
            board_cons_act=True
            break
    if(down_board[0][0]==field_height-1 ):
        must_reverse=True

    else:
        for i in range(len(down_n)):
            if(mat[down_n[i][0]][down_n[i][1]][0]>0):
                has_neighb=True
                break
    if(has_neighb and not board_cons_act): must_reverse = True
    return must_reverse


def normalize():
    global mat
    global rshift_num_right
    global rshift_num_left
    global rshift_num_down
    global fig_act
    for _ in range(rshift_num_right):
        print("here rright")
        figure_fall(b=False)
        rshift_num_right-=1
    for _ in range(rshift_num_left):
        print("here rleft")
        figure_up(b=False)
        rshift_num_left-=1
    # for _ in  range(rshift_num_down):# не доделана
    #      print("here rdown")
    #      fig_act.to_left()


def rot_square_fall():
    global f
    global rshift_num_left
    global rshift_num_right
    global rshift_num_down

    # l,r,u,d,=find_rot_square_neighb()
    # print(l)
    # print(r)
    # print(u)
    # print(d)
    # print("down reverse",can_rev_down())
    if (can_rev_down()):  # (если f.rotate_square на граници массива или элемент снизу с текстурой) и граничный элемент rot/square не содержит активных элементовто смещаем влево
        rot_square_up()
        rshift_num_down+=1
    for i in range(len(f.rotate_square)):
        f.rotate_square[i][0] += 1

def rot_square_up():
    global f
    for i in range(len(f.rotate_square)):
        f.rotate_square[i][0] -= 1
rshift_num_left=0#количество смещений если элемент на границе слева
rshift_num_right=0#количество смещений если элемент на границе справа
rshift_num_down=0#количество смещений если элемент на границе снизу

def rot_square_left():
    global f
    global rshift_num_left
    global rshift_num_right
    if(rshift_num_right>0):# eсли уже были смещения то не меняем f.rotate_square
        rshift_num_right-=1
        return

    if (can_rev_left()):  # если f.rotate_square на граници массива  то смещаем влево
        rot_square_right()
        rshift_num_left += 1
    for i in range(len(f.rotate_square)):
        f.rotate_square[i][1] -= 1


def rot_square_right():
    global f
    global mat
    global field_width
    global rshift_num_left
    global rshift_num_right

    print("rshift_left",rshift_num_left)
    print("rshift_right",rshift_num_right)
    if (rshift_num_left > 0):  # eсли уже были смещения то не меняем f.rotate_square
        rshift_num_left -= 1
        return
    if (can_rev_right()):  # если f.rotate_square на граници массива  то смещаем влево
        rot_square_left()
        rshift_num_right+=1
    # for i in range(rshift_num_right+1):
    #      rot_square_up()
    for i in range(len(f.rotate_square)):
        f.rotate_square[i][1] += 1


def draw(mat=mat,canvas=canvas):
    field_width=len(mat[0])
    field_height=len(mat)
    for i in range(field_height):
        for j in range(field_width):
            if (sum(mat[i][j]) != 0):
                canvas.add(simple_rect(i, j, mat[i][j],canvas=canvas))

def draw_next_mat():
    global next_f_mat
    global canvas_lab
    global nf
    clean_next_f_mat()
    nf=fig_list[1]
    mat=next_f_mat
    a=nf.a
    if (a == 0):
        for i in range(0, 5):
            mat[i][4] = [a+1,0]
    elif (a == 1):
        for i in range(0, 3):
            mat[i][4] = [a+1,0]
        mat[0][5] = [a+1,0]
        mat[2][3] = [a+1,0]
    elif (a == 2):
        mat[0][5] = [a+1,0]
        mat[1][5] =[a+1,0]
        mat[1][4] = [a+1,0]
        mat[2][4] = [a+1,0]
        mat[2][3] = [a+1,0]
    elif(a==3):
        mat[0][4] = [a+1,0]
        mat[1][4] = [a+1,0]
        mat[1][5] = [a+1,0]
        mat[0][5] = [a+1,0]
        mat[2][4] = [a+1,0]
    elif(a==4):
        mat[0][4] = [a+1,0]
        mat[1][4] = [a+1,0]
        mat[2][4] = [a+1,0]
        mat[0][5] = [a+1,0]
        mat[1][3] = [a+1,0]
    elif(a==5):
        mat[0][5] = [a+1,0]
        mat[1][5] = [a+1,0]
        mat[2][5] = [a+1,0]
        mat[0][4] = [a+1,0]
        mat[2][4] = [a+1,0]
    elif(a==6):
        mat[0][5] = [a+1,0]
        mat[1][5] = [a+1,0]
        mat[2][5] = [a+1,0]
        mat[2][4] =[a+1,0]
        mat[2][6] = [a+1,0]
    elif(a==7):
        mat[0][5] = [a+1,0]
        mat[1][5] = [a+1,0]
        mat[2][5] =[a+1,0]
        mat[2][4] = [a+1,0]
        mat[3][4] = [a+1,0]
    elif(a==8):
        mat[0][4] = [a+1,0]
        mat[1][4] = [a+1,0]
        mat[2][4] = [a+1,0]
        mat[3][4] = [a+1,0]
        mat[0][5] = [a+1,0]
    elif(a==9):
        mat[0][3] = [a+1,0]
        mat[1][3] = [a+1,0]
        mat[2][3] = [a+1,0]
        mat[0][4] = [a+1,0]
        mat[0][5] = [a+1,0]
    elif (a==10):
        mat[0][4] = [a+1,0]
        mat[1][4] = [a+1,0]
        mat[2][4] = [a+1,0]
        mat[1][3] = [a+1,0]
        mat[1][5] = [a+1,0]
    elif(a==11):
        mat[0][4] = [a+1,0]
        mat[1][4] = [a+1,0]
        mat[2][4] = [a+1,0]
        mat[3][4] = [a+1,0]
        mat[1][5] = [a+1,0]
    field_width = len(mat[0])
    field_height = len(mat)
    for i in range(field_height):
        for j in range(field_width):
            if (sum(mat[i][j]) != 0):
                canvas.add(simple_rect_for_n(i, j, mat[i][j]))

def simple_rect_for_n(i, j, color):
    if (color[0] > 0):
        color_name = fig_colors[color[0] - 1][0]

        return Rectangle(texture=Image(color_name + ".png").texture, size=(size_factor, size_factor),
                         pos=(next_fig_l_pos[0]+j * size_factor, 150 - (i + 1) * size_factor))
    else:
        canvas.add(Color(0, 0, 0))
        return Rectangle(size=(size_factor, size_factor), pos=(j * size_factor, height - (i + 1) * size_factor))

def clean_next_f_mat():
    global next_f_mat
    for i in range(len(next_f_mat)):
        for j in range(len(next_f_mat[0])):
            next_f_mat[i][j]=[0,0]
def changeMat():
    global f
    global fall
    global fig_list
    is_fallen()# упала ли фигура на дно
    if(fall):
        figure_fall()
        draw_next_mat()
    else:
        score()
        set_unUnsed()
        change_f()
        f.gen_F()
        fall=True

def get_active_arr():# возвращает массив индексов активных элементов
    global mat
    global field_height
    global field_width
    global f
    arr1 = []  # массив с индексами активных элемено
    for i in range(field_height):
        for j in range(field_width):
            if (mat[i][j][1] == 1):
                arr1.append(list((i, j)))
    return arr1
def change_f():
    global f
    global fig_list
    fig_list[0] = copy.deepcopy(fig_list[1])
    fig_list.pop(1)
    fig_list.append(Figures())
    f = fig_list[0]


def is_fallen():
    global mat
    global field_height
    global fall
    global is_Used
    for j in mat[field_height-1]:
        if(j[0]>0 and j[1]==1):
            fall=False
            is_Used=True
            break

def detect_collision():
    global mat
    global field_height
    global field_width
    global f
    global fall
    f.can_right = True
    f.can_left = True
    arr1=get_active_arr()# массив с индексами активных элеменов
    collision= False # столкновение с фигурой и землёй
    for k in arr1:
        i=k[0]
        j=k[1]
        left=[];right=[];up=[];down=[]# left - соседняя ячейка слева от mat[i][j]
        # присвоем значения избежав выхода за границы массива
        if (0<=j-1<field_width):
            left=mat[i][j-1]
        else:
            left=[100,0]
        if (0<=j+1<field_width):
            right=mat[i][j+1]
        else:
            right = [100, 0]
        if (0<=i-1<field_height):
            up=mat[i-1][j]
        else:
            up = [100, 0]
        if (0<=i+1<field_height):
            down=mat[i+1][j]
        else:
            down = [100, 0]
        if(down[0] > 0 and down[1] == 0  ):
            collision=True
        if(left[0] > 0 and left[1] == 0):# если есть цвет  слева и он принадлежит неактивной фигуре или за пределом то нельзя перемещаться влево
            f.can_left=False
        if (right[0] > 0 and right[1] == 0):
            f.can_right = False
    return collision
            
        
    # show_mat()
# print(f.rotate_square)
# print(fall)
# print("///////////////////////////////////////////")
def figure_fall(b=True):# b - cмещать ли f.rotate_square
    global mat
    global fall
    global f
    global is_Used
    detect_collision()
    if (fall):
        if (detect_collision()):  # столкновение с фигурой
            # set_unUnsed()
            # is_Used=True
            fall = False

        for i in range(field_height - 1, -1, -1):
            if (fall):
                for j in range(field_width):
                    if (mat[i][j][1] == 1 and i < field_height - 1):# если активна и не на дне меняем местами
                        mat[i + 1][j], mat[i][j] = mat[i][j], [0, 0]
    if (b):
        rot_square_fall()



def figure_up(b=True):
    global mat
    global field_height
    global field_width
    for i in range(field_height):
        for j in range(field_width):
            if (mat[i][j][1] == 1 and i > 0):  # если активна и не на дне меняем местами
                mat[i - 1][j], mat[i][j] = mat[i][j], [0, 0]
    if(b):
        rot_square_up()

def loop(dt):
    global is_Game
    global game_Over
    global player_score
    global ss
    global is_Used


    if (is_Game and not game_Over):  # цикл начинается когда нажата кнопка new game
        canvas.clear()
        is_lose()
        changeMat()
        draw()
    else:
        pass


def score():
    global mat
    global player_score
    global ss
    for i in range(field_height):
        deleteLine = True
        l = list(x[0] for x in mat[i])
        for y in range(len(l) - 1):
            if (l[y] != l[y + 1] or l[y] == 0):
                deleteLine = False
                break
        if (deleteLine):
            player_score += 10
            for j in range(field_width):
                mat[i][j] = [0, 0]
            for k in range(i, 0, -1):
                for m in range(field_width):
                    mat[k][m], mat[k - 1][m] = mat[k - 1][m], mat[k][m]
            ss.sc_lab.text = "Score: " + str(player_score)


def is_lose():
    global game_Over
    global mat
    # print(mat[0],end=" ")
    for j in mat[0]:
        # print(j[0],end=" ")
        if (j[0] > 0 and not fall):
            game_Over = True
    # print()
def change_next_f_mat(a):
    if (a == 0):
        Figures.init_f_line(next_f_mat)
    elif (a== 1):
        Figures.init_f_ssform(next_f_mat)
    elif (a == 2):
        Figures.init_f_wform(next_f_mat)
    elif (a == 3):
        Figures.init_f_rform(next_f_mat)
    elif (a == 4):
        Figures.init_f_hardform(next_f_mat)
    elif (a == 5):
        Figures.init_f_sform(next_f_mat)
    elif (a == 6):
        Figures.init_f_tform(next_f_mat)
    elif (a == 7):
        Figures.init_f_fourform(next_f_mat)
    elif (a == 8):
        Figures.init_f_gform(next_f_mat)
    elif (a == 9):
        Figures.init_f_angelf(next_f_mat)
    elif (a == 10):
        Figures.init_f_surikenform(next_f_mat)
    elif (a == 11):
        Figures.init_nf_form(next_f_mat)
class Figures():
    def gen_F(self):
        if (self.a == 0):
            return self.init_f_line()
        elif (self.a == 1):
            return self.init_f_ssform()
        elif (self.a == 2):
            return self.init_f_wform()
        elif (self.a == 3):
            return self.init_f_rform()
        elif (self.a == 4):
            return self.init_f_hardform()
        elif (self.a == 5):
            return self.init_f_sform()
        elif (self.a == 6):
            return self.init_f_tform()
        elif (self.a == 7):
            return self.init_f_fourform()
        elif (self.a == 8):
            return self.init_f_gform()
        elif (self.a == 9):
            return self.init_f_angelf()
        elif (self.a == 10):
            return self.init_f_surikenform()# chan
        elif (self.a == 11):
            return self.init_nf_form()

    def __init__(self):
        self.a = r.randint(1, 11)  # вид фигуры
        self.can_right = True
        self.can_left = True

        self.rotate_square = []
        self.square_width = 0
        self.color_ = [0, 0]  # [0]-цвет [1]- отрисовывать или нет
        self.color_[0] = self.a + 1

    def init_f_line(self,mat=mat):
        global fall
        global is_Used
        for i in range(5):
            for j in range(2, 7):
                self.rotate_square.append([i, j])

        self.square_width = 5
        self.color_[1] = 1
        for i in range(0, 5):
            mat[i][4] = self.color_;




    def init_f_ssform(self,mat=mat):
        global fall

        global is_Used
        for i in range(3):
            for j in range(3, 6):
                self.rotate_square.append([i, j])

        self.square_width = 3
        self.color_[1] = 1
        for i in range(0, 3):
            mat[i][4] = self.color_;
        mat[0][5] = self.color_
        mat[2][3] = self.color_


    def init_f_wform(self,mat=mat):
        global fall

        for i in range(3):
            for j in range(3, 6):
                self.rotate_square.append([i, j])

        self.square_width = 3
        self.color_[1] = 1

        mat[0][5] = self.color_
        mat[1][5] = self.color_
        mat[1][4] = self.color_
        mat[2][4] = self.color_
        mat[2][3] = self.color_



    def init_f_rform(self,mat=mat):
        global fall

        for i in range(3):
            for j in range(4, 7):
                self.rotate_square.append([i, j])

        self.square_width = 3
        self.color_[1] = 1

        mat[0][4] = self.color_
        mat[1][4] = self.color_
        mat[1][5] = self.color_
        mat[0][5] = self.color_
        mat[2][4] = self.color_



    def init_f_hardform(self,mat=mat):
        global fall
        for i in range(3):
            for j in range(3, 6):
                self.rotate_square.append([i, j])

        self.square_width = 3

        self.color_[1] = 1

        mat[0][4] = self.color_
        mat[1][4] = self.color_
        mat[2][4] = self.color_
        mat[0][5] = self.color_
        mat[1][3] = self.color_



    def init_f_sform(self,mat=mat):
        global fall

        for i in range(3):
            for j in range(4, 7):
                self.rotate_square.append([i, j])

        self.square_width = 3

        self.color_[1] = 1

        mat[0][5] = self.color_
        mat[1][5] = self.color_
        mat[2][5] = self.color_
        mat[0][4] = self.color_
        mat[2][4] = self.color_


    def init_f_tform(self,mat=mat):
        global fall

        for i in range(3):
            for j in range(4, 7):
                self.rotate_square.append([i, j])

        self.square_width = 3

        self.color_[1] = 1

        mat[0][5] = self.color_
        mat[1][5] = self.color_
        mat[2][5] = self.color_
        mat[2][4] = self.color_
        mat[2][6] = self.color_



    def init_f_fourform(self,mat=mat):
        global fall
        for i in range(4):
            for j in range(3, 7):
                self.rotate_square.append([i, j])

        self.square_width = 4
        self.color_[1] = 1
        mat[0][5] = self.color_
        mat[1][5] = self.color_
        mat[2][5] = self.color_
        mat[2][4] = self.color_
        mat[3][4] = self.color_


    def init_f_gform(self,mat=mat):
        global fall

        for i in range(4):
            for j in range(3, 7):
                self.rotate_square.append([i, j])

        self.square_width = 4

        self.color_[1] = 1

        mat[0][4] = self.color_
        mat[1][4] = self.color_
        mat[2][4] = self.color_
        mat[3][4] = self.color_
        mat[0][5] = self.color_



    def init_f_angelf(self,mat=mat):
        global fall

        for i in range(3):
            for j in range(3, 6):
                self.rotate_square.append([i, j])

        self.square_width = 3

        self.color_[1] = 1

        mat[0][3] = self.color_
        mat[1][3] = self.color_
        mat[2][3] = self.color_
        mat[0][4] = self.color_
        mat[0][5] = self.color_


    def init_f_surikenform(self,mat=mat):
        global fall
        self.rotate_square=[]
        for i in range(3):
            for j in range(3, 6):
                self.rotate_square.append([i, j])

        self.square_width = 3

        self.color_[1] = 1

        mat[0][4] = self.color_
        mat[1][4] = self.color_
        mat[2][4] = self.color_
        mat[1][3] = self.color_
        mat[1][5] = self.color_



    def init_nf_form(self,mat=mat):
        global fall

        for i in range(4):
            for j in range(3, 7):
                self.rotate_square.append([i, j])

        self.square_width = 4

        self.color_[1] = 1

        mat[0][4] = self.color_
        mat[1][4] = self.color_
        mat[2][4] = self.color_
        mat[3][4] = self.color_
        mat[1][5] = self.color_



f = Figures()
nf=Figures()
class FirstSc(Screen):
    def new_hame_on_press(self, *args):
        global is_Game
        sm.current = 'second'
        is_Game = True

    def b(self):
        self.root = BoxLayout(orientation="vertical")
        self.new_game = Button(text="New Game")
        self.new_game.bind(on_press=self.new_hame_on_press)
        self.another = Button(text="Another")
        self.root.add_widget(self.new_game)
        self.root.add_widget(self.another)
        return self.root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.b())


def get_rotate_arr(): #возвращает массив для поворота
    global f
    global mat
    matrix = []
    matrix_n = []

    # print("//////////////")
    # print("before")
    # show_mat(mat)
    # print(f.rotate_square)

    for i in f.rotate_square:
        matrix.append(mat[i[0]][i[1]])
    # print(f.rotate_square)
    # print('matrix', matrix)
    i = 0
    for _ in range(len(matrix)):
        if (i >= len(matrix) - 1): break
        m = []
        for j in range(f.square_width):
            m.append(matrix[i])
            i += 1
        matrix_n.append(m)
    res_arr = []
    if(matrix_n!=[]) :   # чтобы избежать ошибки если нажать когда фигура не падает а новая фигура ещёне появилась
        matrix_n = np.rot90(matrix_n)
        for i in matrix_n:
            for j in i:
                res_arr.append(list(j))
    return res_arr

class Figure_Actions:
    def rot90(self):
        global mat
        global temp_mat
        res_arr=get_rotate_arr()
        k = 0
        clear_Used()
        for i in f.rotate_square:
            if(temp_mat[i[0]][i[1]][1]==1):
                mat[i[0]][i[1]] = res_arr[k]
            k += 1
        normalize()
        # for i in range(rshift_num_right):
        #     figure_up() ариант другой дополнить матрицу

    def to_right(self):
        global mat
        global field_height
        global field_width
        detect_collision()  # вызываем чтобы проверь можно ли перемещаться
        if (f.can_right):
            rot_square_right()
            for j in range(field_width - 1, -1, -1):
                for i in range(field_height - 1, -1, -1):
                    if(mat[i][j][1]==1):
                        mat[i][j + 1], mat[i][j] = mat[i][j], [0, 0]

    def to_left(self):
        global mat
        global field_height
        global field_width
        detect_collision()# вызываем чтобы проверь можно ли перемещаться
        if (f.can_left):
            rot_square_left()
            for j in range(field_width):
                    for i in range(field_height):
                        if (mat[i][j][1] == 1):
                            mat[i][j - 1], mat[i][j] = mat[i][j], [0, 0]

fig_act=[]
next_fig_l_pos=[]
class SecondSc(Screen, Widget):

    def b_on_press(self, *args):
        global is_Game
        global ss
        global mat
        global fall, is_Game, game_Over, is_Used
        sm.current = "first"
        fall = False
        is_Game = False
        game_Over = False
        is_Used = False
        for i in range(field_height):
            for j in range(field_width):
                mat[i][j][0] = 0
                mat[i][j][1] = 0

        is_Game = False

    def pause_on_press(self,*args):
        global is_pause
        is_pause=True
        sm.current = "first"

    def __init__(self, **kwargs):
        super(SecondSc, self).__init__(**kwargs)
        global fig_list
        global player_score
        global fig_act
        global canvas_lab
        global next_fig_l_pos
        self.fig_act = Figure_Actions()
        fig_act=self.fig_act
        fig_list.append(Figures())
        fig_list.append(Figures())
        # f = fig_list.pop(0)
        self.lab_game = Label()
        self.lab_game.canvas = canvas
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.box_l = BoxLayout(orientation="vertical")
        self.sc_lab = Label(text="Score:" + str(player_score), size=(200, 200), padding=(50, 50), markup=True,
                            color=[1, 1, 0, 1])
        self.fig_text_lab=Label(text="Следующая фигура",font_size=20)
        self.button_new_g = Button(text="Новая игра",size_hint=(1,0.2))
        self.button_new_g.bind(on_press=self.b_on_press)
        self.button_pause=Button(text="Пауза",size_hint=(1,0.2))
        self.button_pause.bind(on_press=self.pause_on_press)
        self.next_figure_lab=Label()
        next_fig_l_pos=self.next_figure_lab.pos
        canvas_lab=self.next_figure_lab.canvas

        self.box_l.add_widget(self.sc_lab)
        self.box_l.add_widget(self.button_new_g)
        self.box_l.add_widget(self.button_pause)
        self.box_l.add_widget(self.fig_text_lab)
        self.box_l.add_widget(self.next_figure_lab)
        self.root = BoxLayout(orientation="horizontal")
        self.root.add_widget(self.lab_game)
        self.root.add_widget(self.box_l)
        self.add_widget(self.root)
        Clock.schedule_interval(loop, 0.2)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        global f
        if keycode[1] == 'd':
            self.fig_act.to_right()
        if keycode[1] == 'a':
            self.fig_act.to_left()
        if keycode[1] == 'w':
            detect_collision()
            if (can_Rotate() and fall):
                self.fig_act.rot90()
                # print("after")
                # show_mat(mat)
                detect_collision()
        return True


ss = SecondSc(name='second');


class Main(App):
    def build(self):
        global ss
        fs = FirstSc(name='first');
        fs.height = height
        fs.width = width
        ss.height = height
        ss.width = width
        sm.add_widget(fs)
        sm.add_widget(ss)

        return sm


if __name__ == "__main__":
    Main().run()

