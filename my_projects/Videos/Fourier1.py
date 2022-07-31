from manimlib.imports import *
from manim_sandbox.utils.imports import *


class Scene1(Scene):
    def construct(self):
        bg = NumberPlane().scale(2)
        cir1 = Circle(radius=2, color=GREY, stroke_width=2)
        vec1 = Vector(RIGHT*2, color=YELLOW)
        vec2 = Vector(RIGHT*1.2, color=YELLOW)
        vec3 = Vector(RIGHT*0.8, color=YELLOW)
        vec2.save_state()
        vec3.save_state()
        vec2.shift(vec1.get_vector())
        vec3.shift(vec1.get_vector()+vec2.get_vector())
        self.add(bg, cir1, vec1, vec2, vec3)

        def vec2_anim(mob):
            vec2.restore()
            vec2.shift(vec1.get_vector())
            vec2.rotate(-3*vec1.get_angle(), about_point=vec1.get_end())

        def vec3_anim(mob):
            vec3.restore()
            vec3.shift(vec2.get_end())
            vec3.rotate(2*vec1.get_angle(), about_point=vec2.get_end())

        vec2.add_updater(vec2_anim)
        vec3.add_updater(vec3_anim)

        path = TracedPath(vec3.get_end, stroke_color=ORANGE, stroke_width=8)
        self.add(path)

        # def path_anim(mob):
        #   path.shift(DOWN*0.03)

        # path.add_updater(path_anim)

        def rot(mob, dt):
            vec1.rotate(dt*60*DEGREES, about_point=ORIGIN)

        vec1.add_updater(rot)

        self.wait(20)
        # self.play(Rotating(vec1,about_point=UP,run_time=8))
