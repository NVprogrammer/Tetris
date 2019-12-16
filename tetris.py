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
import math
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
fall = False
is_Game = False
game_Over = False
is_Used = False
fig_list = []
fig_colors = [["line", 1], ["ssform", 2], ["wform", 3], ["rform", 4], ["hardform", 5], ["sform", 6],
              ["tform", 7], ["fourform", 8], ["gform", 9], ["anglef", 10], ["surikenform", 11], ["nfform", 12]
              ]
player_score = 0


def simple_rect(i, j, color):
    global height
    color_name = ""
    if (color[0] > 0):
        color_name = fig_colors[color[0] - 1][0]
        return Rectangle(texture=Image(color_name + ".png").texture, size=(size_factor, size_factor),
                         pos=(j * size_factor, height - (i + 1) * size_factor))
    else:
        canvas.add(Color(0, 0, 0))
        return Rectangle(size=(size_factor, size_factor), pos=(j * size_factor, height - (i + 1) * size_factor))


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


def can_Rotate():
    global mat
    global f
    global can_r
    global field_height
    global field_width
    can_r = True
    for i in f.rotate_square:
        if (i[0] >= field_height or i[1] >= field_width):
            can_r = False
            break
        if (mat[i[0]][i[1]][0] > 0 and mat[i[0]][i[1]][1] == 0 or (i[0] < 0 or i[1] < 0)):
            can_r = False
            break
    print(can_r)
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

def show_mat(mat=mat):
    for i in mat:
        for j in i:
            print(j, end=' ')
        print()


def rot_square_fall():
    global f
    for i in range(len(f.rotate_square)):
        f.rotate_square[i][0] += 1

def rot_square_left():
    global f
    for i in range(len(f.rotate_square)):
        f.rotate_square[i][1] -= 1


def rot_square_right():
    global f
    for i in range(len(f.rotate_square)):
        f.rotate_square[i][1] += 1


def draw():
    global mat
    for i in range(field_height):
        for j in range(field_width):
            if (sum(mat[i][j]) != 0):
                canvas.add(simple_rect(i, j, mat[i][j]))


def changeMat():
    global f
    global fall
    global fig_list
    f.gen_F()
    if (not fall):
        score()
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



def detect_collision():
    global mat
    global field_height
    global field_width
    global f
    arr1=get_active_arr()# массив с индексами активных элеменов
    collision= False # столкновение с фигурой
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
            up = [0, 0]
        if (0<=i+1<field_height):
            down=mat[i+1][j]
        else:
            down = [100, 0]
        if(down[0] > 0 and down[1] == 0 ):
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
def figure_fall():
    global mat
    global fall
    global f

    if (fall):
        if (detect_collision()):  # столкновение с фигурой
            fig_list.append(Figures())
            f = fig_list.pop(0)
            set_unUnsed()
            fall = False
        for i in range(field_height - 1, -1, -1):
            if (fall):
                for j in range(field_width):
                    if (mat[i][j][1] == 1 and i < field_height - 1):# если активна и не на дне меняем местами
                        mat[i + 1][j], mat[i][j] = mat[i][j], [0, 0]



    rot_square_fall()


def loop(dt):
    global is_Game
    global game_Over
    global player_score
    global ss
    global is_Used

    # print(is_Used)
    if (is_Game and not game_Over):  # цикл начинается когда нажата кнопка new game
        canvas.clear()
        is_lose()
        changeMat()
        # show_mat()
        # print()
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

