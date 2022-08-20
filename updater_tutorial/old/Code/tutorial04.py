from manimlib.imports import *
from manim_sandbox.utils.imports import *


class RollingWheel(DarkScene):
    def construct(self):
        t2c = {"def": PURPLE_B, "anim": TEAL, "VGroup": BLUE, "UpdateFromAlphaFunc": BLUE,
               "set_value": BLUE_D, "save_state": BLUE_D, "self": RED, "run_time": ORANGE,
               ".": GREY, ",": GREY, "=": "#fa8763"}
        ap = TexMobject("\\alpha=").shift(DOWN * 3 + LEFT * 0.7)
        dec = DecimalNumber(0).next_to(ap, RIGHT)
        l = Line(LEFT * 7, RIGHT * 7).shift(DOWN * 2)
        cir = Circle(radius=1).shift(LEFT * PI + DOWN)
        vec = Vector(DOWN, color=YELLOW).shift(LEFT * PI + DOWN)
        gup = VGroup(cir, vec)
        self.play(ShowCreation(l))
        self.play(ShowCreation(gup))

        code = CodeLine(r"""gup = VGroup(cir,vec)
gup.save_state()

def anim(obj, alpha):
    obj.restore()
    obj.shift(RIGHT*TAU*alpha)
    obj.rotate(-TAU*alpha)
    dec.set_value(alpha)

self.play(UpdateFromAlphaFunc(gup, anim),
    run_time=4)""", t2s={"def": ITALIC}).scale(2).to_corner(UL)
        code.set_color_by_t2c(t2c)
        self.play(Write(code))
        self.play(Write(ap), Write(dec))
        gup.save_state()

        def anim(obj, alpha):
            obj.restore()
            obj.shift(RIGHT * TAU * alpha)
            obj.rotate(-TAU * alpha)
            dec.set_value(alpha)

        path = TracedPath(vec.get_end, stroke_width=4, stroke_color=ORANGE)
        self.add(path)
        self.play(UpdateFromAlphaFunc(gup, anim), run_time=4, rate_func=sine)
        self.wait()


class DebugTextExample(DarkScene):
    def construct(self):
        text = TextMobject("F").scale(10).shift(LEFT * 4)
        self.add(text)
        cir = Circle(radius=2.5).shift(RIGHT * 4)
        self.add(cir)
        debugPoints(self, text[0][0])
        debugPoints(self, cir)

        # def func(p):
        #     print(p)
        #     for point in p[0][0].points:
        #         point += np.array([
        #             np.sin(point[1]), np.sin(point[0]), 0
        #         ])
        #     return p

        # self.play(ApplyFunction(func, text))
        # self.play(text.apply_function,
        #           lambda p: p + np.array([
        #               np.sin(p[1]), np.sin(p[0]), 0
        #           ]))


class TargetExample(DarkScene):
    def construct(self):
        t2c = {"def": PURPLE_B, "anim": TEAL, "Square": BLUE, "UpdateFromAlphaFunc": BLUE,
               "set_value": BLUE_D, "save_state": BLUE_D, "self": RED, "run_time": ORANGE,
               "lambda": PURPLE_A, "TextMobject": BLUE, "add_updater": BLUE_D, '"': TEAL,
               ".": GREY, ",": GREY, "=": "#fa8763"}
        codeText = r"""sq = Square().shift(LEFT*2)
text = TextMobject("Text")
text.add_updater(lambda t:t.next_to(sq, DOWN))
self.play(sq.shift, RIGHT*4)
"""
        code = CodeLine(codeText, t2s={"lambda": ITALIC}) \
            .scale(2.5).to_corner(UL)
        code.set_color_by_t2c(t2c)
        code[48:52].set_color("#a3ce9e")
        code[79].set_color(ORANGE)
        # self.add(code)
        # debugTeX(code, code)
        sq = Square(side_length=1, color=BLUE).shift(LEFT * 2)
        text = TextMobject("Text").next_to(sq, DOWN).set_plot_depth(2)
        textc = text.copy().set_fill(color=GREY).set_plot_depth(1)
        vec = Vector(UP * 0.7, color=YELLOW).next_to(textc, DOWN) \
            .add_updater(lambda a: a.next_to(textc, DOWN))
        tar = TextMobject("target") \
            .add_updater(lambda a: a.next_to(vec, DOWN))
        self.play(Write(sq), Write(text), Write(tar), Write(textc))
        self.play(Write(code), ShowCreation(vec))
        for i in range(4):
            self.play(sq.shift, RIGHT)
            self.play(textc.shift, RIGHT)
            self.play(text.shift, RIGHT)


