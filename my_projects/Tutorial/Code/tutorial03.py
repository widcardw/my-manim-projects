from manimlib.imports import *
from manim_sandbox.utils.imports import *


# 注意:DarkScene为我自定义背景色的场景,
# 若想要使用,请将以下代码取消注释
# class DarkScene(Scene):
# 	CONFIG = {"camera_config":{"background_color":"#1f252A"}}


class UpdateFromFuncExample(DarkScene):
    def construct(self):
        square = Square().to_edge(UP)
        mobject = TextMobject("Text").scale(2).next_to(square, RIGHT)

        def update_func(mob):
            mob.next_to(square, RIGHT)

        self.add(square, mobject)
        self.wait()
        self.play(
            square.to_edge, DOWN,
            UpdateFromFunc(mobject, update_func)
        )
        self.wait()


class UpdateFromFuncExample2(DarkScene):
    def construct(self):
        sq1 = Square(color=RED, side_length=1).shift(UP * 2.25 + LEFT * 5)
        sq2 = Square(color=BLUE, side_length=1).shift(LEFT * 5 + UP * 0.75)
        sq3 = Square(color=YELLOW, side_length=1).shift(LEFT * 5 + DOWN * 0.75)
        sq4 = Square(color=GREEN, side_length=1).shift(LEFT * 5 + DOWN * 2.25)

        dt = 1 / self.camera.frame_rate

        def anim(obj):
            obj.shift(RIGHT * dt * 2)
            obj.rotate(0.4 * TAU * dt)

        self.add(sq1, sq2, sq3, sq4)
        self.play(UpdateFromFunc(sq1, anim),

                  sq2.shift, RIGHT * 10,
                  Rotating(sq2),

                  Rotating(sq3),
                  sq3.shift, RIGHT * 10,

                  sq4.rotate, PI,
                  sq4.shift, RIGHT * 10,
                  run_time=5 - dt, rate_func=linear)


class EnvelopFunc(DarkScene):
    def construct(self):
        sq1 = Square(color=RED, side_length=2).shift(UP * 2 + LEFT * 5)
        sq2 = Square(color=RED, side_length=2).shift(UP * 2 + LEFT * 5) \
            .set_stroke(width=0.5, opacity=0.5)
        dt = 1 / self.camera.frame_rate
        en = VGroup()
        self.add(sq1, sq2, en, sq2.copy())

        def anim(obj):
            obj.shift(RIGHT * dt * 2)
            obj.rotate(0.4 * TAU * dt)
            en.add(obj.copy())

        def anim2(obj):
            obj.shift(RIGHT * dt)
            obj.rotate(0.2 * TAU * dt)

        sq4 = Square(color=GREEN, side_length=2).shift(LEFT * 5 + DOWN * 2)
        dot0 = Dot(sq4.get_vertices()[0], color=BLUE).scale(2)
        dot1 = Dot(sq4.get_vertices()[1], color=YELLOW).scale(2)
        dot2 = Dot(sq4.get_vertices()[2], color=ORANGE).scale(2)
        dot3 = Dot(sq4.get_vertices()[3], color=PURPLE_A).scale(2)
        vg1 = VGroup(sq4, dot0, dot1, dot2, dot3)
        self.add(vg1)

        self.wait()
        self.play(UpdateFromFunc(sq2, anim),
                  FadeIn(vg1.copy().shift(
                      RIGHT * 10).rotate(PI).set_stroke(opacity=0.3)),
                  run_time=5 - 2 * dt, rate_func=linear)
        self.wait()
        self.play(UpdateFromFunc(sq1, anim2),

                  vg1.shift, RIGHT * 10,
                  vg1.rotate, PI,

                  run_time=10 - 2 * dt, rate_func=linear)
        self.wait()


class MoveAlongPathWithAlphaScene(DarkScene):
    def construct(self):
        line = Line(LEFT * 4, RIGHT * 4, color=BLUE).shift(UP * 2.5)
        cir = Circle().shift(LEFT * 3 + DOWN).scale(2)
        sinfunc = ParametricFunction(
            lambda t: np.array([t, np.sin(t), 0]), t_min=-PI / 2, t_max=PI / 2) \
            .shift(RIGHT * 2 + DOWN).set_color(YELLOW)
        dot0 = Dot()
        dot1 = Dot()
        dot2 = Dot()

        def anim0(obj, alpha):
            obj.move_to(line.point_from_proportion(alpha))

        def anim1(obj, alpha):
            obj.move_to(cir.point_from_proportion(alpha))

        def anim2(obj, alpha):
            obj.move_to(sinfunc.point_from_proportion(alpha))

        self.play(ShowCreation(line),
                  ShowCreation(cir),
                  ShowCreation(sinfunc))

        self.add(dot0, dot1, dot2)
        debugPoints(self, line)
        debugPoints(self, cir)

        self.play(UpdateFromAlphaFunc(dot0, anim0),
                  UpdateFromAlphaFunc(dot1, anim1),
                  UpdateFromAlphaFunc(dot2, anim2),
                  run_time=5, rate_func=linear)


