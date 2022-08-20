from manimlib import *

class ClockExampleScene(Scene):
    def construct(self):
        omega = -6 * DEGREES
        cir = Circle(radius=3, color=WHITE)
        # 添加刻度
        for i in range(60):
            percent = i / 60
            if i % 5 == 0:
                cir.add(Line(cir.pfp(percent), cir.pfp(percent) * 0.9))
            else:
                cir.add(Line(cir.pfp(percent), cir.pfp(percent) * 0.95))
        self.add(cir)
        # 秒针 分针 时针
        sec_handle = Line(DOWN / 4, UP * 2.7, stroke_width=3)
        minute_handle = Line(DOWN / 4, UP * 2, stroke_width=6)
        hour_handle = Line(DOWN / 4, UP * 1.5, stroke_width=9)

        self.add(hour_handle, minute_handle, sec_handle)

        def updater_sec(m: Mobject, dt: float):
            m.rotate(omega * dt, about_point=ORIGIN)

        def updater_minute(m: Mobject, dt: float):
            m.rotate(omega * dt / 60, about_point=ORIGIN)
        
        def updater_hour(m: Mobject, dt: float):
            m.rotate(omega * dt / 3600, about_point=ORIGIN)

        # 分别添加与时间相关的更新
        sec_handle.add_updater(updater_sec)
        minute_handle.add_updater(updater_minute)
        hour_handle.add_updater(updater_hour)

        self.wait(10)


'''
##### 1. 恒星行星模型：制作地球绕太阳公转，月球绕地球公转的动画。公转的速度、半径不做硬性要求。
'''

'''
class StarPlantExample(Scene):
    def construct(self):
        sun = Sphere(radius=1, color=RED)
        earth = Sphere(radius=0.5, color=BLUE)
        moon = Sphere(radius=0.2, color=YELLOW_A)

        earth.move_to(sun.get_center() + 3.5 * RIGHT)
        moon.move_to(earth.get_center() + 2 * RIGHT)

        self.add(sun, earth, moon)

        # 地球绕太阳转
        def update_earth(m: Mobject, dt: float):
            m.rotate(dt, about_point=sun.get_center())

        def update_moon(m: Mobject, dt: float):
            # 强行移动到地球的右侧
            m.move_to(earth.get_center() + 2 * RIGHT)
            # 根据动画已经运行的时间来旋转
            # self.time 是 Scene 的属性，用于记录动画总的运行时间
            # 其实用了 self.time 稍微就有点违背了原本的想法了，虽然这样写比较简单
            m.rotate(self.time * 3, about_point=earth.get_center())

        earth.add_updater(update_earth)
        moon.add_updater(update_moon)
        self.wait(10)
'''

'''
李萨如曲线：让一个物件按照李撒如图形的轨迹持续运动。李萨如图形的参数可自己给定。
'''

class LissajousExample(Scene):
    def construct(self):
        u = 4
        v = 5
        # 李萨如图形的参数曲线
        lissajous = ParametricCurve(
            lambda t: 3 * np.array([
                np.sin(u * t),
                np.sin(v * t),
                0
            ]),
            t_range=[0, TAU, 0.1],
            stroke_color=GREY
        )

        self.add(lissajous)

        dot = Dot(color=YELLOW)

        def update_dot(m: Mobject, dt: float):
            m.move_to(3 * np.array([
                np.sin(u * self.time / 3),
                np.sin(v * self.time / 3),
                0
            ]))
        dot.add_updater(update_dot)
        self.add(dot)
        self.wait(6)

'''
追逐曲线：一个正三角形的三个顶点分别以一定速度靠近同一侧相邻的顶点，画出每一帧三角形的位置。
'''

class TracingCurveExample(Scene):
    # 极坐标转换为笛卡尔坐标
    def polar2xyz(self, pho: float, theta: float):
        return pho * np.array([
            np.cos(theta),
            np.sin(theta),
            0
        ])

    def construct(self):
        r = 3
        # 3 个顶点
        a = Dot(self.polar2xyz(r, PI / 2), color=YELLOW)
        b = Dot(self.polar2xyz(r, PI / 2 + TAU / 3), color=YELLOW)
        c = Dot(self.polar2xyz(r, PI / 2 - TAU / 3), color=YELLOW)

        # 3 条边
        ab = Line(a.get_center(), b.get_center(), color=GOLD)
        bc = Line(b.get_center(), c.get_center(), color=GOLD)
        ca = Line(c.get_center(), a.get_center(), color=GOLD)

        # 使 3 条边始终连接 3 个顶点
        ab.add_updater(lambda l: l.put_start_and_end_on(a.get_center(), b.get_center()))
        bc.add_updater(lambda l: l.put_start_and_end_on(b.get_center(), c.get_center()))
        ca.add_updater(lambda l: l.put_start_and_end_on(c.get_center(), a.get_center()))

        self.add(ab, bc, ca)
        self.add(a, b, c)

        # 3 个顶点随时间向同一侧相邻点靠近
        a.add_updater(lambda m, dt: m.shift((b.get_center() - m.get_center()) * dt))
        b.add_updater(lambda m, dt: m.shift((c.get_center() - m.get_center()) * dt))
        c.add_updater(lambda m, dt: m.shift((a.get_center() - m.get_center()) * dt))

        # 轨迹
        trace = VGroup()

        # 向轨迹中不断添加三角形三边的拷贝
        def update_trace(m: Mobject, dt: float):
            m.add(ab.copy().clear_updaters().set_stroke(width=1))
            m.add(bc.copy().clear_updaters().set_stroke(width=1))
            m.add(ca.copy().clear_updaters().set_stroke(width=1))

        trace.add_updater(update_trace)
        self.add(trace)
        self.wait(4)

'''
东方弹幕游戏：对手每一帧都会改变弹幕的发射角，但是当弹幕发射出去之后，只会进行匀速直线运动，
直至飞出屏幕。你需要制作一张螺旋符卡，拥有 至少 3 条伪线，且发射角匀速变化。
'''

from my_videos.videos.danmku import Bullet


class Bullet(ArrowTip):
    def __init__(self, angle=0, **kwargs):
        super().__init__(**kwargs)
        self.data["points"][4] += LEFT*0.5
        self.scale(0.5)
        self.rotate(angle + PI)
        self.vector = normalize(rotate_vector(RIGHT, angle))

color_list = [RED, GOLD, YELLOW, GREEN, TEAL, BLUE, PURPLE]
v = 2

class Danmaku01(Scene):
    def construct(self):
        danmaku = VGroup()

        def update(m: Mobject, dt: float):
            m.add(Bullet(self.time ** 2 * 2))
            m.set_color_by_gradient(*color_list)

            for b in m:
                b.shift(v * dt * b.vector)
                if b.is_off_screen():
                    m.remove(b)

        danmaku.add_updater(update)
        self.add(danmaku)


class TimeExample(Scene):
    def construct(self):
        cur_time = DecimalNumber(0)
        cur_time.add_updater(lambda m, dt: m.set_value(self.time))
        self.add(cur_time)
        self.wait(10)