class VTExample(DarkScene):
    def construct(self):
        t2c = {"def": PURPLE_B, "anim": TEAL, "Square": BLUE, "UpdateFromAlphaFunc": BLUE,
               "set_value": BLUE_D, "save_state": BLUE_D, "self": RED, "run_time": ORANGE,
               "lambda": PURPLE_A, "TextMobject": BLUE, "add_updater": BLUE_D, '"': TEAL,
               ".": GREY, ",": GREY, "=": "#fa8763", "ValueTracker": BLUE}
        codet = CodeLine("t = ValueTracker()").scale(2.5).set_color_by_t2c(t2c)
        codet.to_edge(UP)
        self.play(Write(codet))
        t = ValueTracker(-TAU)
        dec = DecimalNumber(0).shift(UP * 1 + LEFT * 5) \
            .add_updater(lambda a: a.set_value(t.get_value()))
        path = ParametricFunction(lambda t: np.array([t, np.sin(t) - 1, 0]),
                                  t_min=-8, t_max=8)
        cir = VGroup(Circle(radius=1), Dot(color=ORANGE))
        cir.add_updater(lambda a: a.move_to(np.array([
            t.get_value(), np.sin(t.get_value()) - 1, 0
        ])))
        vec = Vector()
        vec.add_updater(lambda a: a.become(
            Vector(RIGHT, color=YELLOW).rotate(
                np.arctan(np.cos(t.get_value())), about_point=ORIGIN)
            .shift(cir[0].get_center())
        ))
        vec1 = Vector()
        vec1.add_updater(lambda a: a.become(
            Vector(RIGHT, color=YELLOW).rotate(
                np.arctan(np.cos(t.get_value())), about_point=ORIGIN)
            .shift(UP * 1 + RIGHT * 4)
        ))
        self.play(ShowCreation(path), Write(dec),
                  ShowCreation(cir), ShowCreation(vec), ShowCreation(vec1))
        ve1 = Arrow(codet[0].get_center(), dec.get_center(),
                    buff=0.7, color=GREEN)
        ve2 = Arrow(codet[-1].get_center(),
                    vec1.get_start(), buff=0.7, color=GREEN)
        ve3 = Arrow().add_updater(lambda a: a.become(
            Arrow(codet.get_center(), cir.get_center(), color=GREEN, buff=1)
        ))
        texta = TextMobject(r"add_updater", plot_depth=2) \
            .scale(1.5).shift(UP * 2.5).add_background_rectangle(opacity=0.5)
        self.play(ShowCreation(ve1), ShowCreation(
            ve2), ShowCreation(ve3), Write(texta))
        self.wait(0.5)
        self.play(t.set_value, TAU, run_time=6, rate_func=sine)
        self.wait(2)


class TestDt(DarkScene):
    def construct(self):
        dot0 = Dot(UP + LEFT * 5)
        dot1 = Dot(DOWN + LEFT * 5)
        line = Line(UP, DOWN, color=BLUE)
        dot0.add_updater(lambda a, dt: a.shift(RIGHT * dt))
        dot1.add_updater(lambda a: a.shift(RIGHT / self.camera.frame_rate))
        line.add_updater(lambda l: l.move_to(dot0.get_center() + DOWN))
        self.add(dot0, dot1, line)
        self.wait(3)
        self.play(ShowCreation(TextMobject("This is some text.")))
        self.wait(3)


