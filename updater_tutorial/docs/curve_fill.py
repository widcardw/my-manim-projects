from manimlib import *
from manim_sandbox.utils.functions.debugTeX import AllPointsIndex

class TestCircle(Scene):
    def construct(self):
        cir = Circle(fill_opacity=1, stroke_width=0).scale(3)
        points = cir.get_all_points()

        # cir.reverse_points()
        tri = cir.get_triangulation()
        tri_indices = tri[len(points):]

        a = tri_indices[0::3]
        b = tri_indices[1::3]
        c = tri_indices[2::3]

        indices = AllPointsIndex(cir, color=YELLOW)

        self.add(cir)
        print(tri)

        for i, _ in enumerate(a):
            self.add(Polygon(points[a[i]], points[b[i]], points[c[i]],\
            stroke_color=WHITE, stroke_width=2, fill_opacity=0))

        # dots = DotCloud(points)
        self.add(indices)


class TestCurve(Scene):
    def construct(self) -> None:
        points = np.array([
            # [-1,-1,0],
            # [0, -1, 0],
            # [1, -1, 0],
            # [1, -1, 0],
            # [0.5, 0, 0],
            # [0, 1, 0],
            [0, 1, 0],
            [-2, 2, 0],
            [-1, -1, 0]
        ], dtype=np.float64)
        arc = VMobject(fill_opacity=1, fill_color=RED, stroke_width=0)
        arc.set_points(points)
        arc.scale(2.5).center()

        points = arc.get_all_points()

        dots = DotCloud(points, radius=0.1, color=YELLOW)

        poly = Polygon(*points, fill_color=BLUE_E, fill_opacity=1, stroke_width=0)
        
        # arc.set_fill()
        self.add(poly)
        self.add(arc)

        label1 = Text("对整个三角形上色", font="LXGW WenKai").set_color(RED).next_to(poly, LEFT)
        label2 = Text("蓝色部分透明度设置为 0", font="LXGW WenKai").set_color(BLUE_D).next_to(label1, DOWN, aligned_edge=LEFT)

        self.add(label1, label2)
        self.add(dots)
