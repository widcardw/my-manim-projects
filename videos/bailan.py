import random
from manimlib import *


class BgText(Text):
    CONFIG = {
        "stroke_width": 6,
        "stroke_color": BLACK,
        "draw_stroke_behind_fill": True
    }


# save_state 好像执行失败了
class 超牛逼文字动画(Scene):
    def construct(self):
        text1 = BgText("超牛逼", font="serif", weight=BOLD, stroke_color=RED).scale(3)
        text2 = BgText("文字动画", font="serif", weight=BOLD, stroke_color=RED).scale(3)
        VGroup(text1, text2).arrange(DOWN)
        chars = VGroup(*text1, *text2)
        ll = [0, 1, 2, 3, 4, 5, 6]
        self.add(chars)
        for char in chars:
            char.save_state()

        def objanim1(obj):
            return obj.animate.scale(1 + random.random())

        def objanim2(obj):
            return obj.animate.restore()

        for k in range(60):
            random.shuffle(ll)
            self.play(*[
                objanim1(chars[i]) if i % 2 == random.randint(0, 1) else objanim2(chars[i])
                for i in ll
            ], run_time=0.15, rate_func=linear)

        self.wait()


class 灯笼(VGroup):
    def __init__(self):
        super(灯笼, self).__init__()
        cir = Circle(fill_color=RED, fill_opacity=1, stroke_color=YELLOW).set_height(1.5, True).scale(2)
        福 = BgText("福", font="Source Han Serif SC", weight=BOLD, fill_color=BLACK, stroke_color=YELLOW,
                   stroke_width=6).scale(2.5)
        rect = Rectangle(fill_color=RED, fill_opacity=1, stroke_color=YELLOW).set_width(1.5)
        rect.next_to(cir, UP, buff=-0.5)
        rec = Difference(rect, cir)
        rec.set_style(fill_color=RED, fill_opacity=1, stroke_color=YELLOW, stroke_width=6)
        rec2 = rec.copy().rotate(PI, about_point=ORIGIN)
        须 = VGroup(*[Rectangle(width=0.2, height=3, stroke_color=YELLOW, fill_color=RED, fill_opacity=1)
                     for i in range(4)]).arrange(RIGHT).next_to(rec2, DOWN, buff=0)
        self.add(rec, cir, 福, 须, rec2)


class 超牛逼灯笼旋转(Scene):
    def construct(self):
        d = 灯笼().move_to(RIGHT * 10)
        self.add(d)
        self.play(d.animate.move_to(LEFT * 2), runtime=1.5)
        self.v = RIGHT * 12
        self.a = RIGHT / 10 + DOWN / 20

        def 转灯笼(obj, dt):
            omega = TAU * 10
            offset = UP / 4

            obj.rotate(omega * dt, about_point=obj.get_center() + offset)
            obj.shift(self.v * dt)
            self.v += self.a * dt
            self.a = (np.random.random(3) - 0.5) / 10

        d.add_updater(转灯笼)
        self.wait(3)


class 福字(VGroup):
    def __init__(self, omega=TAU):
        super(福字, self).__init__()
        福 = Text("福", font="serif", weight=BOLD, fill_color=BLACK).scale(2.5)
        bg = Square(stroke_color=YELLOW, fill_color=RED, fill_opacity=1).rotate(PI / 4)
        self.v = np.zeros(3)
        self.omega = omega
        self.add(bg, 福)


class 超牛逼转福字(Scene):
    def construct(self):
        f1 = 福字(PI / 2).shift(DL)
        f2 = 福字().shift(UR)
        f3 = 福字(-TAU)
        f4 = 福字(PI).scale(0.7)
        f5 = 福字(-TAU)

        def 转圈圈(obj: 福字, dt):
            obj.rotate(obj.omega * dt)
            obj.scale(1.001)
            r = (np.random.random(3) - 0.5) / 5
            r[2] = 0
            obj.v += dt * r
            obj.shift(obj.v)
            pos = obj.get_center()
            if pos[0] < -7 or pos[0] > 7:
                obj.v[0] *= -1
                # obj.shift((- obj.get_center()) /2)
            if pos[1] < -4 or pos[1] > 4:
                obj.v[1] *= -1

        def 自转(obj, dt):
            omega = TAU * 5
            obj[1].rotate(omega * dt)

        self.add(f1, f2, f3, f4, f5)
        f1.add_updater(转圈圈)
        f2.add_updater(转圈圈)
        f3.add_updater(转圈圈)
        f4.add_updater(转圈圈)
        f5.add_updater(转圈圈)
        f2.add_updater(自转)
        f5.add_updater(自转)
        # self.wait(30)
