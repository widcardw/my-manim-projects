# from my_videos.glitch.functions import relu, linear_step
from manimlib import *


class OneHorizontalPiece(VMobject):
    CONFIG = {
        "angle": 0
    }

    def __init__(self, vmobject: VMobject, x_range: np.ndarray, **kwargs):
        super().__init__(**kwargs)
        self.set_points(vmobject.get_all_points())
        x_min, x_max = x_range
        for i in range(len(self.data['points'])):
            p = self.data['points'][i]
            self.data['points'][i] = np.array([p[0], np.clip(p[1], x_min, x_max), p[2]])
        self.match_style(vmobject)
        self.set_stroke(width=0)


class HorizontalPieces(VGroup):
    def __init__(self, vmobject: VMobject, pieces_num=6, **kwargs):
        super().__init__(**kwargs)
        height = vmobject.get_height()
        bottom = vmobject.get_bottom()[1]  # 底部的纵坐标
        for i in range(pieces_num):
            p = np.array([i, i + 1]) / pieces_num * height + bottom
            self.add(OneHorizontalPiece(vmobject, p))


class Pieces(HorizontalPieces):
    CONFIG = {
        "angle": 0
    }

    def __init__(self, vmobject: VMobject, pieces_num=6, angle=0, **kwargs):
        self.angle = angle
        for sub in vmobject:
            sub.angle = angle
        super().__init__(vmobject.copy().rotate(angle), pieces_num, **kwargs)
        self.rotate(-angle, about_point=vmobject.get_center())


class TestOnePiece(Scene):
    def construct(self):
        squ = Square(fill_opacity=1, color=BLUE, stroke_width=0).scale(3)
        cir = Circle(fill_opacity=1, color=BLUE, stroke_width=0).scale(3)
        # squ = Text("Hello world", stroke_width=0).scale(4)
        pieces = Pieces(squ, 10, PI / 6)
        self.play(ClipGrow(pieces))
        self.wait()
        self.play(FadeOut(pieces))
        pieces2 = HorizontalPieces(cir, 10)
        self.play(ClipGrowFromDown(pieces2))
        self.wait()


class ClipGrowFromDown(Animation):
    CONFIG = {
        "lag_ratio": 0
    }

    def interpolate_submobject(self, submobject, starting_sumobject, alpha):
        height = starting_sumobject.get_height()
        bottom = starting_sumobject.get_bottom()[1]
        p = np.array([bottom, bottom + height * alpha])
        submobject.become(OneHorizontalPiece(starting_sumobject, p))


class ClipGrow(ClipGrowFromDown):
    def create_starting_mobject(self):
        return self.mobject.copy().rotate(-self.mobject.angle)

    def interpolate_submobject(self, submobject, starting_sumobject, alpha):
        angle = starting_sumobject.angle
        height = starting_sumobject.get_height()
        bottom = starting_sumobject.get_bottom()[1]
        p = np.array([bottom, bottom + height * alpha])
        submobject.become(
            OneHorizontalPiece(starting_sumobject, p) \
                .rotate(angle, about_point=starting_sumobject.get_center())
        )