class Example1(DarkScene):
    def construct(self):
        textr = TextMobject("radius=").shift(UP * 1 + RIGHT * 4)
        texta = TextMobject("angle=").shift(DOWN + RIGHT * 4)
        decr = DecimalNumber().next_to(textr)
        deca = DecimalNumber(unit="rad").next_to(texta)
        radius_ = ValueTracker(2)
        ang_ = ValueTracker(PI / 2)
        decr.add_updater(lambda a: a.set_value(radius_.get_value()))
        deca.add_updater(lambda a: a.set_value(ang_.get_value()))
        arc = Arc()
        arc.add_updater(lambda a: a.become(
            Arc(radius=radius_.get_value(), angle=ang_.get_value())
            .shift(LEFT * 3)
        ))
        self.add(textr, texta, decr, deca, arc)
        self.play(radius_.set_value, 3, run_time=2)
        self.play(ang_.set_value, TAU, run_time=2)


# MK作业: 包络线av795077074
# 1:09 抛物线 video by @二茂铁
class Example2(DarkScene):
    def construct(self):
        line = Line(LEFT * 7, RIGHT * 7).shift(UP * 3)
        dotF = Dot(UP)
        dotP = Dot(color=ORANGE)
        l_fp = Line(color=GREEN)
        l_h = Line()
        enve = VGroup()
        self.i = 0

        def anim(obj, alpha):
            obj.move_to(line.point_from_proportion(alpha))
            l_fp.put_start_and_end_on(dotP.get_center(), dotF.get_center())
            l_h.become(l_fp.copy().set_color(BLUE).rotate(PI / 2).scale(20))
            if self.i % 6 == 0:
                enve.add(l_h.copy().set_stroke(width=1, color=BLUE_D))
            self.i += 1

        self.add(line, dotF, dotP, l_fp, l_h, enve)
        self.play(UpdateFromAlphaFunc(dotP, anim),
                  run_time=8, rate_func=linear)


# 4:49 追逐曲线 video by @zgh2000
class Example3(DarkScene):
    def construct(self):
        dotA = Dot(np.array([-3.5, -3.5, 0]))
        dotB = Dot(np.array([3.5, -3.5, 0]))
        dotC = Dot(np.array([3.5, 3.5, 0]))
        dotD = Dot(np.array([-3.5, 3.5, 0]))
        l_ab = Line(dotA.get_center(), dotB.get_center())
        l_bc = Line(dotB.get_center(), dotC.get_center())
        l_cd = Line(dotC.get_center(), dotD.get_center())
        l_da = Line(dotD.get_center(), dotA.get_center())
        l_1 = l_ab.copy()
        l_2 = l_bc.copy()
        l_3 = l_cd.copy()
        l_4 = l_da.copy()
        enve = VGroup()
        gup = VGroup(l_1, l_2, l_3, l_4)
        dt = self.camera.frame_rate

        def anim(obj):
            dotA.shift((dotB.get_center() - dotA.get_center()) * dt)
            dotB.shift((dotC.get_center() - dotB.get_center()) * dt)
            dotC.shift((dotD.get_center() - dotC.get_center()) * dt)
            dotD.shift((dotA.get_center() - dotD.get_center()) * dt)
            obj[0].put_start_and_end_on(dotA.get_center(), dotB.get_center())
            obj[1].put_start_and_end_on(dotB.get_center(), dotC.get_center())
            obj[2].put_start_and_end_on(dotC.get_center(), dotD.get_center())
            obj[3].put_start_and_end_on(dotD.get_center(), dotA.get_center())
            enve.add(obj[0].copy().set_stroke(width=1, color=BLUE),
                     obj[1].copy().set_stroke(width=1, color=BLUE),
                     obj[2].copy().set_stroke(width=1, color=BLUE),
                     obj[3].copy().set_stroke(width=1, color=BLUE))

        self.add(dotA, dotB, dotC, dotD, l_ab, l_bc, l_cd, l_da, gup, enve)
        self.play(UpdateFromFunc(gup, anim), run_time=5, rate_func=linear)


