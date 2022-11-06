from manimlib import *


class TriangleHeightScene(Scene):
    def construct(self) -> None:
        triangle = Triangle().scale(3)
        self.add(triangle)

        dot_p = Dot(color=ORANGE).move_to(triangle.get_vertices()[1])
        alpha = ValueTracker(0.)

        def put_p_on_bottom(p: Mobject):
            p.move_to(interpolate(*triangle.get_anchors()[2:4], alpha.get_value()))

        dot_p.add_updater(put_p_on_bottom)

        self.add(dot_p)

        line_height = Line()

        def line_updater(line: Mobject):
            if not isinstance(line, Line):
                return
            if -0.05 < np.dot(line.get_vector(), triangle.get_vertices()[2] - triangle.get_vertices()[1]) < 0.05:
                line.set_color(YELLOW)
            else:
                line.set_color(WHITE)
            line.put_start_and_end_on(triangle.get_start(), dot_p.get_center())

        line_height.add_updater(line_updater)
        self.add(line_height, dot_p)

        self.play(alpha.animate.set_value(0.5))
        self.wait()
        # self.play(alpha.animate.set_value(1.0))
        self.wait()
