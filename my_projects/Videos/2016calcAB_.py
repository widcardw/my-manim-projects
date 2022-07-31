# from big_ol_pile_of_manim_imports import*
from manimlib.imports import *
# from manimlib.debug import *
import numpy as np


class triangle(GraphScene):
    CONFIG = {
        "start_x": 0.5,
        "big_x": 5,
        "dx": 0.001,
        "x_min": -3,
        "x_max": 9,
        "y_min": -3,
        "y_tick_frequency": 1,
        "y_max": 6,
        "x_labeled_nums": list(range(-1, 1, 1)),
        "y_labeled_nums": list(range(-1, 1, 1)),
        "graph_origin": 1 * DOWN + 2 * LEFT,  # 设置调整坐标轴的选项
    }

    def construct(self):
        self.draw_graph()
        # self.show_move()
        # self.emphmax()

    def draw_graph(self):
        func = lambda x: np.log(2 * x) - 1 / 2 * x + 5
        self.setup_axes(animate=True)
        graph = self.get_graph(func, x_min=0.01, color=RED, step_size=0.001)

        func_label = TexMobject(r"f(x)=\ln (2x)-\frac12 x+5").scale(0.5)
        func_label.next_to(graph, direction=LEFT, buff=LARGE_BUFF)

        self.graph = graph
        self.func = func

        dotA = Dot(self.coords_to_point(1, 0), color=BLUE)
        dotB = Dot(self.coords_to_point(5, 0), color=BLUE)
        dotC = Dot(point=self.coords_to_point(self.start_x, func(self.start_x)), color=BLUE)

        self.dotA = dotA.set_plot_depth(1)
        self.dotB = dotB.set_plot_depth(1)
        self.dotC = dotC.set_plot_depth(1)
        c_controller = ValueTracker(self.start_x)
        # self.dotC.add_updater(lambda d: d.move_to(self.coords_to_point(c_controller.get_value(), func(c_controller.get_value()))))
        triangle = self.get_triangle().add_updater(lambda tri: [
            self.dotC.move_to(self.coords_to_point(c_controller.get_value(), func(c_controller.get_value()))),
            tri.become(self.get_triangle())])
        labelgroup = self.get_point_label().add_updater(
            lambda l, dt: l[2].next_to(self.dotC, direction=RIGHT, buff=SMALL_BUFF))

        self.play(
            ShowCreation(graph),
            Write(func_label),
            rate_func=smooth
        )
        self.play(
            FadeInFromDown(dotA),
            FadeInFromDown(dotB),
            FadeInFromDown(dotC),
            rate_func=smooth
        )
        self.wait()

        self.play(Write(labelgroup))
        self.wait()
        self.play(ShowCreation(triangle))
        self.wait()
        self.play(c_controller.set_value, 8, rate_func=there_and_back, run_time=8)
        self.wait()

    def get_point_label(self):
        labelgroup = VGroup()

        labelA = TextMobject("A").scale(0.5)
        labelA.next_to(self.dotA, direction=UL * 0.75, buff=SMALL_BUFF)

        labelB = TextMobject("B").scale(0.5)
        labelB.next_to(self.dotB, direction=UP, buff=SMALL_BUFF)

        labelC = TextMobject("C").scale(0.5)
        labelC.next_to(self.dotC, direction=RIGHT, buff=SMALL_BUFF)

        labelgroup.add(labelA, labelB, labelC)

        return labelgroup

    def get_triangle(self):
        triangle = Polygon(self.dotA.get_center(), self.dotB.get_center(), self.dotC.get_center(),
                           stroke_width=2, stroke_color=WHITE, fill_opacity=0.6, fill_color=PINK)

        return triangle
