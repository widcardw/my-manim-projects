from manimlib import *
from manim_sandbox.utils.functions.debugTeX import AllPointsIndex

# class TestCurveStroke(Scene):
#     def construct(self) -> None:
#         frame = self.camera.frame
#         frame.set_width(4).shift(UP/4)

#         points = np.array([
#             [-1, 0, 0],
#             [0, 1, 0],
#             [1, 0, 0]
#         ])

#         poly_points = np.array([
#             [-0.9, -0.1, 0],
#             [-1.1, 0.1, 0],
#             [0, 1.15, 0],
#             [1.1, 0.1, 0],
#             [0.9, -0.1, 0]
#         ])

#         poly = Polygon(*points, stroke_width=0, fill_opacity=1, fill_color=BLUE_E)
#         poly2 = Polygon(*poly_points, stroke_width=0, fill_opacity=1, fill_color=BLUE_D)
#         curve = VMobject(stroke_width=28, stroke_opacity=0.5)
#         curve.set_points(points)
#         indices = AllPointsIndex(curve, color=YELLOW, scale_factor=0.2, stroke_width=2)
#         self.add(poly2)
#         self.add(poly)
#         self.add(curve)

#         # label1 = Text("先对整个部分上色", font="LXGW WenKai").scale(0.3).next_to(poly, DOWN, buff=0.1)
#         # label2 = Text("再将不需要的部分擦除", font="LXGW WenKai").scale(0.3).next_to(label1, DOWN, buff=0.1)
#         self.add(indices)
#         # self.add(label1, label2)


class TestCornerStroke(InteractiveScene):
    def construct(self) -> None:
        frame = self.camera.frame

        frame.set_width(4)
        frame.shift(UP / 3)

        points = np.array([
            [0., 1., 0.],
            [0.5, 0., 0.],
            [-0.5, 0., 0.]
        ])
        
        v1 = VMobject(stroke_width=10)
        v1.start_new_path(points[0])
        v1.add_line_to(points[1])
        v1.add_line_to(points[2])
        v1.shift(LEFT)

        v2 = VGroup(
            Line(points[0], points[1]),
            Line(points[1], points[2])
        )
        v2.set_stroke(width=10, opacity=0.5)
        v2.shift(RIGHT)
        self.add(v1, v2)
        print(v2.stroke_shader_wrapper.vert_indices)        