from manimlib.imports import *


# 用无数段3阶贝塞尔曲线来拟合n阶贝塞尔曲线
# 这只是权宜之计,今后可能会研究怎样直接绘制n阶贝塞尔曲线
class BezierFunc(ParametricFunction):
    CONFIG = {
        "steps_per_handle": 80,  # 每增加一个锚点,增加的曲线数量
    }

    def __init__(self, points, **kwargs):
        digest_config(self, kwargs)
        n = len(points) - 1
        self.step_size = 1 / (n * self.steps_per_handle)
        self.function = bezier(points)
        super().__init__(**kwargs)


class BezierGenerator(VGroup):
    CONFIG = {
        "dot_color": WHITE,
        "dot_scale": 1,
        "line_color": WHITE,
        "line_stroke_width": 2,
        "target_dot_color": RED,
        "tar_dot_scale": 1,
        "bezier_curve_color": ORANGE,
        "bzc_stroke_width": 6
    }

    def __init__(self, dot_list, **kwargs):
        VGroup.__init__(self, **kwargs)
        dot_color = self.dot_color
        line_color = self.line_color
        targ_dot_color = self.target_dot_color
        bzc_color = self.bezier_curve_color
        bzc_stroke_width = self.bzc_stroke_width
        listlen = len(dot_list)
        lg = VGroup()  # line group
        dg = VGroup()  # dot group
        for i in range(listlen):
            sub_dg = VGroup()
            for j in range(listlen - i):
                sub_dg.add(Dot(dot_list[j], color=dot_color).scale(self.dot_scale))
            dg.add(sub_dg)
        dg[-1][0].set_color(targ_dot_color).scale(self.tar_dot_scale)
        for i in range(listlen - 1):
            sub_lg = VGroup()
            for j in range(listlen - i - 1):
                sub_lg.add(Line(dot_list[j], dot_list[j + 1], color=line_color)
                           .set_stroke(width=self.line_stroke_width))
            lg.add(sub_lg)
        # path = TracedPath(dg[-1][0].get_center, stroke_color=bzc_color,
        #                   stroke_width=bzc_stroke_width)
        self.curve_path = BezierFunc(dot_list, stroke_color=bzc_color,
                                     stroke_width=bzc_stroke_width)
        # 原本这里用了TracedPath,但是一旦碰到点移动量不大或者折返时
        # 曲线就会出现方形,因此改用新定义的BezierFunc
        self.add(dg, lg)

    def dot_anim(self, obj, alpha):  # 迫于限制强行添加了一个obj参数
        n = len(self[0]) - 1
        for i in range(n):
            for j in range(n - i):
                self[0][i + 1][j].move_to(
                    interpolate(
                        self[0][i][j].get_center(),
                        self[0][i][j + 1].get_center(),
                        alpha
                    )
                )

    def sync_line(self, obj):  # 迫于限制强行添加了一个obj参数
        n = len(self[1])
        for i in range(1, n):
            for j in range(n - i):
                self[1][i][j].put_start_and_end_on(
                    self[0][i][j].get_center(), self[0][i][j + 1].get_center()
                )
        # 此处,如果两个连接直线的顶点距离过近,可能会报错
        # 如果用become(Line(...))也行,很暴力,注意别忘了把参数放进去
        # 另外,put_start_and_end_on不支持三维,如果要用到三维那么可能只能用become了


'''
class MakeBezier(Animation):  # 尚不完善, 路径的绘制有问题, 暂时先用MakeBezier2
    CONFIG = {
        "rate_func": smooth,
        "run_time": 6,
    }

    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)
        assert (isinstance(mobject, BezierGenerator))
        self.mobject = mobject
        self.curve_path = mobject.curve_path
        self.dot_anim = mobject.dot_anim
        self.sync_line = mobject.sync_line

    def interpolate_mobject(self, alpha):
        self.dot_anim(self.mobject[0], alpha)  # 查阅UpdateFromAlphaFunc
        self.sync_line(self.mobject[1])  # 查阅UpdateFromFunc
        self.interpolate_path(self.curve_path, alpha)

    def interpolate_path(self, path, alpha):
        families = list(zip(*[
            mob.family_members_with_points()
            for mob in [path, path.copy()]
        ]))
        for i, mobs in enumerate(families):
            sub_alpha = self.get_sub_alpha(alpha, i, len(families))
            path.pointwise_become_partial(path.copy(), 0, sub_alpha)
'''


class MakeBezier2(AnimationGroup):
    CONFIG = {
        "lag_ratio": 0,
        "rate_func": smooth,
        "run_time": 6,
    }

    def __init__(self, mobject, **kwargs):
        assert (isinstance(mobject, BezierGenerator))
        dot_anim = mobject.dot_anim
        sync_line = mobject.sync_line
        curve_path = mobject.curve_path
        super().__init__(
            UpdateFromAlphaFunc(mobject[0], dot_anim),
            UpdateFromFunc(mobject[1], sync_line),
            ShowCreation(curve_path),
            **kwargs
        )


# 使用例desu
class TestBezier(Scene):
    def construct(self):
        dot_lst = [
            np.array([-3, -3, 0]),
            np.array([-3, 3, 0]),
            np.array([3, 3, 0]),
            np.array([3, -3, 0]),
        ]
        obj = BezierGenerator(dot_lst)
        dot_anim = obj.dot_anim  # 点的动画函数(本质是function)
        line_anim = obj.sync_line  # 直线的更新函数(本质是Function)
        path = obj.curve_path  # 形成的贝塞尔曲线(本质是VMobject)
        obj[1].add_updater(line_anim)  # 给直线加上更新函数
        self.add(obj)  # 添加点和直线物件
        self.play(UpdateFromAlphaFunc(obj[0], dot_anim),  # 使点的位置从初始移动到结束,直线也随之更新
                  ShowCreation(path),  # 播放贝塞尔曲线的创建动画,与上面的同步
                  run_time=4
                  )


class TestBezier2(Scene):
    def construct(self):
        dot_lst = [
            np.array([-3, -3, 0]),
            np.array([-3, 3, 0]),
            np.array([3, 3, 0]),
            np.array([3, -3, 0]),
        ]
        obj = BezierGenerator(dot_lst)
        self.play(MakeBezier2(obj))
