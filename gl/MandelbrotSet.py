from manimlib import *
from manim_sandbox.utils.mobjects.DragDot import DragDot


def z_func(z, c):
    return z ** 2 + c


class TestMandelbrot(Scene):
    CONFIG = {
        'it_times': 20,
    }

    def init_camera(self):
        frame = self.camera.frame
        frame.set_height(4)

    def setup(self):
        self.init_camera()
        self.plane = ComplexPlane(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1],
            width=4, height=4
        )
        self.plane.add_coordinate_labels()
        self.add(self.plane)

        self.ddot = DragDot(LEFT, color=YELLOW)

        dots = [TrueDot(color=GREEN).scale(0.7).make_3d() for i in range(self.it_times + 1)]
        lines = [Line(stroke_width=2) for i in range(self.it_times)]

        for i in range(self.it_times):
            self.update_dots(dots[i + 1], dots[i])
            self.update_lines(lines[i], dots[i + 1], dots[i])

        self.add(*lines, *dots)

        self.add(self.ddot)

    def update_dots(self, z_n_1, z_n):
        z_n_1.add_updater(lambda a: a.move_to(
            self.plane.n2p(
                z_func(
                    self.plane.p2n(z_n.get_center()),
                    self.plane.p2n(self.ddot.get_center())
                )
            )
        ))

    def update_lines(self, line, z_n_1, z_n):
        line.add_updater(lambda a: a.put_start_and_end_on(
            z_n_1.get_center(), z_n.get_center()
        ))

