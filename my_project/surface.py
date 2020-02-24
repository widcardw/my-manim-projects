from manimlib.imports import *


class test3(SpecialThreeDScene):

    def construct(self):
        self.set_camera_to_default_position()
        axes = ThreeDAxes()
        self.add(axes)
        self.wait(0.2)
        sphere1 = Sphere(radius=2, checkerboard_colors=None, fill_opacity=0.3)
        self.play(*[FadeInFrom(sphere1[i], sphere1[i].get_center()[0]*2*RIGHT+sphere1[i]
                               .get_center()[2]*2*OUT+sphere1[i].get_center()[1]*2*UP,
                               run_time=np.random.random()*2, rate_func=running_start)
                    for i in range(len(sphere1))])
        self.wait()
        self.play(*[FadeOutAndShift(sphere1[i], sphere1[i].get_center()[0]*2*RIGHT+sphere1[i]
                                    .get_center()[2]*2*OUT+sphere1[i].get_center()[1]*2*UP,
                                    run_time=np.random.random()*2, rate_func=running_start)
                    for i in range(len(sphere1))])
        self.wait()


class test2(SpecialThreeDScene):

    def construct(self):

        self.set_camera_to_default_position()
        axes = ThreeDAxes()
        self.add(axes)

        self.wait(0.2)
        sphere1 = Sphere(radius=2, checkerboard_colors=None, fill_opacity=0.3)
        self.play(*[GrowFromPoint(sphere1[i], point=ORIGIN, run_time=np.random.random()*2)
                    for i in range(len(sphere1))])
        self.wait()
        self.play(*[GrowFromPoint(sphere1[i], point=ORIGIN, run_time=np.random.random()*2, rate_func=re_running_start)
                    for i in range(len(sphere1))])
        self.wait()
