from manimlib.imports import *


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
        lg = VGroup()
        dg = VGroup()
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
        path = TracedPath(dg[-1][0].get_center, stroke_color=bzc_color,
                          stroke_width=bzc_stroke_width)
        self.add(dg, lg, path)

    def dot_anim(self, obj, alpha):
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

    def sync_line(self, obj):
        n = len(self[1])
        for i in range(1, n):
            for j in range(n - i):
                self[1][i][j].put_start_and_end_on(
                    self[0][i][j].get_center(), self[0][i][j + 1].get_center()
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
        dot_anim = obj.dot_anim
        line_anim = obj.sync_line
        obj[1].add_updater(line_anim)
        self.add(obj)
        self.play(UpdateFromAlphaFunc(obj, dot_anim), run_time=4)
