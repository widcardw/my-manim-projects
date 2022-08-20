from manimlib import *
# from my_videos.utils.old_parametric_surface import *


class TestSphere(Scene):
    def construct(self):
        day_texture = "images/PureImg.png"

        s1 = Sphere(radius=1).shift(UP * 2)
        s2 = Sphere(radius=2).set_opacity(0.1)
        s1.apply_depth_test()
        s2.apply_depth_test()
        # s2.set_color_by_rgba_func(lambda p: np.array([0.5, 0.75, 1.0, 0.2]))
        # s2.set_color_by_code("color.a = 0.2;")
        self.add(s2, s1)


# class PureImg(Scene):
#     def construct(self):
#         rect = Rectangle(FRAME_WIDTH, FRAME_HEIGHT, stroke_width=0, color=BLUE, fill_opacity=0.2)
#         self.add(rect)

# class TestOldSphere(Scene):
#     def construct(self):
#         s1 = OldSphere(radius=1).set_fill(opacity=0.2, color=BLUE).set_stroke(width=0)
#         s2 = OldSphere(radius=2).set_fill(opacity=0.2, color=RED).set_stroke(width=0)
#         self.play(ShowCreation(s2))
#         self.play(ShowCreation(s1))