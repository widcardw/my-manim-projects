from manimlib.imports import *
from manim_sandbox.utils.imports import *


class Scene_(Scene):
    CONFIG = {"camera_config": {"background_color": GREY}}


class Scene1(Scene_):
    def construct(self):
        line1 = Line(ORIGIN, UP * 3, color=WHITE)
        path1 = TracedPath(line1.get_end, stroke_color=WHITE, stroke_width=5)
        line2 = Line(ORIGIN, DOWN * 3, color=BLACK)
        path2 = TracedPath(line2.get_end, stroke_color=BLACK, stroke_width=5)
        line1.save_state()
        line2.save_state()
        dot1 = Dot(ORIGIN, color=BLACK).scale(0.3)
        dot2 = Dot(ORIGIN, color=WHITE).scale(0.3)
        path11 = TracedPath(
            dot1.get_center, stroke_color=BLACK, stroke_width=5)
        path22 = TracedPath(
            dot2.get_center, stroke_color=WHITE, stroke_width=5)
        group1 = VGroup(line1, dot1)
        group2 = VGroup(line2, dot2)

        def ro(l, alpha):
            l[0].restore()
            l[0].rotate(PI * alpha, about_point=l[0].get_start())
            l[1].move_to(l[0].point_from_proportion(np.sin(alpha / PI * 5)))

        self.add(line1, line2, path1, path2, path11, path22)
        self.wait(0.1)
        self.play(UpdateFromAlphaFunc(group1, ro),
                  UpdateFromAlphaFunc(group2, ro),
                  rate_func=linear, run_time=6)
        self.remove(line1, line2, dot1, dot2)
        self.wait(0.1)


class OffsetExample(Scene):
    def construct(self):
        tex = TexMobject(
            r"1-{1\over 2}+{1\over 2}-{1\over 3}+{1\over 3}-{1\over 4}+\cdots+{1\over {n-1}}-{1\over n}")
        self.add(tex)
        debugTeX(self, tex[0])
        # self.play(*[ShowCreationThenDestruction(SurroundingRectangle(obj))
        #     for obj in [tex[0][1:5],tex[0][5:9],tex[0][9:13],tex[0][13:17],tex[0][25:31]]],
        #     run_time=1.5, rate_func=sine)
        # self.wait()
        # self.play(*[FadeOutAndShift(obj, RIGHT*0.5, path_arc=-PI/2)
        #     for obj in [tex[0][1:5],tex[0][9:13],tex[0][17:21]]],
        #     *[FadeOutAndShift(obj, LEFT*0.5, path_arc=-PI/2)
        #     for obj in [tex[0][5:9],tex[0][13:17],tex[0][21:25],tex[0][25:31]]],
        #     run_time=2, rate_func=sine)
        # self.wait()
        # self.play(tex[0][0].shift,RIGHT*4.2,tex[0][31:].shift,LEFT*4.2)
        # self.wait()


class TestBrace(Scene):
    def construct(self):
        t1 = ValueTracker(2)
        t2 = ValueTracker(2)

        rect = Rectangle().add_updater(lambda a: a.become(Rectangle(
            width=t1.get_value(), height=t2.get_value()
        )))
        brace_l = Brace(rect, LEFT)
        label_l = DecimalNumber(0)
        brace_d = Brace(rect, DOWN)
        label_d = DecimalNumber(0)

        brace_l.add_updater(lambda a: a.become(Brace(rect, LEFT)))
        brace_d.add_updater(lambda a: a.become(Brace(rect, DOWN)))
        label_l.add_updater(lambda a: a.set_value(
            t1.get_value()).next_to(brace_l, LEFT))
        label_d.add_updater(lambda a: a.set_value(
            t2.get_value()).next_to(brace_d, DOWN))

        self.add(rect, brace_l, brace_d, label_l, label_d)
        self.play(t1.set_value, 8,
                  t2.set_value, 4)


class MyTextExp(Scene):
    def construct(self):
        arrow = Vector(RIGHT * 4)
        self.add(arrow)


class TeXLaTeX(NewGraphScene):
    def construct(self):
        cir = Circle().scale(3)
        pot = AllPointsIndex(cir)
        # pot.add_updater(lambda a: a.become(AllPointsIndex(cir)))
        pot.update_position(cir)
        self.add(cir, pot)
        self.play(ShowCreation(cir))
        self.play(cir.shift, RIGHT * 2)
        squ = Square().scale(2)
        # pot.clear_updaters()
        # pot.update_obj(squ)
        # pot.update_position(squ)
        self.play(Transform(cir, squ))
        self.wait()


class TestArrow(Scene):
    def construct(self):
        dots = np.array([
            [-3, -3, 0],
            [-1, -2, 0],
            [0, 2, 0],
            [3, -2, 0],
            [4, 1, 0]
        ])
        path = TipableVMobject()
        path.set_points_smoothly(dots)
        path.add_tip(tip_look=1)
        self.add(path)


class TestVMobject(Scene):
    def construct(self):
        dots = np.array([
            [-6, -3, 0],
            [-5, 3, 0],
            [-4, 2, 0],
            [-3, -1, 0],
            [-2, 2, 0],
            [-1, 0, 0],
            [0, 3.5, 0],
            [1, 2, 0]
        ])
        for i in dots:
            self.add(Dot(i))
        path = VMobject(n_points_per_cubic_curve=8)
        path.points = dots
        self.add(path)


class ColorByCaracterFixed(Scene):
    def construct(self):
        text = Text("高中数学", font="等线 Bold")
        self.play(Write(text))
        self.wait(2)


class Danmaku(Scene):
    def construct(self):
        n = 130
        color_list = [RED, ORANGE, GOLD, YELLOW, GREEN, TEAL, BLUE, PURPLE]
        dg = VGroup(*[Dot(np.array([7 * (i / n) ** 1.8, 0, 0])).scale(3 * i / n)
                      for i in range(n)]).set_color_by_gradient(*color_list)

        def anim(obj, dt):
            for i in range(n):
                obj[i].rotate((n - i) / n * 8 * dt, about_point=ORIGIN)

        dg.add_updater(anim)
        self.add(dg)
        self.wait(100)


class TestPlot(Scene):
    def construct(self):
        cir = Circle(fill_opacity=1, radius=2).set_plot_depth(1)
        squ = Square(fill_opacity=1).set_plot_depth(2)
        self.add(squ)
        self.add(cir)