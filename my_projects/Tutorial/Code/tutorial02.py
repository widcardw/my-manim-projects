from manimlib.imports import *
from manim_sandbox.utils.imports import *


# 注意:DarkScene为我自定义背景色的场景,
# 若想要使用,请将以下代码取消注释
# class DarkScene(Scene):
# 	CONFIG = {"camera_config":{"background_color":"#1f252A"}}

# dt
# 1s == 30frames => dt == 1/30 s


class UpdateDtScene1(DarkScene):
    def construct(self):
        numline = NumberLine(include_numbers=True)
        dot = Dot(LEFT * 3).scale(2)

        def anim(obj, dt):
            print(dt)
            obj.shift(dt * RIGHT)

        dot.add_updater(anim)
        self.add(numline, dot)
        self.wait(3)


class UpdateShiftScene(DarkScene):
    def construct(self):
        dot = Dot(LEFT * 7)
        dot.add_updater(lambda a, dt: a.shift(RIGHT * 0.04))  # 含时间
        text = TextMobject("This is some text.")
        self.add(dot)
        self.play(Write(text))
        self.wait()
        self.play(Uncreate(text))
        self.wait()


class DtScene2(DarkScene):
    def construct(self):
        numline = NumberLine(include_numbers=True)
        dot = Dot(LEFT * 7 + UP * 0.5, color=YELLOW).scale(2)
        dec = DecimalNumber(0).shift(UP)
        dec.add_updater(lambda a: a.set_value(dot.get_center()[0]))

        def anim(obj, dt):
            obj.shift(RIGHT * dt * 4)

        dot.add_updater(anim)
        self.add(numline, dot, dec)
        self.wait(3.5)


class DtEllipseScene(DarkScene):
    def construct(self):
        self.t = 0
        axes = Axes().set_opacity(0.3)
        orbit = Ellipse(width=8, height=6)
        planet = Dot(color=YELLOW).scale(2)
        dec = DecimalNumber(0).to_corner(UR)
        dec.add_updater(lambda a: a.set_value(
            self.t))  # 没有包含时间,但在wait过程中仍然保持更新

        def anim(obj, dt):
            obj.move_to(np.array([4 * np.cos(self.t), 3 * np.sin(self.t), 0]))
            self.t += dt

        planet.add_updater(anim)
        self.add(axes, orbit, planet, dec)
        self.wait(8)


class SaveStateRestoreScene(DarkScene):
    def construct(self):
        sq = Square(side_length=2, color=BLUE)
        sq.save_state()
        self.play(sq.shift, RIGHT * 4)
        self.play(sq.restore)
        self.wait(0.3)
        self.play(sq.become, TextMobject("This is a square."))
        self.wait(0.3)
        self.play(Restore(sq))


class DtFourierScene(DarkScene):
    def construct(self):
        axes = Axes()
        vec1 = Vector(RIGHT, color=YELLOW)
        cir1 = Circle(radius=1, color=BLUE)
        gup1 = VGroup(vec1, cir1)

        vec2 = Vector(RIGHT, color=YELLOW)
        cir2 = Circle(radius=1, color=BLUE)
        gup2 = VGroup(vec2, cir2)
        gup2.save_state()

        def anim1(obj, dt):
            obj.rotate(dt, about_point=ORIGIN)

        def anim2(obj):
            obj.restore()
            obj.rotate(-vec1.get_angle())
            obj.shift(vec1.get_vector())

        gup1.add_updater(anim1)
        gup2.add_updater(anim2)

        path = TracedPath(vec2.get_end, stroke_width=6, stroke_color=ORANGE)
        path.add_updater(lambda a, dt: a.shift(DOWN * dt))
        self.add(axes, gup1, gup2, path)
        self.wait(6)


class LastSceneHelp(DarkScene):
    def construct(self):
        axes = Axes()
        vec1 = Vector(RIGHT, color=YELLOW_E)
        cir1 = Circle(radius=1, color=BLUE_E)
        gup1 = VGroup(vec1, cir1)

        vec2 = Vector(RIGHT, color=YELLOW)
        cir2 = Circle(radius=1, color=BLUE)
        gup2 = VGroup(vec2, cir2)
        gup2.save_state()

        text1 = TextMobject("Group1").add_updater(
            lambda a: a.next_to(gup1, LEFT))
        text2 = TextMobject("Group2").add_updater(
            lambda a: a.next_to(gup2, RIGHT))

        code0 = CodeLine(r"""def anim1(obj, dt):
	obj.rotate(dt, about_point=ORIGIN)""").scale(2).shift(RIGHT * 3.9 + DOWN * 2)
        code0[0:3].set_color(PURPLE_A)
        code0[10:13].set_color(YELLOW_D)
        code0[15:17].set_color(YELLOW_D)
        code0[-19:-8].set_color(YELLOW_D)

        code = CodeLine(r"""def anim2(obj):
	obj.restore()
	obj.rotate(-vec1.get_angle())
	obj.shift(vec1.get_vector())""").scale(2).next_to(code0, DOWN, aligned_edge=LEFT)
        code[0:3].set_color(PURPLE_A)
        code[10:13].set_color(YELLOW_D)

        point = TexMobject("\\blacktriangleright",
                           color=YELLOW).next_to(code0[0], LEFT)

        self.add(gup1, gup2, text1, text2, code, point, code0)
        self.play(gup2.shift, vec1.get_vector(), run_time=0.5)
        self.add(vec2.copy().set_opacity(0.2),
                 cir2.copy().set_stroke(opacity=0.2))
        self.wait(0.2)

        for i in range(10):
            self.play(point.next_to, code0[21], LEFT, run_time=0.3)
            self.play(MRotate(gup1, radians=PI / 5,
                              about_point=ORIGIN), run_time=0.7)
            self.play(point.next_to, code[17], LEFT, run_time=0.3)
            self.play(gup2.restore, run_time=0.7)
            self.play(point.next_to, code[32], LEFT, run_time=0.3)
            self.play(MRotate(gup2, radians=-vec1.get_angle(),
                              about_point=ORIGIN), run_time=0.7)
            self.play(point.next_to, code[63], LEFT, run_time=0.3)
            self.play(gup2.shift, vec1.get_vector(), run_time=0.7)
            self.add(vec2.copy().set_opacity(0.2),
                     cir2.copy().set_stroke(opacity=0.2))

        def anim1(obj, dt):
            obj.rotate(dt, about_point=ORIGIN)

        def anim2(obj):
            obj.restore()
            obj.rotate(-vec1.get_angle())
            obj.shift(vec1.get_vector())

        gup1.add_updater(anim1)
        gup2.add_updater(anim2)
        text1.clear_updaters()
        text2.clear_updaters()
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(point))
        self.wait(2 * TAU)
