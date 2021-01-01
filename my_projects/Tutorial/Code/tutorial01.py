from manimlib.imports import *
from manim_sandbox.utils.imports import *


# 注意:DarkScene为我自定义背景色的场景,
# 若想要使用,请将以下代码取消注释
# class DarkScene(Scene):
# 	CONFIG = {"camera_config":{"background_color":"#1f252A"}}


class UpdateScene(DarkScene):
    def construct(self):
        dot = Dot(LEFT * 3 + DOWN * 2)
        text = TextMobject("This is some text.").next_to(dot, RIGHT)

        text.add_updater(lambda a: a.next_to(dot, RIGHT))

        # def anim(obj):
        # 	obj.next_to(dot, RIGHT)
        # text.add_updater(anim)

        self.add(dot, text)
        self.play(dot.shift, UP * 4, rate_func=there_and_back, run_time=2)
        # text.remove_updater(lambda a:a.next_to(dot, RIGHT)) ERROR
        text.clear_updaters()
        self.play(dot.shift, UP * 4, rate_func=there_and_back, run_time=2)


class EnvelopeScene2(DarkScene):
    def construct(self):
        dot = Dot(LEFT * 3 + DOWN * 2)
        text = TextMobject("This is some text.").next_to(dot, RIGHT)
        envelope = VGroup()

        text.add_updater(lambda a: a.next_to(dot, RIGHT))
        envelope.add_updater(lambda a: a.add(
            text.copy().clear_updaters().set_opacity(0.2)))

        self.add(dot, text, envelope)
        self.play(dot.shift, UP * 4, rate_func=there_and_back, run_time=2)


class ValueTrackerScene(DarkScene):
    def construct(self):
        t = ValueTracker(-2)
        numline = NumberLine()
        triangle = Triangle(fill_opacity=1, color=YELLOW).scale(0.1).rotate(PI).move_to(
            np.array([-2, 0.5, 0]))
        dec = DecimalNumber(0)
        triangle.add_updater(lambda a: a.move_to(
            np.array([t.get_value(), 0.5, 0])))
        dec.add_updater(lambda a: a.set_value(t.get_value()))
        dec.add_updater(lambda a: a.next_to(triangle, UP))
        self.add(numline, triangle, dec)
        self.play(t.set_value, 2, rate_func=there_and_back, run_time=3)


class ValueTrackerScene2(DarkScene):
    def construct(self):
        t = ValueTracker(0)
        cir = Circle(radius=2).shift(LEFT * 5)
        dot_o = Dot(LEFT * 5)
        dot_a = Dot(LEFT * 3)
        l_oa = Line(LEFT * 5, LEFT * 3)
        dot_p = Dot().add_updater(lambda a: a.move_to(
            np.array([-5 + 2 * np.cos(t.get_value()), 2 * np.sin(t.get_value()), 0])))
        l_op = Line().add_updater(lambda a: a.put_start_and_end_on(
            dot_o.get_center(), dot_p.get_center()))
        arc = Arc(angle=0).add_updater(lambda a: a.become(
            Arc(start_angle=0, angle=t.get_value() % TAU, color=ORANGE).shift(LEFT * 5)))
        self.add(cir, dot_o, dot_a, dot_p, l_oa, l_op, arc)
        self.play(t.set_value, 2 * TAU, run_time=8, rate_func=linear)


class ValueTrackerScene3(DarkScene):
    def construct(self):
        t = ValueTracker(0)
        cir = Circle(radius=2).shift(LEFT * 5)
        dot_p = Dot().add_updater(lambda a: a.move_to(
            np.array([-5 + 2 * np.cos(t.get_value()), 2 * np.sin(t.get_value()), 0])))
        dot_q = Dot().add_updater(lambda a: a.move_to(
            np.array([-2, 2 * np.sin(t.get_value()), 0])))
        l_pq = DashedLine().add_updater(lambda a: a.put_start_and_end_on(
            dot_p.get_center(), dot_q.get_center()))

        path = TracedPath(dot_q.get_center, stroke_width=6,
                          stroke_color=YELLOW)
        path.add_updater(lambda a: a.shift(RIGHT * 0.04))

        self.add(cir, dot_p, dot_q, l_pq, path)
        self.play(t.set_value, 2 * TAU, run_time=8, rate_func=linear)


class UpdateShiftScene(Scene):
    def construct(self):
        dot = Dot(LEFT * 7)
        dot.add_updater(lambda a: a.shift(RIGHT * 0.04))
        text = TextMobject("This is some text.")
        self.add(dot)
        self.play(Write(text))
        self.wait()
        self.play(Uncreate(text))
        self.wait()


class UpdateDtScene(Scene):
    def construct(self):
        dot = Dot(LEFT * 7)

        def anim(obj, dt):
            obj.shift(RIGHT * 0.05)

        dot.add_updater(anim)
        text = TextMobject("This is some text.")
        self.add(dot)
        self.play(Write(text))
        self.wait()
        self.play(Uncreate(text))
        self.wait()


# 暂存第二期场景

class UpdateDtScene2(DarkScene):
    def construct(self):
        numline = NumberLine(include_numbers=True)
        dot = Dot(LEFT * 7 + UP * 0.5)
        dec = DecimalNumber(0).shift(UP)

        def anim(obj, dt):
            obj.shift(dt * RIGHT)

        dot.add_updater(anim)
        dec.add_updater(lambda a: a.set_value(dot.get_center()[0]))
        self.add(numline, dot, dec)
        self.wait(14)


class DtEllipseScene(DarkScene):
    def construct(self):
        self.t = 0
        axes = Axes().set_opacity(0.2)
        elp = Ellipse(width=8, height=6)
        dot_p = Dot().scale(2)
        dec = DecimalNumber(0).to_corner(UR)
        dec.add_updater(lambda a: a.set_value(self.t))  # 没有包含时间,但仍然能够进行更新

        def anim(obj, dt):
            obj.move_to(np.array([4 * np.cos(self.t), 3 * np.sin(self.t), 0]))
            self.t += dt

        dot_p.add_updater(anim)

        self.add(axes, elp, dot_p, dec)
        self.wait(8)


class SaveStateRestore(DarkScene):
    def construct(self):
        sq = Square(side_length=2)
        sq.save_state()
        self.add(sq)
        self.wait(0.3)
        self.play(sq.shift, RIGHT * 3)
        self.play(sq.restore)
        self.play(sq.become, TextMobject("This is a square."))
        self.wait(0.3)
        self.play(sq.restore)


class DtFourierScene(DarkScene):
    def construct(self):
        axes = Axes()
        vec1 = Vector(RIGHT, color=YELLOW)
        cir1 = Circle(radius=1, color=BLUE)
        rad1 = VGroup(vec1, cir1)

        self.add(axes)
