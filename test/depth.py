from manimlib import *


class TestDepthTest(Scene):
    def construct(self) -> None:
        axes = ThreeDAxes()
        self.add(axes)
        line = Line(np.array([-2.5, 1, 1]), np.array([2.5, 1, 1]), stroke_width=10, color=GREEN).insert_n_curves(10)
        self.add(line)
        squ = Rectangle(5, 0.1, stroke_width=0, fill_opacity=1, fill_color=RED).shift(DOWN + IN)
        self.add(squ)
        t1 = Text("使用 Line 构造的直线").scale(0.6).next_to(line)
        t2 = Text("使用 Rectangle 模拟的直线").scale(0.6).next_to(squ)
        t1.fix_in_frame()
        t2.fix_in_frame()
        self.add(t1, t2)

        camera = self.camera.frame

        self.wait()
        self.play(camera.animate.set_orientation(Rotation([0.8, 0.2, 0.1, 0.8])))
        self.wait()
        # sphere = Sphere(color=BLUE)
        # line.apply_depth_test()
        # sphere.apply_depth_test()
        # axes.apply_depth_test()

        # self.add(axes, sphere, line)

        # graph = ParametricCurve(
        #     lambda t: np.array([np.cos(t), np.sin(t), t / 4]), t_range=[-5 * TAU, 5 * TAU]
        # )
        # self.add(graph)
