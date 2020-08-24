from manimlib.imports import *
from manim_sandbox.imports import *
# 注意:DarkScene为我自定义背景色的场景,
# 若想要使用,请将以下代码取消注释
# class DarkScene(Scene):
# 	CONFIG = {"camera_config":{"background_color":"#1f252A"}}


class MoveToTargetExample(DarkScene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)
        A.generate_target()  # copyA自身形成A的target属性
        A.target.scale(3).shift(RIGHT*7+UP*2)  # 操作A的target

        self.add(A)
        self.wait()
        self.play(MoveToTarget(A))
        self.wait()


class MoveToTargetExample2(DarkScene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)
        A.generate_target()  # copyA自身形成A的target属性
        A.target.become(Square().shift(RIGHT*2+UP*1))

        self.add(A)
        self.wait()
        self.play(MoveToTarget(A))
        self.wait()


class UpdateTest(DarkScene):
    def construct(self):
        dotA = Dot().shift(RIGHT)
        dotB = Dot().shift(RIGHT*3)
        textA = TextMobject("A").next_to(dotA)
        textB = TextMobject("B").next_to(dotB)
        self.add(dotA, dotB, textA, textB)

        # def nextFunc(obj, tar):
        #     obj.add_updater(lambda a:a.next_to(tar, RIGHT))

        # nextFunc(textA, dotA)
        # nextFunc(textB, dotB)

        textA.add_updater(lambda a: a.next_to(dotA, RIGHT))
        textB.add_updater(lambda a: a.next_to(dotB, RIGHT))

        self.play(
            Rotating(dotA, about_point=ORIGIN),
            Rotating(dotB, about_point=ORIGIN),
            run_time=2
        )
        textA.remove_updater(lambda a: a.next_to(dotA, RIGHT))  # 無駄
        textB.clear_updaters()
        self.play(
            Rotating(dotA, about_point=ORIGIN),
            Rotating(dotB, about_point=ORIGIN),
            run_time=2
        )


class ValueTrackerScene(DarkScene):
    def construct(self):
        numline = NumberLine()
        t = ValueTracker(-2)
        ruler = Triangle(fill_opacity=1, color=WHITE).scale(
            0.1).rotate(PI).move_to(np.array([0, 0.5, 0]))
        dec = DecimalNumber(0)
        ruler.add_updater(lambda a: a.move_to(
            np.array([t.get_value(), 0.5, 0])
        ))
        dec.add_updater(lambda a: a.set_value(t.get_value()))
        dec.add_updater(lambda a: a.next_to(ruler, UP))
        self.add(numline, ruler, dec)
        self.play(t.set_value, 2, rate_func=there_and_back, run_time=4)


class ValueTrackerScene2(DarkScene):
    def construct(self):
        axes = Axes()
        t = ValueTracker(0)
        cir = Circle(radius=2).shift(LEFT*5)

        # dot_o = Dot(LEFT*5)
        # text_o = TexMobject("O").next_to(dot_o, DOWN)
        # dot_a = Dot(LEFT*3)
        # text_a = TexMobject("A").next_to(dot_a, DOWN+RIGHT)
        # l_oa = Line(LEFT*5, LEFT*3)

        dot_p = Dot().add_updater(lambda a: a.move_to(
            np.array([-5+2*np.cos(t.get_value()), 2*np.sin(t.get_value()), 0])
        ))
        # text_p = TexMobject("P").add_updater(
        #     lambda a:a.move_to(dot_o.get_center()+1.2*(dot_p.get_center()-dot_o.get_center())))
        # l_op = Line().add_updater(lambda a:a.put_start_and_end_on(
        #     dot_o.get_center(), dot_p.get_center()
        #     ))
        # arc = Arc(angle=0).shift(LEFT*5)
        # arc.add_updater(lambda a:a.become(
        #     Arc(start_angle=0, angle=t.get_value()%TAU, color=ORANGE).shift(LEFT*5)
        #     ))

        dot_q = Dot().add_updater(lambda a: a.move_to(
            np.array([-2, 2*np.sin(t.get_value()), 0])
        ))
        l_pq = DashedLine().add_updater(lambda a: a.put_start_and_end_on(
            dot_p.get_center(), dot_q.get_center()
        ))

        path = TracedPath(dot_q.get_center,
                          stroke_color=YELLOW, stroke_width=6)
        path.add_updater(lambda a: a.shift(RIGHT*0.04))

        self.add(cir, dot_p, dot_q, l_pq, path)
        self.play(t.set_value, 2*TAU, run_time=8, rate_func=linear)


# 03
class UpdateFromFuncExample2(DarkScene):
    def construct(self):
        r0 = 3
        r1 = 1
        cir0 = Circle(radius=r0, color=BLUE)
        gear0 = Gear_outline(pitch_circle_radius=r0, tooth_hight=0.2,
                             tooth_num=int(r0*20), stroke_color=BLUE, stroke_opacity=0.3)
        vec0 = Vector(RIGHT*(r0-r1), color=YELLOW)

        cir1 = Circle(radius=r1, color=BLUE_B)
        vec1 = Vector(RIGHT*0.8*r1, color=YELLOW_B)
        gear1 = Gear_outline(pitch_circle_radius=r1, tooth_hight=0.2,
                             tooth_num=int(r1*20), stroke_color=BLUE, stroke_opacity=0.3)
        gup1 = VGroup(cir1, vec1, gear1).shift(RIGHT*(r0-r1))

        dt = 1/self.camera.frame_rate

        def anim0(obj):
            obj.rotate(dt, about_point=ORIGIN)

        def anim1(obj):
            obj.move_to(vec0.get_end())
            obj.rotate(-(r0-r1)/r1*dt, about_point=vec1.get_start())

        path = TracedPath(vec1.get_end, stroke_width=2, stroke_color=RED_B)

        self.add(cir0, vec0, gear0, gup1, path)
        self.play(UpdateFromFunc(vec0, anim0),
                  UpdateFromFunc(gup1, anim1),
                  run_time=2*TAU, rate_func=linear)

'''
def debugPoints(self, obj):
	for i,points in enumerate(obj.get_points()):
		point_id = Integer(i).scale(0.5).set_color(PURPLE_A)
		point_id.move_to(points)
		self.add(point_id)
'''
# 锚点测试
class PointsTest(DarkScene):
    def construct(self):
        obj = Circle().scale(3)
        obj.points[1:3] += RIGHT
        debugPoints(self, obj)
        self.add(obj)
