from manimlib.imports import *
from manim_sandbox.utils.imports import *


class Scene_(Scene):
    CONFIG = {"camera_config": {"background_color": "#1f252A"}}


# 二茂铁 抛物线
class Scene1(Scene_):
    def construct(self):
        hL = Line(color=BLUE).scale(7).shift(UP*3)
        dot0 = Dot(color=ORANGE).shift(UP*2)
        self.add(hL, dot0)
        vg = VGroup()
        doti = Dot(color=ORANGE).move_to(hL.get_start())
        l_1 = Line(color=WHITE, stroke_width=1.5).put_start_and_end_on(
            dot0.get_center(), doti.get_center())
        l_2 = l_1.copy().rotate(PI/2).scale(10).set_color(GOLD).set_stroke(width=6)
        doti.save_state()
        self.add(doti, l_1, l_2, vg)

        def anim(obj, alpha):
            doti.restore()
            doti.shift(RIGHT*hL.get_length()*alpha)
            l_1.put_start_and_end_on(dot0.get_center(), doti.get_center())
            l_2.become(l_1.copy().rotate(
                PI / 2).scale(100).set_color(GOLD).set_stroke(width=6))
            vg.add(l_2.copy().set_stroke(width=2, color=GOLD_E))

        self.play(UpdateFromAlphaFunc(doti, anim),
                  run_time=8, rate_func=linear)
        self.wait()


# fdd 贝塞尔曲线
class Scene2(Scene_):
    def construct(self):
        dot_a = Dot(np.array([-3, -3, 0]), color=PURPLE_A)
        dot_b = Dot(np.array([0, 3, 0]), color=PURPLE_A)
        dot_c = Dot(np.array([3, -3, 0]), color=PURPLE_A)
        l_1 = Line(color=BLUE).put_start_and_end_on(
            dot_a.get_center(), dot_b.get_center())
        l_2 = Line(color=BLUE).put_start_and_end_on(
            dot_b.get_center(), dot_c.get_center())
        l_3 = l_1.copy()
        lineG = VGroup()
        self.add(dot_a, dot_b, dot_c, l_1, l_2, l_3, lineG)

        self.i = 0

        def anim(obj, alpha):
            dot_a.move_to(l_1.point_from_proportion(alpha))
            dot_b.move_to(l_2.point_from_proportion(alpha))
            l_3.put_start_and_end_on(dot_a.get_center(), dot_b.get_center())
            self.i += 1
            if self.i % 4 == 0:
                lineG.add(l_3.copy().set_stroke(width=2, color=BLUE_B))
            # if int(alpha*100) % 5 == 0:  # 加if之后会间歇的加入中间的包络线
            #     lineG.add(l_3.copy().set_stroke(width=2, color=BLUE_A))
            # lineG.add(l_3.copy().set_stroke(
            #     width=2, color=BLUE_A))  # 这行的话最后是用线填充这个区域

        self.play(UpdateFromAlphaFunc(l_3, anim),
                  run_time=8, rate_func=linear)
        self.wait()


# fdd 贝塞尔曲线2
class BezierScene(Scene_):
    def construct(self):
        dot_a = Dot(np.array([-3, -3, 0]), color=WHITE)
        dot_b = Dot(np.array([0, 3, 0]), color=WHITE)
        dot_c = Dot(np.array([3, -3, 0]), color=WHITE)
        l_ab = Line(color=ORANGE).add_updater(
            lambda a: a.put_start_and_end_on(dot_a.get_center(), dot_b.get_center()))
        l_bc = Line(color=ORANGE).add_updater(
            lambda a: a.put_start_and_end_on(dot_b.get_center(), dot_c.get_center()))
        dotGroupAB = VGroup()
        dotGroupBC = VGroup()
        lineGroup = VGroup()
        div = 16
        for i in range(1, div):
            dotGroupAB.add(Dot().add_updater(
                lambda a: a.move_to(l_ab.point_from_proportion(i/div))))
            dotGroupBC.add(Dot().add_updater(
                lambda a: a.move_to(l_bc.point_from_proportion(i/div))))

        for i in range(div-1):
            lineGroup.add(Line(color=RED_A, stroke_width=1.5))
            lineGroup[i].add_updater(lambda a: a.put_start_and_end_on(
                dotGroupAB[i].get_center(), dotGroupBC[i].get_center()))

        self.add(dot_a, dot_b, dot_c, l_ab, l_bc,
                 dotGroupAB, dotGroupBC, lineGroup)
        # self.play(ShowCreation(lineGroup))
        # self.play(dot_a.move_to, np.array([-4, -2, 0]))
        # self.wait()


