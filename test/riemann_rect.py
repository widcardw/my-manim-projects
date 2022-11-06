from manimlib import *


class TestRiemann(InteractiveScene):
    def construct(self) -> None:
        axes = Axes()
        graph = axes.get_graph(
            lambda x: 2 * np.exp(-(x*0.2)**2),
            x_range=[-8, 8, 0.1],
        )
        self.add(axes)
        self.add(graph)
        rects = axes.get_riemann_rectangles(
            graph, [-8, 8, 1], stroke_background=True)
        self.play(ShowCreation(rects))
        self.wait(0.5)
        self.play(
            rects.animate.become(axes.get_riemann_rectangles(
                graph, [-8, 8, 0.5], stroke_background=True))
        )
        self.wait(0.5)
        self.play(
            rects.animate.become(axes.get_riemann_rectangles(
                graph, [-8, 8, 0.25], stroke_background=True))
        )
        self.wait(0.5)
        self.play(
            rects.animate.become(axes.get_riemann_rectangles(
                graph, [-8, 8, 0.125], stroke_background=True))
        )