class TestClock(DarkScene):
    def construct(self):
        t2c = {"def": PURPLE_B, "anim": TEAL, "Square": BLUE, "UpdateFromAlphaFunc": BLUE,
               "set_value": BLUE_D, "save_state": BLUE_D, "self": RED, "run_time": ORANGE,
               "lambda": PURPLE_A, "TextMobject": BLUE, "add_updater": BLUE_D, '"': TEAL,
               ".": GREY, ",": GREY, "=": "#fa8763", "ValueTracker": BLUE, "sin": BLUE_D,
               "cos": BLUE_D, "+": "#fa8763", "wait": BLUE_D}
        clock = Clock().scale(2).shift(LEFT * 4)
        self.play(Write(clock))
        codeText = r"""self.t = 0

def anim(obj, dt):
    obj.move_to(np.array([
        np.cos(self.t),
        np.sin(self.t),
        0
    ]))
    self.t += dt
    
text.add_updater(anim)
"""
        code = CodeLine(codeText, t2s={"def": ITALIC, "self": ITALIC}) \
            .scale(2).shift(RIGHT * 4)
        code.set_color_by_t2c(t2c)
        text = TextMobject("Text")
        self.t = 0

        def anim(obj, dt):
            obj.move_to(np.array([
                np.cos(self.t),
                np.sin(self.t),
                0
            ]))
            self.t += dt

        cir = DashedVMobject(Circle(color=GREY, radius=1)).set_plot_depth(-1)
        self.play(Write(code))
        self.play(Write(text), Write(cir))
        self.play(text.shift, RIGHT)

        text.add_updater(anim)

        codeplay = CodeLine("self.play(...)", t2s={"def": ITALIC, "self": ITALIC}) \
            .scale(2).set_color_by_t2c(t2c).next_to(code, DOWN, aligned_edge=LEFT)
        codewait = CodeLine("self.wait(7)", t2s={"def": ITALIC, "self": ITALIC}) \
            .scale(2).set_color_by_t2c(t2c).next_to(codeplay, DOWN, aligned_edge=LEFT)
        self.play(
            Write(codeplay, run_time=1),
            ClockPassesTime(clock, run_time=5, hours_passed=5)
        )
        self.play(
            Write(codewait, run_time=1),
            ClockPassesTime(clock, run_time=7, hours_passed=7)
        )


class Testttt(DarkScene):
    def construct(self):
        sq = Square(side_length=2, color=BLUE).shift(LEFT * 4)
        ci = Circle(radius=2).shift(RIGHT * 4).set_stroke(opacity=0.2)
        text = TextMobject("target").next_to(ci, UP)
        text1 = TextMobject("origin").next_to(sq, UP)
        self.add(sq)
        self.play(Write(text), ShowCreation(ci), Write(text1))
        self.wait()
        vec = Arrow(LEFT * 2, RIGHT * 1.5, color=YELLOW)
        self.play(ShowCreationThenFadeOut(vec))
        self.play(TransformFromCopy(sq, ci.copy().set_stroke(opacity=1)))
        self.wait()


class Envelope(DarkScene):
    def construct(self):
        t = ValueTracker(0.)
        num = 60
        enve = VGroup()
        decn = DecimalNumber(0).to_corner(DR, buff=0.8)
        textn = TexMobject("n=").next_to(decn, LEFT, buff=0.18)
        enve.add(*[Line() for j in range(num)])

        def anim(obj):
            for i in range(num):
                distance = abs(get_norm(np.array([np.cos(i * TAU / num), np.sin(i * TAU / num), 0])
                                        - np.array(
                    [np.cos(t.get_value() * i * TAU / num), np.sin(t.get_value() * i * TAU / num), 0])))
                if distance == 0:
                    obj[i].set_stroke(opacity=0)
                else:
                    obj[i].become(Line(3.5 * np.array([np.cos(i * TAU / num), np.sin(i * TAU / num), 0]),
                                       3.5 *
                                       np.array(
                                           [np.cos(t.get_value() * i * TAU / num),
                                            np.sin(t.get_value() * i * TAU / num), 0]),
                                       stroke_width=1))
                    obj.set_color_by_gradient(
                        [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])

        decn.add_updater(lambda a: a.set_value(t.get_value()))
        enve.add_updater(anim)
        self.add(enve, decn, textn)
        self.play(t.set_value, 4, run_time=6, rate_func=linear)
