from manimlib import *


class TestRiemannRectangles(Scene):
    def construct(self):
        axes = Axes(width=10, height=4,
                    x_range=[-4, 4, 1], y_range=[-0.1, 0.6, 0.05])
        self.add(axes)

        def normal_distribution(x: float):
            return (1 / np.sqrt(2 * PI)) * np.exp(- x ** 2)

        graph = axes.get_graph(normal_distribution, x_range=[-4, 4, 0.1])
        self.add(graph)

        rects = axes.get_riemann_rectangles(
            graph, x_range=[-4, 4, 0.5], stroke_background=False, fill_opacity=[1., 0.5])
        self.add(rects)
