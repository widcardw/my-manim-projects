from manimlib import *


class FuncIntersection(Scene):
    def construct(self):
        axes = Axes(x_range=[-1, 10, 1],
                    y_range=[-1, 6, 1], width=11, height=7)
        self.add(axes)

        fx = axes.get_graph(lambda x: np.sqrt(x), x_range=[0, 9, 0.1])
        gx = axes.get_graph(lambda x: np.exp(x/2), x_range=[-1, 9, 0.1])
        a, b = 1, 3
        f = axes.get_graph(lambda x: np.sqrt(x), x_range=[a, b, 0.1])
        g = axes.get_graph(lambda x: np.exp(x/2), x_range=[a, b, 0.1])
        inter = VMobject(color=YELLOW, fill_opacity=0.2)
        inter.append_points(f.get_all_points()) \
            .add_line_to(g.get_end()) \
            .append_points(g.get_all_points()[::-1]) \
            .close_path()
        self.add(fx, gx, inter)
