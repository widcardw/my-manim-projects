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


class planet(SpecialThreeDScene):
    def construct(self):
        self.set_camera_to_default_position()
        self.begin_ambient_camera_rotation(rate=0.01)
        t1 = ValueTracker(TAU)
        t2 = ValueTracker(TAU)
        sun = Sphere(radius=0.8, checkerboard_colors=[
                     RED_D, RED_E], fill_opacity=0.6)
        earth = Sphere(radius=0.4, checkerboard_colors=[
                       BLUE_D, BLUE_E], fill_opacity=0.6)
        moon = Sphere(radius=0.2, checkerboard_colors=[
                      YELLOW_D, YELLOW_E], fill_opacity=0.7)
        earth.add_updater(lambda a: a.move_to(
            sun.get_center()+3.5*np.sin(t1.get_value())*RIGHT+3.5*np.cos(t1.get_value())*IN))
        moon.add_updater(lambda b: b.move_to(
            earth.get_center()+1.6*np.sin(t2.get_value())*RIGHT+1.6*np.cos(t2.get_value())*UP+0.2*np.sin(t2.get_value())*IN))
        self.add(sun, earth, moon)
        self.play(t1.increment_value, 0.5*TAU,
                  t2.increment_value, -6*TAU, rate_func=linear, run_time=6)
        dsun = Sphere(radius=0.2, stroke_width=0,
                      checkerboard_colors=None, fill_color=RED, fill_opacity=1)
        dearth = Sphere(radius=0.1, stroke_width=0, checkerboard_colors=None, fill_opacity=1).add_updater(lambda a: a.move_to(
            dsun.get_center()+3.5*np.sin(t1.get_value())*RIGHT+3.5*np.cos(t1.get_value())*IN))
        dmoon = Sphere(radius=0.08, stroke_width=0, checkerboard_colors=None, fill_color=YELLOW, fill_opacity=1).add_updater(lambda b: b.move_to(
            dearth.get_center()+1.6*np.sin(t2.get_value())*RIGHT+1.6*np.cos(t2.get_value())*UP+0.2*np.sin(t2.get_value())*IN))
        self.add(dsun, dearth, dmoon)
        self.play(sun.set_opacity, 0,
                  earth.set_opacity, 0,
                  moon.set_opacity, 0, run_time=1/60)
        self.play(t1.increment_value, 0.5*TAU,
                  t2.increment_value, -6*TAU, rate_func=linear, run_time=6)
        self.stop_ambient_camera_rotation()