class debugPointsScene(DarkScene):
    def construct(self):
        obj = Circle().scale(3)
        obj.points[1:4] += RIGHT
        self.add(obj)
        debugPoints(self, obj)


# alpha
# point_from_proportion(alpha)
class UpdateFromAlphaFuncExample(DarkScene):
    def construct(self):
        line = DashedVMobject(Line(LEFT * 5, RIGHT * 5).set_color(GREY))
        sq = Square(side_length=1, color=BLUE).shift(LEFT * 5)
        sq.save_state()

        def anim(obj, alpha):
            obj.restore()
            obj.shift(RIGHT * alpha * 10)
            obj.rotate(PI * 3 * alpha)

        self.add(sq, line)
        self.play(UpdateFromAlphaFunc(sq, anim),
                  run_time=5)


class ExplainExample1(DarkScene):

    def construct(self):
        t2c_dic = {"def": PURPLE_B,
                   "anim": TEAL_D,
                   "restore": BLUE_D,
                   "shift": BLUE_D,
                   "rotate": BLUE_D,
                   "save_state": BLUE_D}
        code = CodeLine(r"""sq.save_state()

def anim(obj, alpha):
    obj.restore()
    obj.shift(RIGHT*alpha*10)
    obj.rotate(PI*3*alpha)""", t2s={"def": ITALIC}).scale(2).to_corner(DR, buff=1)
        code.set_color_by_t2c(t2c_dic)
        code[26:29].set_color(ORANGE)
        self.add(code)
        text = TexMobject("\\blacktriangleright",
                          color=YELLOW).next_to(code[0], LEFT)
        self.add(text)
        line = Line(LEFT * 5, RIGHT * 5).set_color(GREY)
        sq = Square(side_length=1, color=BLUE).shift(LEFT * 5)
        sq.save_state()

        def anim(obj, alpha):
            obj.restore()
            obj.shift(RIGHT * alpha * 10)
            obj.rotate(PI * 3 * alpha)

        self.add(line, sq)

        verticalL = VGroup(*[DashedLine(UP, DOWN, color=GREY).move_to(
            line.point_from_proportion(i / 10)) for i in range(11)])
        numG = VGroup(*[DecimalNumber(i / 10, num_decimal_places=1).scale(0.6).next_to(verticalL[i], UP)
                        for i in range(11)])
        self.add(verticalL, numG)

        self.wait()
        self.add(sq.copy().set_stroke(opacity=0.35, color=WHITE))
        for i in range(1, 11):
            self.play(text.next_to, code[43], LEFT, run_time=0.3)
            self.play(sq.restore, run_time=0.7)
            self.play(text.next_to, code[61], LEFT, run_time=0.3)
            self.play(sq.shift, RIGHT * i, run_time=0.7)
            self.play(text.next_to, code[91], LEFT, run_time=0.3)
            self.play(MRotate(sq, radians=PI * 3 * i / 10), run_time=0.7)
            self.add(sq.copy().set_stroke(opacity=0.35, color=WHITE))

        self.play(sq.restore)
        self.play(UpdateFromAlphaFunc(sq, anim),
                  run_time=10, rate_func=linear)
        self.wait()


class EnvelopeExampleScene(DarkScene):
    def construct(self):
        dot_o = Dot(RIGHT * 2.2)
        cir_o = Circle(radius=1.5, color=GREEN)
        dot_p = Dot()
        cir_p = Circle()
        enve = VGroup()
        self.i = 0

        def anim(obj, alpha):
            obj.move_to(cir_o.point_from_proportion(alpha))
            cir_p.become(Circle(radius=abs(get_norm(dot_o.get_center() - dot_p.get_center())),
                                color=BLUE, plot_depth=2).move_to(dot_p.get_center()))
            if self.i % 6 == 0:
                enve.add(cir_p.copy().set_stroke(color=PURPLE, width=1))
            self.i += 1

        self.add(dot_o, cir_o, dot_p, cir_p, enve)
        self.play(UpdateFromAlphaFunc(dot_p, anim),
                  run_time=6, rate_func=linear)
