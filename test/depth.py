from manimlib import *


class TestDepthTest(Scene):
    def construct(self) -> None:
        axes = ThreeDAxes()
        line = Line(np.array([0, 0, 0]), np.array([3, 3, 3]))
        sphere = Sphere(color=BLUE)
        line.apply_depth_test()
        sphere.apply_depth_test()
        axes.apply_depth_test()

        self.add(axes, sphere, line)
