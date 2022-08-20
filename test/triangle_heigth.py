from manimlib import *


class TriangleHeightScene(Scene):
    def construct(self) -> None:
        triangle = Triangle().scale(3)
        self.add(triangle)

        dot_p = Dot(color=ORANGE).move_to(triangle.get_vertices()[1])
        alpha = ValueTracker(0.)

        def put_p_on_bottom(p: Dot):
            p.move_to(interpolate(*triangle.get_anchors()[2:4], alpha.get_value()))

        dot_p.add_updater(put_p_on_bottom)

        self.add(dot_p)

        line_height = Line()

        def line_updater(l: Line):
            if -0.05 < np.dot(l.get_vector(), triangle.get_vertices()[2] - triangle.get_vertices()[1]) < 0.05:
                l.set_color(YELLOW)
            else:
                l.set_color(WHITE)
            l.put_start_and_end_on(triangle.get_start(), dot_p.get_center())

        line_height.add_updater(line_updater)
        self.add(line_height, dot_p)

        self.play(alpha.animate.set_value(0.5))
        self.wait()
        # self.play(alpha.animate.set_value(1.0))
        self.wait()
