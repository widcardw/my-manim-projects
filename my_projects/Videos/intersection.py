from manimlib.imports import *


class TwoCircleIntersection(VMobject):
    def __init__(self, cir1, cir2, **kwargs):
        assert (isinstance(cir1, Circle))
        assert (isinstance(cir2, Circle))
        VMobject.__init__(self, **kwargs)
        r1 = cir1.get_width() / 2
        r2 = cir2.get_width() / 2
        vec_r1tor2 = cir1.get_center() - cir2.get_center()
        distance = abs(get_norm(vec_r1tor2))
        if abs(r1 - r2) < distance < r1 + r2:
            ang = np.arccos((r1 ** 2 + distance ** 2 - r2 ** 2) / (2 * r1 * distance))
            rotate_matrix1 = np.array([
                [np.cos(ang), -np.sin(ang), 0],
                [np.sin(ang), np.cos(ang), 0],
                [0, 0, 0]
            ])
            rotate_matrix2 = np.array([
                [np.cos(-ang), -np.sin(-ang), 0],
                [np.sin(-ang), np.cos(-ang), 0],
                [0, 0, 0]
            ])
            p1 = cir1.get_center() + np.dot(-vec_r1tor2, rotate_matrix1) / distance * r1
            p2 = cir1.get_center() + np.dot(-vec_r1tor2, rotate_matrix2) / distance * r1
            ang2 = np.arccos((r2 ** 2 + distance ** 2 - r1 ** 2) / (2 * r2 * distance))
            self.points = np.vstack(
                (ArcBetweenPoints(p1, p2, 2 * ang).points,
                 ArcBetweenPoints(p1, p2, -2 * ang2).points)
            )
        elif distance <= abs(r1 - r2):
            if r1 > r2:
                self.points = cir2.points
            else:
                self.points = cir1.points
        else:
            pass


class Test(Scene):
    def construct(self):
        axes = Axes()
        cir1 = Circle(radius=2).shift(RIGHT).set_stroke(opacity=0.4)
        cir2 = Circle(radius=1).shift(UP).set_stroke(opacity=0.4)
        inter = TwoCircleIntersection(cir1, cir2)
        self.add(axes, cir1, cir2, inter)