# 绿洲
class Scene3(Scene_):
    def construct(self):
        cir0 = Circle(color=BLUE_E, radius=1.5)
        l_up = Line(color=WHITE, stroke_width=1.5).shift(UP*1.5).scale(10)
        l_down = Line(color=WHITE, stroke_width=1.5).shift(DOWN*1.5).scale(10)
        dot_a = Dot(UP*1.5, color=ORANGE)
        dot_b = Dot(DOWN*1.5, color=ORANGE)
        dot_c = Dot(color=ORANGE).move_to(cir0.point_from_proportion(0))
        l_ac = Line(dot_a.get_center(), dot_c.get_center(), color=RED_A)\
            .scale(20, about_point=dot_a.get_center())
        l_bc = Line(dot_b.get_center(), dot_c.get_center(), color=RED_A)\
            .scale(20, about_point=dot_b.get_center())
        dot_p = Dot(color=ORANGE).move_to(
            get_intersect(l_down, l_ac, "parallel"))
        dot_q = Dot(color=ORANGE).move_to(
            get_intersect(l_up, l_bc, "parallel"))
        l_pq = Line(dot_p.get_center(), dot_q.get_center(), color=GREEN)
        linegroup = VGroup()
        self.add(cir0, l_up, l_down, dot_a, dot_b,
                 dot_c, l_ac, l_bc, dot_p, dot_q, l_pq, linegroup)
        self.i = 0

        def anim(obj, alpha):
            dot_c.move_to(cir0.point_from_proportion(alpha))
            if abs(get_norm(dot_a.get_center()-dot_c.get_center())) != 0 and\
                    abs(get_norm(dot_b.get_center()-dot_c.get_center())) != 0:
                l_ac.put_start_and_end_on(dot_a.get_center(), dot_c.get_center())\
                    .scale(20, about_point=dot_a.get_center())
                l_bc.put_start_and_end_on(dot_b.get_center(), dot_c.get_center())\
                    .scale(20, about_point=dot_b.get_center())
                dot_p.move_to(get_intersect(l_down, l_ac, DOWN*1.5))
                dot_q.move_to(get_intersect(l_up, l_bc, UP*1.5))
                l_pq.put_start_and_end_on(
                    dot_p.get_center(), dot_q.get_center())
                self.i += 1
                if self.i % 2 == 0:
                    linegroup.add(l_pq.copy().set_stroke(
                        width=1.5, color=GREEN_E))

        self.play(UpdateFromAlphaFunc(dot_c, anim),
                  run_time=8, rate_func=linear)
        self.wait()


# 鹤翔万里 椭圆
class EillpseScene1(Scene_):
    def construct(self):
        dot_o = Dot()
        cir_o = Circle(radius=3, color=BLUE)
        dot_a = Dot(LEFT*2, color=PURPLE)
        dot_p = Dot(cir_o.point_from_proportion(0), color=ORANGE)
        l_ap = Line(color=GREY).put_start_and_end_on(
            dot_a.get_center(), dot_p.get_center())
        l_pq = l_ap.copy().set_color(RED_A).rotate(
            PI/2, about_point=l_ap.get_end()).scale(20)
        lineGroup = VGroup()

        def anim(obj, alpha):
            dot_p.move_to(cir_o.point_from_proportion(alpha))
            l_ap.put_start_and_end_on(dot_a.get_center(), dot_p.get_center())
            l_pq.become(l_ap.copy().set_color(RED_A).rotate(
                PI/2, about_point=l_ap.get_end()).scale(20))
            lineGroup.add(l_pq.copy().set_stroke(width=1.5, color=RED))

        self.add(dot_o, cir_o, dot_a, dot_p, l_ap, l_pq, lineGroup)
        self.play(UpdateFromAlphaFunc(dot_p, anim),
                  run_time=8, rate_func=linear)
        self.wait()


# 绿洲 椭圆
class EllipseScene2(Scene_):
    def construct(self):
        l_1 = Line(np.array([-2, 2, 0]), np.array([-2, -3, 0]), color=BLUE_A)
        l_2 = Line(np.array([2, 0, 0]), np.array([-3, 0, 0]), color=BLUE_B)
        dot_a = Dot(l_1.get_start())
        dot_b = Dot(l_2.get_start())
        cir = Circle(radius=abs(get_norm(dot_a.get_center()-dot_b.get_center())), color=RED)\
            .move_to(dot_b.get_center()).set_plot_depth(1)
        envelop = VGroup()

        def anim(obj, alpha):
            dot_b.become(Dot(l_2.point_from_proportion(alpha)))
            dot_a.move_to(l_1.point_from_proportion(alpha))
            cir.become(Circle(radius=abs(get_norm(dot_a.get_center()-dot_b.get_center())), color=RED)
                       .move_to(dot_b.get_center()))
            envelop.add(cir.copy().set_stroke(width=1.5, color=RED_A))

        self.add(l_1, l_2, dot_a, dot_b, cir, envelop)
        self.play(UpdateFromAlphaFunc(dot_a, anim),
                  run_time=8, rate_func=linear)
        self.wait()


