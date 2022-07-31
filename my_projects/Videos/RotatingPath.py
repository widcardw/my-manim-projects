from manimlib.imports import *
from manim_sandbox.utils.imports import *


class Test1(Scene):

    def construct(self):
        cir_bg = Circle(radius=3, color=DARK_GREY)
        val = ValueTracker(0.)

        cir1 = Circle(radius=1.5, color=BLUE).shift(RIGHT*1.5)
        dot1 = Dot(color=RED)
        vec1 = Vector(LEFT*1.5, color=ORANGE).shift(RIGHT*1.5)
        cir1_ = VGroup(cir1, dot1, vec1)
        path1 = TracedPath(dot1.get_center, stroke_color=YELLOW,
                           min_distance_to_new_point=0.02)

        self.add(cir_bg, cir1_)

        def rotate_path(mob, dt):
            mob.rotate(val.get_value(), about_point=cir_bg.get_center())
            mob.rotate(-2*val.get_value(), about_point=mob[0].get_center())

        cir1_.add_updater(rotate_path)
        # group1=VGroup(cir1,dot1,vec1,path1)
        self.add(cir1_, path1)
        self.play(val.set_value, 2 * DEGREES)

        self.wait(10)


class Test2(Scene):

    def construct(self):
        ciro = Circle(radius=3, color=BLUE)
        cir1 = VGroup(
            Circle(radius=1.5),
            Vector(RIGHT*1.5, color=YELLOW)
        )
        cir1.save_state()

        def anim(mob, alpha):
            cir1.restore()
            cir1.rotate(-alpha*PI*2, about_point=cir1.get_center())
            cir1.shift(
                np.array([1.5*np.cos(alpha*TAU), 1.5*np.sin(alpha*TAU), 0]))

        self.add(cir1, ciro)
        self.play(UpdateFromAlphaFunc(cir1, anim),
                  run_time=5, rate_func=linear)
        self.wait(0.1)


class SweepSurface(SpecialThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_to_default_position()
        line = Line(ORIGIN, RIGHT*2, color=RED).shift(DOWN*2)
        # par = ParametricSurface(lambda u, v: np.array([, 0, 0]))
        self.add(line)
        var = ValueTracker(0)
        line.add_updater(lambda l: l.become(
            Line(np.array([0, 0, var.get_value()/PI-2]),
                 np.array([
                     2*np.cos(var.get_value()),
                     2*np.sin(var.get_value()),
                     var.get_value()/PI-2]), color=RED)
        ))
        self.play(var.set_value, TAU*2, run_time=4, rate_func=linear)
        self.wait()
