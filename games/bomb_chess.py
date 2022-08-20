from manimlib import *

LEN = 6
ARRAY = np.zeros(LEN ** 2).reshape((LEN, LEN))
LIMIT = np.ones(LEN ** 2).reshape((LEN, LEN)) * 4
DX = [-1, 0, 0, 1]
DY = [0, 1, -1, 0]
DIR = [UP, RIGHT, LEFT, DOWN]
COLOR_DICT = {
    1: RED,
    -1: BLUE
}
COIN_RADIUS = (FRAME_HEIGHT - 1) / 2 / 4 / LEN
for i in range(LEN):
    LIMIT[0][i] -= 1
    LIMIT[LEN - 1][i] -= 1
    LIMIT[i][0] -= 1
    LIMIT[i][LEN - 1] -= 1
MAX_UPDATE = 40
JUDGE_GAME_OVER_COIN = 15


class Coin(Circle):
    CONFIG = {
        "fill_opacity": 1,
        "stroke_width": 6,
        "stroke_color": WHITE,
        "draw_stroke_behind_fill": True,
    }

    def __init__(self, player, **kwargs):
        super(Coin, self).__init__(radius=COIN_RADIUS, fill_color=COLOR_DICT[player], **kwargs)


class MyBox(Button):

    def __init__(self, index: int, scene: Scene, **kwargs):
        self.index = index
        self.coin = 0
        self.scene = scene
        self.coin_mobject = Group()
        self.squ = Square(**kwargs)
        super(MyBox, self).__init__(self.squ, self.on_click)

    def on_click(self, mob):
        if self.scene.mutex:
            return
        player = np.sign(self.coin)
        # 只能下在非对方的格子内
        if player == -self.scene.player:
            return
        self.scene.mutex = True

        self.append_coin()
        flag = True
        count = 0
        while flag:
            flag = self.scene.update_boxes()
            count += 1
            if count > MAX_UPDATE:
                break
        if self.scene.coin_num > JUDGE_GAME_OVER_COIN and self.scene.game_is_over():
            self.scene.play(FadeIn(self.scene.game_over, UP), run_time=0.5)
            self.scene.wait()
            self.scene.play(FadeOut(self.scene.game_over, DOWN), run_time=0.5)

        self.scene.player *= -1
        if self.scene.player == 1:
            self.scene.play(self.scene.cir.animate.set_color(RED), run_time=0.5)
        elif self.scene.player == -1:
            self.scene.play(self.scene.cir.animate.set_color(BLUE), run_time=0.5)

        self.scene.mutex = False

    def append_coin(self):
        self.scene.coin_num += 1
        self.coin += self.scene.player
        self.coin_mobject.add(Coin(self.scene.player))
        self.coin_mobject.arrange_in_grid(2, 2)
        self.coin_mobject.move_to(self.squ)
        self.scene.add(self.coin_mobject)

    def refresh_coin_mobject(self):
        self.scene.remove(self.coin_mobject)
        self.coin_mobject.remove(*self.coin_mobject.submobjects)
        player = np.sign(self.coin)
        for i in range(abs(self.coin)):
            self.coin_mobject.add(Coin(player))
        if len(self.coin_mobject) > 0:
            self.coin_mobject.arrange_in_grid(2, 2).move_to(self.squ)
        self.scene.add(self.coin_mobject)


class GameScene(Scene):
    CONFIG = {
        "player": 1,
        "side_length": (FRAME_HEIGHT - 1) / LEN,
        "anims": [],
        "coin_num": 0,
        "mutex": False,
    }

    def init_boxes(self):
        self.boxes = Group()
        for i in range(LEN ** 2):
            box = MyBox(i, self, side_length=self.side_length, color=GREY)
            self.boxes.add(box)
        self.boxes.arrange_in_grid(LEN, LEN, buff=0).shift(RIGHT)
        self.add(self.boxes)

    def init_player(self):
        self.cir = Circle(radius=0.3, fill_opacity=1).to_edge(RIGHT)
        self.add(self.cir)

    def get_matrix(self):
        matrix = np.zeros(LEN ** 2)
        for i in range(LEN ** 2):
            matrix[i] = self.boxes[i].coin
        return matrix

    def game_is_over(self):
        red = False
        blue = False
        for box in self.boxes:
            if box.coin > 0:
                red = True
            elif box.coin < 0:
                blue = True
            if red & blue:
                return False
        return True

    def update_boxes(self):
        self.anims = []
        flag = False
        # 遍历所有格子的时候应该使用过去式的矩阵
        previous_matrix = self.get_matrix()
        for box in self.boxes:
            x, y = box.index // LEN, box.index % LEN
            # 如果这个格子的硬币数达到上限（此处用过去的矩阵）
            if abs(previous_matrix[box.index]) >= LIMIT[x, y]:
                flag = True
                # 那么这个各自的硬币溢出，进入并夺取周围格子的硬币
                box.coin = 0
                count = 0
                for i in range(4):
                    nx, ny = x + DX[i], y + DY[i]
                    if 0 <= nx < LEN and 0 <= ny < LEN:
                        nind = nx * LEN + ny
                        self.boxes[nind].coin = (abs(self.boxes[nind].coin) + 1) * self.player
                        # 添加动画
                        box.coin_mobject[count].move_to(box)
                        self.anims.append(
                            box.coin_mobject[count].animate.shift(DIR[i] * self.side_length)
                        )
                        count += 1
        if len(self.anims) > 0:
            self.play(*self.anims, run_time=0.5)
            for box in self.boxes:
                box.refresh_coin_mobject()
        return flag

    def init_info(self):
        text = Text("点击格子可以下棋\n"
                    "每个格子只能有一种颜色的棋子\n"
                    "当格子中的棋子数量达到上限时\n"
                    "即角上为2，边上为3，中间为4\n"
                    "那么棋子将会从这个格子溢出，\n"
                    "溢出时会将相邻的格子的棋子占\n"
                    "为己有\n\n"
                    "游戏规则：\n"
                    "哪方先将对方所有棋子占有，则\n"
                    "该方获胜", font="Sans").scale(0.5).to_edge(LEFT)
        self.add(text)
        self.game_over = Text("Game Over").add_background_rectangle(color=BLACK, buff=0.25).to_edge(DOWN)

    def setup(self):
        self.init_boxes()
        self.init_player()
        self.init_info()