# widcardw 双曲线
class Hyperbola(Scene_):
    def construct(self):
        dot_o = Dot()
        cir = Circle(radius=1.5, color=GREEN)
        dot_a = Dot(RIGHT*3)
        dot_b = Dot(cir.point_from_proportion(0))
        l_ab = Line(dot_a.get_center(), dot_b.get_center(), color=BLUE)
        tgline = l_ab.copy().rotate(PI/2, about_point=l_ab.get_end()).set_color(GOLD).scale(40)
        envelop = VGroup()

        def anim(obj, alpha):
            dot_b.move_to(cir.point_from_proportion(alpha))
            l_ab.become(Line(dot_a.get_center(),
                             dot_b.get_center(), color=BLUE))
            tgline.become(l_ab.copy().rotate(
                PI/2, about_point=l_ab.get_end()).set_color(GOLD).scale(40))
            envelop.add(tgline.copy().set_stroke(color=GOLD_E, width=1.5))

        self.add(dot_o, cir, dot_a, dot_b, l_ab, tgline, envelop)
        self.play(UpdateFromAlphaFunc(dot_b, anim),
                  run_time=8, rate_func=linear)
        self.wait()

# widcardw 涡线


class Voltex(Scene_):
    def construct(self):
        cir_o = Circle(radius=1, color=GREEN).shift(DOWN).rotate(-PI/2)
        dot_p = Dot(DOWN*3)
        dot_q = Dot(cir_o.point_from_proportion(0))
        cir_q = Circle(color=BLUE, radius=abs(get_norm(dot_p.get_center()-dot_q.get_center())))\
            .move_to(dot_q.get_center())
        envelop = VGroup()

        def anim(obj, alpha):
            dot_q.move_to(cir_o.point_from_proportion(alpha))
            cir_q.become(Circle(color=BLUE, radius=abs(get_norm(dot_p.get_center()-dot_q.get_center())))
                         .move_to(dot_q.get_center()))
            envelop.add(cir_q.copy().set_stroke(width=1.5, color=BLUE_E))

        self.add(cir_o, dot_p, dot_q, cir_q, envelop)
        self.play(UpdateFromAlphaFunc(dot_q, anim),
                  run_time=8, rate_func=linear)
        self.wait()


# tf 外摆线
class Epicycloid(Scene_):
    def construct(self):
        cir_o = Circle(radius=2, color=GREEN)
        l_ab = Line(LEFT*2, RIGHT*2, color=GREEN)
        dot_p = Dot(cir_o.point_from_proportion(0.0001))
        cir_p = Circle(radius=abs(dot_p.get_center()[1]), color=PURPLE).move_to(
            dot_p.get_center())
        envelop = VGroup()

        def anim(obj, alpha):
            dot_p.move_to(cir_o.point_from_proportion(alpha))
            if abs(dot_p.get_center()[1]) > 0:
                cir_p.become(Circle(radius=abs(dot_p.get_center()[
                             1]), color=PURPLE).move_to(dot_p.get_center()))
                envelop.add(cir_p.copy().set_stroke(width=1.5, color=BLUE))

        self.add(cir_o, l_ab, dot_p, cir_p, envelop)
        self.play(UpdateFromAlphaFunc(dot_p, anim),
                  run_time=8, rate_func=linear)
        self.wait()


# zgh2000 追逐曲线
class ChaseCurve(Scene_):
    def construct(self):
        dot_a = Dot(np.array([0, 3, 0]))
        dot_b = Dot(np.array([2*math.sqrt(3), -3, 0]))
        dot_c = Dot(np.array([-2*math.sqrt(3), -3, 0]))
        l_1 = Line(dot_a.get_center(), dot_b.get_center(), color=GOLD)
        l_2 = Line(dot_b.get_center(), dot_c.get_center(), color=GOLD)
        l_3 = Line(dot_c.get_center(), dot_a.get_center(), color=GOLD)
        envelop = VGroup()

        def anim(obj, dt):
            dot_a.shift(0.01*(dot_b.get_center()-dot_a.get_center()))
            dot_b.shift(0.01*(dot_c.get_center()-dot_b.get_center()))
            dot_c.shift(0.01*(dot_a.get_center()-dot_c.get_center()))
            envelop.add(Line(dot_a.get_center(), dot_b.get_center(),
                             color=GOLD, stroke_width=1.5))
            envelop.add(Line(dot_b.get_center(), dot_c.get_center(),
                             color=GOLD, stroke_width=1.5))
            envelop.add(Line(dot_c.get_center(), dot_a.get_center(),
                             color=GOLD, stroke_width=1.5))

        envelop.add_updater(anim)
        self.add(dot_a, dot_b, dot_c, l_1, l_2, l_3, envelop)
        self.wait(8)
