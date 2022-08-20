import random

import numpy as np

from manimlib import *

LEN = 5
MOVE_INTERVAL = 0.1
DX = [0, -1, 1, 0]
DY = [-1, 0, 0, 1]
DIR = [LEFT, UP, DOWN, RIGHT]

"""
可以点击的方块类
参数：边长，数字，场景，可以移动的方向
方法：点击事件
"""


class ClickBlock(Button):
    def __init__(self, index: int, scene: GameScene, side_length=1.5, **kwargs):
        self.index = index
        self.scene_ctx = scene
        mobject = VGroup(
            Square(side_length=side_length, color=Color(
                hsl=(random.random(), 0.5, 0.5))),
            Integer(index).set_height(scene.side_length * 0.4)
        )
        super(ClickBlock, self).__init__(mobject, self.on_click)
        self.can_move = ORIGIN

    def on_click(self, mob):
        scene = self.scene_ctx
        if np.all(self.can_move == ORIGIN) or scene.on_anim:
            return
        scene.on_anim = True
        scene.play(self.animate.shift(self.can_move *
                   scene.shift_distance), run_time=MOVE_INTERVAL)
        scene.swap_array_item(0, self.index)
        scene.update_can_move()
        scene.on_anim = False


"""
游戏场景
成员：
    正方形边长
    间隙
    游戏窗格位置
    数码数组
    正在播放动画
方法：
    初始化游戏窗格
    初始化数码方块
    初始化按钮
    更新可移动的方块属性
    移动（交换）数码
    开始游戏
    游戏解法
"""


class GameScene(Scene):
    CONFIG = {
        "side_length": 1.5,
        "buff": 0.2,
        "box_center": ORIGIN,
        "array": np.roll(np.arange(LEN ** 2), -1),
        "on_anim": False
    }

    def init_size(self):
        side = (FRAME_HEIGHT - 0.5) / LEN
        self.side_length = side * 0.9
        self.buff = side * 0.1

    def init_gamebox(self):
        self.gamebox = Square(
            side_length=LEN * self.side_length + (LEN + 1) * self.buff
        )
        self.gamebox.shift(self.box_center)
        self.add(self.gamebox)
        self.shift_distance = self.side_length + self.buff

    def init_clickblocks(self):
        self.boxes = Group()  # 15
        for i in range(1, LEN ** 2):
            cb = ClickBlock(i, self, self.side_length)
            self.boxes.add(cb)
        self.boxes.arrange_in_grid(LEN, LEN, buff=self.buff)
        self.boxes.shift(self.box_center)
        self.add(self.boxes)

    def update_can_move(self):
        for cb in self.boxes:
            cb.can_move = ORIGIN
        zero_index = np.where(self.array == 0)[0][0]
        x, y = zero_index // LEN, zero_index % LEN
        for i in range(4):
            new_x, new_y = x + DX[i], y + DY[i]
            if 0 <= new_x < LEN and 0 <= new_y < LEN:
                new_index = new_y + new_x * LEN
                el = self.array[new_index] - 1
                self.boxes[el].can_move = -DIR[i]

    def swap_array_item(self, i, j):
        x = np.where(self.array == i)[0][0]
        y = np.where(self.array == j)[0][0]
        self.array[x], self.array[y] = self.array[y], self.array[x]

    def start_to_play(self, mob):
        if self.on_anim:
            return
        self.on_anim = True
        random.seed(time.time())
        random.shuffle(self.array)
        while not has_answer(self.array):
            random.shuffle(self.array)
        pos = dict()
        top_left = self.gamebox.get_corner(
            UL) + DR * (self.buff + self.side_length / 2)
        for i in range(len(self.array)):
            if self.array[i] == 0:
                continue
            cb_index = self.array[i] - 1
            x, y = i // LEN, i % LEN
            pos[cb_index] = top_left + \
                self.shift_distance * (x * DOWN + y * RIGHT)
        self.play(LaggedStart(*[
            ApplyMethod(self.boxes[i].move_to, pos[i])
            for i in pos
        ]), run_time=1.5, lag_ratio=0.1)
        self.update_can_move()
        self.on_anim = False

    def init_button(self):
        play_btn = Button(
            Text("Play").add_background_rectangle(
                color=BLACK, buff=self.buff).to_edge(RIGHT).shift(UP/2),
            self.start_to_play
        )
        # solve_btn = Button(
        #     Text("Solve").add_background_rectangle(color=BLACK, buff=self.buff).to_edge(RIGHT).shift(DOWN/2),
        #     self.solve_problem
        # )
        self.add(play_btn)

    def setup(self):
        self.init_size()
        self.init_gamebox()
        self.init_clickblocks()
        self.init_button()
        self.update_can_move()


def _get_array_that_ai_larger_than_previous_numbers(array: np.ndarray) -> np.ndarray:
    res = np.zeros(LEN ** 2 - 1)
    mask = array != 0
    sub_arr = array[mask]
    for i in range(1, len(sub_arr)):
        query = np.where(sub_arr[:i] < sub_arr[i])[0]
        res[i] = len(query)
    return res


def has_answer(start: np.ndarray) -> bool:
    sum_array = sum(_get_array_that_ai_larger_than_previous_numbers(start))
    return sum_array % 2 == 0