class Figures():
    def gen_F(self):

        if (self.a == 0):
            return self.f_line()
        elif (self.a == 1):
            return self.f_ssform()
        elif (self.a == 2):
            return self.f_wform()
        elif (self.a == 3):
            return self.f_rform()
        elif (self.a == 4):
            return self.f_hardform()
        elif (self.a == 5):
            return self.f_sform()
        elif (self.a == 6):
            return self.f_tform()
        elif (self.a == 7):
            return self.f_fourform()
        elif (self.a == 8):
            return self.f_gform()
        elif (self.a == 9):
            return self.f_anglef()
        elif (self.a == 10):
            return self.f_surikenform()
        elif (self.a == 11):
            return self.f_nfform()

    def __init__(self):
        self.a = r.randint(0, 12)  # вид фигуры
        self.can_right = True
        self.can_left = True

        self.rotate_square = []
        self.square_width = 0
        self.color_ = [0, 0]  # [0]-цвет [1]- отрисовывать или нет
        self.color_[0] = self.a + 1

    def f_line(self):  # *
        # *
        # *
        # *
        # *
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):
                for i in range(5):
                    for j in range(2, 7):
                        self.rotate_square.append([i, j])

                self.square_width = 5
                self.color_[1] = 1
                for i in range(0, 4):
                    mat[i][4] = self.color_;
                fall = True
            else:
                figure_fall()

    def f_ssform(self):  # **
        #  *
        # **
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):
                for i in range(3):
                    for j in range(3, 6):
                        self.rotate_square.append([i, j])

                self.square_width = 3
                self.color_[1] = 1
                for i in range(0, 3):
                    mat[i][4] = self.color_;
                mat[0][5] = self.color_
                mat[2][3] = self.color_
                fall = True
            else:
                figure_fall()

    def f_wform(self):  # *
        # **
        # **
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):

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
                fall = True
            else:
                figure_fall()

    def f_rform(self):  # **
        # **
        # *
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):

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
                fall = True
            else:
                figure_fall()

    def f_hardform(self):  # **
        # **
        #  *
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):
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
                fall = True
            else:
                figure_fall()

    def f_sform(self):  # **
        #   *
        #  **
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):
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
                fall = True
            else:
                figure_fall()

    def f_tform(self):  # *
        #   *
        #  ***
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):
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
                fall = True
            else:
                figure_fall()

    def f_fourform(self):  # *
        #    *
        #   **
        #   *
        global fall
        global mat
        global is_Used
        if (not is_Used):  # только при инициализации
            if (not fall):
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
                fall = True
            else:
                figure_fall()

    def f_gform(self):  # **
        #   *
        #   *
        #   *
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):

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
                fall = True
            else:
                figure_fall()

    def f_anglef(self):  # ***
        #   *
        #   *
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):

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
                fall = True
            else:
                figure_fall()

    def f_surikenform(self):  # *
        #   ***
        #    *
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):
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
                fall = True
            else:
                figure_fall()

    def f_nfform(self):  # *
        #   **
        #   *
        #   *
        global fall
        global mat
        global is_Used
        if (not is_Used):
            if (not fall):

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
                fall = True
            else:
                figure_fall()

f = Figures()


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



class Figure_Actions:
    def rot90(self):
        global f
        global mat
        matrix = []
        matrix_n = []
        show_mat(mat)
        for i in f.rotate_square:
            matrix.append(mat[i[0]][i[1]])
        print(f.rotate_square)
        print('matrix', matrix)
        i = 0
        for _ in range(len(matrix)):
            if (i >= len(matrix) - 1): break
            m = []
            for j in range(f.square_width):
                m.append(matrix[i])
                i += 1
            matrix_n.append(m)

        matrix_n = np.rot90(matrix_n)
        res_arr = []
        for i in matrix_n:
            for j in i:
                res_arr.append(list(j))
        k = 0
        print('res arr ', res_arr)
        for i in f.rotate_square:
            mat[i[0]][i[1]] = res_arr[k]
            k += 1


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

    def __init__(self, **kwargs):
        super(SecondSc, self).__init__(**kwargs)
        global fig_list
        global player_score
        self.fig_act = Figure_Actions()
        fig_list.append(Figures())
        fig_list.append(Figures())
        f = fig_list.pop(0)
        self.lab_game = Label()
        self.lab_game.canvas = canvas
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.box_l = BoxLayout(orientation="vertical")
        self.sc_lab = Label(text="Score:" + str(player_score), size=(200, 200), padding=(50, 50), markup=True,
                            color=[1, 1, 0, 1])
        self.button_new_g = Button(text="New Game")
        self.button_new_g.bind(on_press=self.b_on_press)
        self.box_l.add_widget(self.sc_lab)
        self.box_l.add_widget(self.button_new_g)
        self.root = BoxLayout(orientation="horizontal")
        self.root.add_widget(self.lab_game)
        self.root.add_widget(self.box_l)
        self.add_widget(self.root)
        Clock.schedule_interval(loop, 0.1)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'd':
            self.fig_act.to_right()
        if keycode[1] == 'a':
            self.fig_act.to_left()
        if keycode[1] == 'w':
            if (can_Rotate()):
                self.fig_act.rot90()
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

