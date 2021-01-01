from manimlib.imports import *
from manim_sandbox.utils.imports import *


class TestDanma(Scene):
    def construct(self):
        color_map = [RED_A, RED_B, RED_C,
                     GOLD_D, GOLD_C, GOLD_B, GOLD_A,
                     YELLOW_E, YELLOW_D, YELLOW_C, YELLOW_B,
                     GREEN_A, GREEN_B, GREEN_C,
                     TEAL_A, TEAL_B, TEAL_C, TEAL_D,
                     BLUE_C, BLUE_D,
                     PURPLE_A, PURPLE_B, PURPLE_C, PURPLE_D,
                     ]

        def mysum(frame, time, a):
            count = 0
            for i in range(frame-time+1):
                count += i*a
            return count
        f = 5
        a = PI/180*0.1
        v = 0.5

        def func(v, time, frame, a):
            t = math.floor(time)
            return np.array([v*t*np.cos(mysum(frame, t, a))*0.05,
                             v*t*np.sin(mysum(frame, t, a))*0.05, 0])

        dotg_0 = VGroup()
        for t in range(min(f, 200)):
            dot_i = Dot(func(v, t, f, a), color=RED).scale(0.5)
            dotg_0.add(dot_i)
        self.add(dotg_0)
        for f in range(300):
            dotg_i = VGroup()
            for t in range(min(f, 180)):
                dot_j = Dot(func(v, t, f, a)).scale(0.5).set_color(
                    color_map[math.floor(t/20) % len(color_map)])
                dotg_i.add(dot_j)
            self.play(Transform(dotg_0, dotg_i), run_time=1/200)
            vg_rm = VGroup()
            for obj in self.mobjects:
                if get_line_long(obj.get_center(), ORIGIN) >= 10:
                    vg_rm.add(obj)
            self.remove(vg_rm)


class Test2(Scene):
    def construct(self):
        color_map = [RED_A, RED_B, RED_C,
                     GOLD_D, GOLD_C, GOLD_B, GOLD_A,
                     YELLOW_E, YELLOW_D, YELLOW_C, YELLOW_B,
                     GREEN_A, GREEN_B, GREEN_C,
                     TEAL_A, TEAL_B, TEAL_C, TEAL_D,
                     BLUE_C, BLUE_D,
                     PURPLE_A, PURPLE_B, PURPLE_C, PURPLE_D,
                     ]

        def mysum(time, frame, cont):
            count = 0
            for i in range(frame-time+1):
                count += i*cont
            return count

        def myfunc(v, t, f, a):
            t_ = math.floor(t)
            return np.array([
                v*t_*np.cos(mysum(t_, f, a)),
                v*t_*np.sin(mysum(t_, f, a)), 0
            ])
        f = 1
        a = DU*0.05
        v = 0.015

        dot_0 = Dot(myfunc(v, 1, f, a), color=RED).scale(0.7)
        self.add(dot_0)
        for f in range(0, 1100, 100):
            dot_i_group = VGroup()
            for t in range(min(f, 490)):
                dot_i = Dot(myfunc(v, t, f, a)).scale(0.7).set_color(
                    color_map[math.floor(t/20) % len(color_map)])
                dot_i_group.add(dot_i)
            self.play(Transform(dot_0, dot_i_group), run_time=1/60)
            vg_rm = VGroup()
            for obj in self.mobjects:
                if get_line_long(obj.get_center(), ORIGIN) >= 14:
                    vg_rm.add(obj)
            self.remove(vg_rm)
